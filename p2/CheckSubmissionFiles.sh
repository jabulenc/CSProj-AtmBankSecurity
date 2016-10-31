#!/bin/sh

# CheckSubmissionFiles.sh
#
# Usage: sh CheckSubmissionFiles.sh <student_directory>
# Checks if all files required for submission are in <student_directory>


if [ ! $# -eq 1 ]
	then 
	echo "Usage: $0 <student directory>"
	exit 1
fi

studentdir=$1

if [ ! -d $studentdir ]
	then
	echo "Directory $1 does not exist"
	exit 1
fi

echo "Checking files in $studentdir"

for x in 1 2 3 4 5 6 7 
do
	echo ""
	echo "==[Task $x]=="
	if [ $x == 4 ] || [ $x ==5 ]
		then
		if [ ! -f $studentdir/task$x.html ]
			then
			echo "Missing task$x.html"
		fi
	elif [ $x == 1 ]
		then
		if [ ! -f $studentdir/HTTPSimpleForge.java ]
			then
			echo "Missing HTTPSimpleForge.java"
		fi
	else
		if [ ! -f $studentdir/task$x.txt ]
			then
			echo "Missing task$x.txt"
		fi
	fi
done




