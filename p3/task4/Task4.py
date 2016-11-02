#!/usr/bin/python
import sys
import Queue
import threading
import time
import multiprocessing
import hashlib
import base64

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.q = q
    def run(self):
        crack(self.q)

def crack(q):
	while not exitFlag:
			queueLock.acquire()
			if not workQueue.empty():
				print 'getting new hash'
				data = q.get()
				queueLock.release()
				for pw in pws:
					pw = pw.strip()
					result = base64.b64encode(hashlib.sha256('CMSC414'+ pw +'Fall16').digest())
					#print result
					if result in hashes:
						outfile.write(pw)
						print pw
						break
					else:
						continue
			else:
				queueLock.release()
        #time.sleep(1) May not need this line at all

pwfilename = sys.argv[1]
hashfilename = sys.argv[2]
cpus = multiprocessing.cpu_count()
queueLock = threading.Lock()
workQueue = Queue.Queue(100)
threads = []
pws = tuple(open(pwfilename, 'rb'))
hashes = tuple(open(hashfilename, 'r'))
outfile = open('cracked.txt', 'w')
print cpus
# Fill the queue
queueLock.acquire()
for hash in hashes:
    workQueue.put_nowait(hash.strip()) #strip all whitespace
queueLock.release()

# Create new threads
for x in xrange(cpus):
    thread = myThread(x, workQueue)
    thread.start()
    threads.append(thread)

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

outfile.close()

# Wait for all threads to complete
for t in threads:
    t.join()
