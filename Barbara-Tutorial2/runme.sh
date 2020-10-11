#!/bin/bash

# My first script


#echo "$(python entradas.py)"

cat arguments.txt | while read line 
do
	echo "$(python3 tutorial2.py $line)"
done

