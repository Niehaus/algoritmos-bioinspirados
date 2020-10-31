#!/bin/bash

# Barbara - Out 2020

index=1
PASTAS=('01' '02' '03' '04' '05' '06' '07' '08')
#PASTAS=('01' '02' '08')
echo "$(python3 entradas.py)"
for ((cont=0; cont<${#PASTAS[@]}; cont++)); do
	cat arguments.txt | while read line
	do
		n=1 #executa cada entrada 12x
		while [ $n -le 12 ]
		do
			echo "$(python3 tutorial3.py $line $n $index ${PASTAS[$cont]})"
			# echo ${PASTAS[$cont]}
			# echo $line
			n=$(( n+1 )) #incrementa n
		done
		index=$(( index+1 )) #incrementa index da instancia
	done
done
# echo "$(python3 plots.py)"