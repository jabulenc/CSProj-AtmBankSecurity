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
            data = q.get()
            queueLock.release()
            # Process here
            # idea - for each password, create saltpasspepp hash
            # check against hash received
            # check for matching -
            # if false, continue. Else, write pass and grab next item.
            # Need to handle for no-match
            result = base64.b64encode(hashlib.sha256('CMSC414'+ pw +'Fall16').digest())
            if result in hashes:
                #done
                print pw
                continue
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

# Wait for all threads to complete
for t in threads:
    t.join()
