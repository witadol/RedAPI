#! /bin/bash
count=0
while [ $count -lt 1000 ]
do
(( count++ ))
echo $count
./cas.py "/dev/ttyUSB0"
done
