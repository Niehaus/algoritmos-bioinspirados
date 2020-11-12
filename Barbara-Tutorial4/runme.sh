#!/bin/bash

# Barbara - Nov 2020

cat arguments | while read line; do
  n=1 #executa cada entrada 12x
  while [ $n -le 12 ]; do
    echo "$(python3 main.py $line)"
    n=$((n + 1)) #incrementa n
  done
done
