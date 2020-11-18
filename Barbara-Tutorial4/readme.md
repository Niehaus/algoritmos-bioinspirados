
# Instruções :D
Para rodar este trabalho será preciso executar o arquivo `runme.sh`, então
talvez seja necessário dar a ele permissões, para isso utilize o comando `chmod
+x runme.sh`. Este script deve primeiro gerar todas as entradas ao rodar
`entradas.py`, ao fim cada execução estará salva em formato `csv`.

Para rodar `results_analytics.py` primeiro utilize `pip3 install pyfiglet`, depois
rode o script. 


# Ant System

Neste trabalho foi escolhido o Ant System para resolver o problema do caixeiro
viajante, com os parâmetros alpha = 1 e beta = 5. 

Cada entrada para este problema variou o número de iterações e a taxa de
evaporação. As melhores FOs encontradas foram selecionadas e dispostas na
tabela abaixo. Não houve como fazer uma comparação direta entre o desempenho do
algoritmo e a solução ótima, pois nos arquivos de entrada não havia indicação
da FO ótima e nem da solução. 

| Instância | Melhor FO Encontrada | Média    | Desvio. P     |  Iterações   |Taxa de Evaporação
|-----------|----------------------|----------|---------------|--------------|-------------------
| lau15     | 291                  | 291      | 0             |     *        |       *               
| wg22      | 781                  | 792. 6   | 9.59          |     50       |      0.5
| kn57      | 13150                | 13273.36 | 64.56         |     75       |      0.75
| wg59      | 1029                 | 1067.36  | 12.49         |     85       |      0.75
| sgb128    | 21771                | 22429.88 | 315.83        |     75       |      0.95


Para a entrada lau15 todas as execuções encontraram a FO 291, que por acaso era
o único arquivo que continha a solução ótima, a qual é exatamente 291. 
