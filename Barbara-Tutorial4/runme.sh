#!/bin/bash

# Barbara - Nov 2020

cat arguments.txt | while read line; do
    echo "$(python3 main.py $line)"
done
