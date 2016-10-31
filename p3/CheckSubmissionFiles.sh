#!/bin/bash

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

filenames[0]=task1a.bin
filenames[1]=task1.key
filenames[2]=task1b.bin
filenames[3]=task2.txt
filenames[4]=terps-enc-ecb.bmp
filenames[5]=terps-enc-cbc.bmp
filenames[6]=task3.[pdf/txt]
filenames[7]=Task4.[java/py/c]
filenames[8]=password_dictionary.txt
filenames[9]=cracked.txt
filenames[10]=server.pem
filenames[11]=ss71.png
filenames[12]=ss72.png
filenames[13]=task7.txt
filenames[14]=task8.txt

for x in {0..14}
do
  echo ""
  echo "==[Checking file ${filenames[x]}]=="
  if [ $x == 6 ]
      then
      if [ ! -f $studentdir/task3.pdf ] && [ ! -f $studentdir/task3.txt ]
       then
        echo "Missing Task 3 file"
    fi
    elif [ $x == 7 ]
    then
    if [ ! -f $studentdir/Task4.java ] && [ ! -f $studentdir/Task4.c ] && [ ! -f $studentdir/Task4.py ]
       then
        echo "Missing Task 4 file"
    fi
  elif [ ! -f $studentdir/${filenames[x]} ]
    then
    echo "Missing ${filenames[x]}"
  fi
done
