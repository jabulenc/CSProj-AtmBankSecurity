#!/bin/sh

#  CheckSubmissionFiles.sh
#  
#
#  Created by Chengxi Ye on 9/1/15.
#

if [ ! $# -eq 1 ]
then
echo "Usage: $0 <student directory>"
exit 1
fi

studentdir=$1

if [ ! -d $studentdir ]
then
echo "Directory $1 doesn't exist"
exit 1
fi


echo "Checking files in $studentdir"


for x in 1 2 3
do
echo ""
echo "==[Lottery $x]=="
if [ ! -f $studentdir/lottery$x.c ]
then
echo "     $studentdir does not include file lottery$x.c"
fi
done

for x in 1 2
do
echo ""
echo "==[Exploit $x]=="
if [ ! -f $studentdir/exploit_$x.c ]
then
echo "     $studentdir does not include file exploit_$x.c"
fi
done


for fname in $studentdir/targetaddr.txt $studentdir/exploit_3_1000.c $studentdir/exploit_3_10000.c $studentdir/exploit_3_100000.c $studentdir/task4/store.c $studentdir/task4/repeat.c $studentdir/security_review.txt
do
if [ ! -f $fname ]
then
echo ""
echo "$studentdir does not include file $fname"
fi
done