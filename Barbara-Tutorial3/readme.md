# Instruções :D
Para rodar este trabalho será preciso executar o arquivo `runme.sh`, entao talvez seja necessário dar a ele permissões, para isso utilize o comando `chmod +x runme.sh`.
Este script deve primeiro gerar todas as entradas ao rodar `entradas.py`, em seguida cada uma das entradas será executada 12 vezes e seus resultados 
estarão numa pasta instanciaN, onde cada execução está salva em formato `csv`.

## AG - Problema da Mochila Binária  

Neste trabalho foram utilizados 08 problemas diferentes, cada um com capacidade, pesos, profits e tamanho da mochila diferentes, e foram realizadas
12 execuções para cada uma das 81 instâncias geradas, nas quais os parâmetros do AG variam em cada uma. Como por exmeplo: 

```
Instância1: 
	Taxa de Mutação = 0.01
	Taxa de Cruzamento = 0.6
	Tamanho da População = 25
	Número de Gerações = 25
``` 

## Plots

Para melhor vizualização as tabelas mostram apenas até a instância 14. 

### Problema 01 
![](https://github.com/Niehaus/algoritmos-bioinspirados/blob/master/Barbara-Tutorial3/datasets/01/resultados01/plot_media_table.png?raw=true)
 
Mas também é possível visualizar qual a melhor instância e o desempenho do algoritmo para este problema levando em consideração 
os resultados de forma mais geral.
 
![](https://github.com/Niehaus/algoritmos-bioinspirados/blob/master/Barbara-Tutorial3/datasets/01/resultados01/plot_best_inst.png)
