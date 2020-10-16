# Instruções :D

## AG - Representação Real
Para rodar este trabalho será preciso executar o arquivo `runme.sh`, entao talvez seja necessário dar a ele permissões, para isso utilize o comando `chmod +x runme.sh`.Este script deve primeiro gerar todas as entradas ao rodar `entradas.py`, em seguida cada uma das entradas será executada 12 vezes e seus resultados estarão numa pasta instanciaN, onde cada execução está salva em formato `csv`.


Como útlimo passado o scrpit deve executar `plots.py` para gerar os gráficos referentes às execuções realizadas, os gráficos gerados são, por exemplo:

```
Instância1: 
	Taxa de Mutação = 0.01
	Taxa de Cruzamento = 0.6
	Tamanho da População = 25
	Número de Gerações = 25
``` 
### Média e o Desvio Padrão nas Gerações (Execução: 1-6)
![](https://github.com/Niehaus/algoritmos-bioinspirados/blob/master/Barbara-Tutorial2/instancias/instancia1/figures/plot_all_gen_avg0.png)

### Melhores Indivíduos nas Gerações (Execução: 1-6)
![](https://github.com/Niehaus/algoritmos-bioinspirados/blob/master/Barbara-Tutorial2/instancias/instancia1/figures/plot_all_gen_best0.png)

### Melhores Indivíduos nas Gerações - Visualização de todas as 12 execuções
![](https://github.com/Niehaus/algoritmos-bioinspirados/blob/master/Barbara-Tutorial2/instancias/instancia1/figures/plot_cumulative.png)

Enfim, utilize o comando `runme.sh` e veja a mágica acontecer!

## AG - Representação Binária
Tanto o AG - Rep. Real e o de Rep. Binária neste caso possuem a mesma função objetivo, e em ambos a média de fitness nas gerações realiza uma rápida descida e não oscila muito em direção ao fitness médio inicial.

Para os mesmos parâmetros os AGs tiveram o seguite desempenho:

```
Instância:
	Taxa de Mutação = 0.1
	Taxa de Cruzamento = 1.0
	Tamanho da População = 100
	Número de Gerações = 50
```

### Rep. Real
![](https://github.com/Niehaus/algoritmos-bioinspirados/blob/master/Barbara-Tutorial2/instancias/instancia80/figures/plot_all_gen_avg0.png)

### Rep. Binária
![](https://github.com/Niehaus/algoritmos-bioinspirados/blob/master/Barbara-Tutorial2/avg-fitness-tut1.png)
