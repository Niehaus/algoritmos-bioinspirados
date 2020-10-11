import math
import random

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

xmin = -2
xmax = 2
indiv_size = 6
dimensao = 2
npop = 100

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
        self.fitness = 0

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
        # print("Cruzamento entre:", pais[index - 1], individuo[pais[index - 1]].rep_bin,"e", pais[index], individuo[pais[index]].rep_bin)
        """Cruzamento que gera filho1"""
        for i in range(len(individuo[pais[index - 1]].rep_bin)):
            filhos.append(individuo[pais[index - 1]].rep_bin[i][:indiv_size - 2] + individuo[pais[index]].rep_bin[i][indiv_size - 2:indiv_size + 1])  
        # print("filho1:", filhos)
        pop_intermediaria.append(Individuo(index - 1, gen_atual))
        for filho in filhos:
            pop_intermediaria[-1].rep_bin.append(filho)
        
        filhos = []
        """Cruzamento que gera filho1"""
        for i in range(len(individuo[pais[index]].rep_bin)):
            filhos.append(individuo[pais[index]].rep_bin[i][:indiv_size - 2] + individuo[pais[index - 1]].rep_bin[i][indiv_size - 2:indiv_size + 1]) 
        # print("filho2:", filhos)
        pop_intermediaria.append(Individuo(index, gen_atual))
        for filho in filhos:
            pop_intermediaria[-1].rep_bin.append(filho)
        filhos = []
        index += 2
    return pop_intermediaria

"""Cada bit do individuo tem 
uma probabilidade de mudar"""
def MutaBit(indiv_part, pm):
    for i in range(len(indiv_part)):    
        chance_mutar = random.randrange(0,1)
        if chance_mutar < pm:
            if indiv_part[i] == 0:
                indiv_part[i] = 1
            else:  
                indiv_part[i] = 0   
    #print("*" * 21)
    #print("1:", indiv_part)
    #print("2:", indiv_part)

def Mutacao(npop, pop_intermediaria, pm):
    for indiv in pop_intermediaria:
        for rep_bin in indiv.rep_bin:
                MutaBit(rep_bin, pm)


"""
pegar na população o de menor fitness, e substituir por aleatoriamente 
por alguém na população intermediaria tanto cromossomo quanto fitness  
e printar esse cara a cada geração
"""
def Elitismo(nelite, populacao, pop_intermed):
    menor_fitness = 1000
    menorf_index = 0
    for index in range(len(populacao)):
        if populacao[index].fitness < menor_fitness:
            menor_fitness = populacao[index].fitness
            menorf_index = index
    indiv_aleatorio = random.randrange(0, len(populacao) -1)
    pop_intermediaria[indiv_aleatorio].rep_bin = populacao[menorf_index].rep_bin

def ImprimePop(populacao):
    #cod = []
    for indiv in populacao:
        #for bins in indiv.rep_bin:
            #cod += bins
        print("Id:", indiv.id, "-> ", indiv.fitness)
        #cod = []

def PlotGenGraph(avg_fitness):
    array_plot  = []
    gen_array = []
    for i in range(len(avg_fitness)):
        array_plot.append(np.mean(avg_fitness[i])) 
        gen_array.append(i)
    
    fig, ax = plt.subplots()
    ax.plot(gen_array, array_plot)

    ax.set(xlabel='Generation', ylabel='Avarege Fitness',
    title='Avarege Fitness over generation')
    ax.grid()

    fig.savefig("test.png")
    plt.show()   
        


gen_atual = 0
pc = 1 #probabilidade de cruzamento
pm = 0.1
nelite = 1
geracao = 100
avg_fitness = []
gen_fitness = []

g = 0
populacao = CriaGeracaoInicial(npop, g)
for indv in populacao:
        indv.fitness = func_obj(RepresentacaoReal(indv))


while g <= geracao:
    pais_vencedores_torneio = Torneio(npop, populacao)
    pop_intermediaria = Cruzamento(g + 1, pc, pais_vencedores_torneio, populacao)
    Mutacao(npop, pop_intermediaria, pm)
    Elitismo(nelite, populacao, pop_intermediaria)
    populacao = pop_intermediaria[:]
    for indv in populacao:
        indv.fitness = func_obj(RepresentacaoReal(indv))
        gen_fitness.append(indv.fitness)
    avg_fitness.append(gen_fitness)
    gen_fitness = []
    g += 1

#ImprimePop(populacao)
PlotGenGraph(avg_fitness)
