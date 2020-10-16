# Instruções :D

Para rodar este trabalho será preciso executar o arquivo `runme.sh`, entao talvez seja necessário dar a ele permissões, para isso utilize o comando `chmod +x runme.sh`.
Feito isso, utilize o comando `./runme.sh` e veja a mágica acontecer!

```
#!/bin/bash

# Barbara - Out 2020

index=1
echo "$(python entradas.py)"
cat arguments.txt | while read line 
do
	n=1 #executa cada entrada 10x
	while [ $n -le 12 ]
	do
		echo "$(python3 tutorial2.py $line $n $index)"
		n=$(( n+1 )) #incrementa n
	done
	index=$(( index+1 )) #incrementa index da instancia
done
echo "$(python3 plots.py)"
```