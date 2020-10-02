import math
import random

import numpy as np

xmin = -2
xmax = 2
indiv_size = 6
dimensao = 2
npop = 10

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
    def __init__(self, id, geracao):
        self.id = id
        self.geracao = geracao
        self.rep_bin = []
        self.fitness = None

"""Gera individuo random de tamanho n"""
def GeradorIndividuo():
    individuos_tmp = []
    for index in range(indiv_size):
        escolhe = random.random()
        if escolhe > 0.5:
            individuos_tmp.append(1)
        else: 
            individuos_tmp.append(0)
    return individuos_tmp

"""Inicializa cada individuo e sua representacao binaria"""
def CriaGeracaoInicial(npop, gen_atual):
    populacao = []  
    for i in range(npop):
        populacao.append(Individuo(i, gen_atual))
        for index in range(dimensao):
            populacao[-1].rep_bin.append(GeradorIndividuo())
    return populacao

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
        repReal =  xmin + ((xmax - xmin)/(2**indiv_size - 1)) * intBin(each_bin, indiv_size)    
        repReal_list.append(repReal)
    return repReal_list

"""Considerando uma funcção de minimização"""
def Torneio(npop, populacao): 
    vpais_index = [None] *  npop
    pv = 0.9 #Chance do pior pai vencer
    i = 0
    while(i < npop):
        p1 = random.randrange(0, npop)
        p2 = random.randrange(0, npop)
        while(p1 == p2):
            p2 = random.randrange(0, npop)
        r = random.randrange(0, 1)
        if populacao[p2].fitness > populacao[p1].fitness: #p1 é o melhor
            vencedor_index = p1
            if r > pv:
                vencedor_index = p2
        else:#p2 é o melhor
            vencedor_index = p2
            if r > pv:
                vencedor_index = p1
        vpais_index[i] = vencedor_index
        i += 1
    return vpais_index

"""Cruzamento entre dois ultimos bits dos pais"""
def Cruzamento(gen_atual, pc, pais, individuo):
    index = 1
    filhos = []
    pop_intermediaria = []
    while index <= len(pais):
        #print("Cruzamento entre:", pais[index - 1], "e", pais[index])
        """Cruzamento que gera filho1"""
        for i in range(len(individuo[pais[index - 1]].rep_bin)):
            filhos.append(individuo[pais[index - 1]].rep_bin[i][:indiv_size - 2] + individuo[pais[index]].rep_bin[i][indiv_size - 2:indiv_size + 1])  
        #print("filho1:", filhos)
        pop_intermediaria.append(Individuo(index - 1, gen_atual))
        for filho in filhos:
            pop_intermediaria[-1].rep_bin.append(filho)
        
        filhos = []
        """Cruzamento que gera filho1"""
        for i in range(len(individuo[pais[index]].rep_bin)):
            filhos.append(individuo[pais[index]].rep_bin[i][:indiv_size - 2] + individuo[pais[index - 1]].rep_bin[i][indiv_size - 2:indiv_size + 1]) 
        #print("filho2:", filhos)
        pop_intermediaria.append(Individuo(index, gen_atual))
        for filho in filhos:
            pop_intermediaria[-1].rep_bin.append(filho)
        filhos = []
        index += 2
    return pop_intermediaria

def MutaBit(indiv_part, pm):
    #print("*" * 21)
    #print("1:", indiv_part)
    for i in range(len(indiv_part)):    
        chance_mutar = random.random()
        if chance_mutar < pm:
            if indiv_part[i] == 0:
                indiv_part[i] = 1
            else:  
                indiv_part[i] = 0   
    #print("2:", indiv_part)

def Mutacao(npop, pop_intermediaria, pm):
    for indiv in pop_intermediaria:
        for rep_bin in indiv.rep_bin:
                MutaBit(rep_bin, pm)
                
def Elitismo(nelite):
    """
    docstring
    """
    pass


def ImprimePop(populacao):
    for indiv in populacao:
        print("Id:", indiv.id, "-> ", indiv.rep_bin)
          

gen_atual = 0
pc = 1 #probabilidade de mutação
pm = 0.1
nelite = 0
geracao = 10


g = 0
populacao = CriaGeracaoInicial(npop, g)

while g <= geracao:
    for indv in populacao:
        indv.fitness = func_obj(RepresentacaoReal(indv))
    pais_vencedores_torneio = Torneio(npop, populacao)
    pop_intermediaria = Cruzamento(g + 1, pc, pais_vencedores_torneio, populacao)
    #for each in pop_intermediaria:
    #   print(each.id, each.geracao, "-> ", each.rep_bin, "\n")
    Mutacao(npop, pop_intermediaria, pm)
    Elitismo(nelite)
    populacao = pop_intermediaria
    g += 1

ImprimePop(populacao)