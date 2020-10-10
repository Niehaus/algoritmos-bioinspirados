#!/bin/bash

# My first script

cat arguments.txt | while read line 
do
	echo "$(python tutorial2.py $line)"
done

