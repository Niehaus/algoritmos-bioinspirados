import math
import random

import numpy as np

xmin = -2
xmax = 2
INDIV_SIZE = 6
dimensao = 2
POP_SIZE = 100
GERACAO = 10


def func_obj(x):

	n = float(len(x))
	f_exp = -0.2 * math.sqrt(1/n * sum(np.power(x, 2)))

	t = 0
	for i in range(0, len(x)):
		t += np.cos(2 * math.pi * x[i])

	s_exp = 1/n * t
	f = -20 * math.exp(f_exp) - math.exp(s_exp) + 20 + math.exp(1)
    
	return f


"""Def do individuo de dimensao x"""
class Individuo:
    def __init__(self, id, geracao, dimensao):
        self.id = id
        self.geracao = geracao
        self.rep_bin = []
        self.fitness = None
        for index in range(dimensao):
            self.rep_bin.append(GeradorIndividuo())

"""Gera individuo random de tamanho n"""
def GeradorIndividuo():
    individuos_tmp = []
    for index in range(INDIV_SIZE):
        escolhe = random.random()
        if escolhe > 0.5:
            individuos_tmp.append(1)
        else: 
            individuos_tmp.append(0)
    return individuos_tmp


"""Funções para gerar representação real do individuo
que sera usada na func_obj gerando o fitness"""
def intBin(bin, n):
	valor = 0 
	for i in range(0, n):
		valor += 2**i * bin[i]
	return valor

def RepresentacaoReal(individuo):
    repReal_list = []
    for each_bin in individuo.rep_bin:
        repReal =  xmin + ((xmax - xmin)/(2**INDIV_SIZE - 1)) * intBin(each_bin, INDIV_SIZE)    
        repReal_list.append(repReal)
    return repReal_list

"""Considerando uma funcção de minimização"""
def Torneio(npop, individuos_list): 
    vpais_index = [None] *  npop
    pv = 0.9 #Chance do pior pai vencer
    i = 0
    while(i < npop):
        p1 = random.randrange(0, npop)
        p2 = random.randrange(0, npop)
        while(p1 == p2):
            p2 = random.randrange(0, npop)
        r = random.randrange(0, 1)
        if individuos_list[p2].fitness > individuos_list[p1].fitness: #p1 é o melhor
            vencedor_index = p1
            if r > pv:
                vencedor_index = p2
        else:#p2 é o melhor
            vencedor_index = p2
            if r > pv:
                vencedor_index = p1
        vpais_index[i] = vencedor_index
        i += 1
    print(vpais_index)
    return vpais_index

def Cruzamento(npop, pm, pais):
    index = 1
    pop_media = []
    while index <= len(pais):
        print("Cruzamento entre:", pais[index - 1], "e ", pais[index])
        index += 2
    return pop_media


individuos_list = []


gen_atual = 0
pm = 1 #probabilidade de mutação

#while gen_atual < GERACAO:
for i in range(POP_SIZE):
    individuos_list.append(Individuo(i, gen_atual, dimensao))

for indv in individuos_list:
    indv.fitness = func_obj(RepresentacaoReal(indv))

pais_vencedores_torneio = Torneio(POP_SIZE, individuos_list)
Cruzamento(POP_SIZE, pm, pais_vencedores_torneio)
#for i in range(num_vencedores):
 #   print(vencedores_torneio[i]," <-> ", vencedores_torneio[(num_vencedores - 1) - i])
     
    
    #gen_atual += 1
#for individuo in individuos_list:
    #print()
    #print ("Id:", individuo.id,"Cod: ",individuo.rep_bin)