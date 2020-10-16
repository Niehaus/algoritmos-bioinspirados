# -*- coding: utf-8 -*-
# Python with shell script example
# Barbara Boechat
# Outubro 2020

import math
import os
import random
import sys

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def print_argumentos(taxa_mutacao, taxa_cruzamento, npop, ngen, execucao, instancia):
    print("Execução: " + str(execucao), "Instancia: " + str(instancia))
    print("Taxa de Mutação = " + str(taxa_mutacao))
    print("Taxa de Cruzamento = " + str(taxa_cruzamento))
    print("Tamanho da População = " + str(npop))
    print("Número de Gerações = " + str(ngen))
    print("--" * 12)
    print("\n")

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
        self.rep_real = []
        self.fitness = 0


"""Gera individuo random de tamanho n, setar igual ao do tutorial1"""
def GeradorIndividuo():
    individuos_tmp = []
    for index in range(dimensao):
        individuos_tmp.append(random.uniform(-2, 2))
    #print(individuos_tmp)
    return individuos_tmp

"""Inicializa cada individuo e sua representacao binaria"""
def CriaGeracaoInicial(npop, gen_atual):
    populacao = []  
    for i in range(npop):
        populacao.append(Individuo(i, gen_atual))
        populacao[-1].rep_real = GeradorIndividuo()
    return populacao


"""Cria roleta a partir dos fitness invertidos, pois
trata-se de uma função de minimização, normalizar pelo rank"""
def CriaRoleta(populacao, roleta, fitness_total):
    fit = []
    for indv in populacao:
        if indv.fitness > 0:
            fit.append(1 / indv.fitness)
        elif indv.fitness == 0:
            fit.append(1)
        fitness_total += fit[-1] 

    for i in range(len(fit)):
        roleta.append(fit[i]/ fitness_total)

"""Considerando uma função de minimização, método de seleção
de pais escolhido:"""
def Roleta(npop, populacao):
    fitness_total = 0
    roleta = []
    limite_sorteado = 0
    acumulador_roleta = 0
    num_pais_sorteados = 0
    lista_pais_sorteados = []
    CriaRoleta(populacao, roleta, fitness_total)
    while num_pais_sorteados < round(npop):
        limite_sorteado = random.random()
        #print("valor premiado:", limite_sorteado )
        for index in range(len(roleta)):
            acumulador_roleta += roleta[index]
            if acumulador_roleta >= limite_sorteado:
                #print("pai sorteado", index)
                acumulador_roleta = 0
                num_pais_sorteados += 1
                lista_pais_sorteados.append(populacao[index])
                break
    return lista_pais_sorteados

def OrganizaPares(pais_sorteados):
    mv_indv = Individuo(0, 0)
    for i in range(0, len(pais_sorteados), 2):
        if i == len(pais_sorteados) - 1: break
        if pais_sorteados[i].id == pais_sorteados[i + 1].id:
            prox_pai = i + 2
            for j in range(prox_pai, len(pais_sorteados)):
                if pais_sorteados[i].id != pais_sorteados[j].id: 
                    mv_indv = pais_sorteados[j]
                    pais_sorteados[j] = pais_sorteados[i + 1]
                    pais_sorteados[i + 1] = mv_indv  
                    break
            
        # print("pai1: ", pais_sorteados[i].id, "pai2:", pais_sorteados[i + 1].id)


"""Cruzamento utilizando blend-alphaBeta """
def Cruzamento(pais_sorteados, taxa_cruzamento, gen_atual, alpha, beta):
    pop_intermediaria = []
    d = []
    rep_real_aleatoria_x = []
    rep_real_aleatoria_y = []
    OrganizaPares(pais_sorteados)
    for i in range(0, len(pais_sorteados), 2):
        if i == len(pais_sorteados) - 1: break
        # print("X:", pais_sorteados[i].id, "-", "Y:", pais_sorteados[i + 1].id)  
        chance_cruzamento = random.random()
        if chance_cruzamento <= taxa_cruzamento: #Houve cruzamento  
            for dim in range(dimensao): 
                X = pais_sorteados[i].rep_real[dim]
                Y = pais_sorteados[i + 1].rep_real[dim]
                d.append(abs(X - Y))
                if X <= Y:
                    rep_real_aleatoria_x.append(random.uniform(X - alpha * d[dim], Y + beta * d[dim]))
                    rep_real_aleatoria_y.append(random.uniform(X - alpha * d[dim], Y + beta * d[dim]))
                else:
                    rep_real_aleatoria_x.append(random.uniform(Y - beta * d[dim], X + alpha * d[dim]))
                    rep_real_aleatoria_y.append(random.uniform(Y - beta * d[dim], X + alpha * d[dim]))
            #Cria filho X'
            pop_intermediaria.append(Individuo(i, gen_atual))
            pop_intermediaria[-1].rep_real = rep_real_aleatoria_x
        
            #Cria filho Y'
            pop_intermediaria.append(Individuo(i + 1, gen_atual))
            pop_intermediaria[-1].rep_real = rep_real_aleatoria_y
            d = []
            rep_real_aleatoria_x = []
            rep_real_aleatoria_y = []
        else: #Não houve cruzamento
            pop_intermediaria.append(pais_sorteados[i]) 
            pop_intermediaria.append(pais_sorteados[i + 1])
    
    return pop_intermediaria

"""Mutar a rep_real de uma dimensão sorteada"""
def Mutacao(npop, pop_intermediaria, taxa_mutacao):
    for indv in pop_intermediaria:
        chance_mutacao = random.random() 
        if chance_mutacao <= taxa_mutacao: #Se vai haver mutação ou não
            index_mutacao = random.randint(0, dimensao - 1)
            indv.rep_real[index_mutacao] = random.random() 

def Elitismo(populacao, pop_intermediaria):
    menor_fitness = 1000
    menorf_index = 0
    for index in range(len(populacao)):
        if populacao[index].fitness < menor_fitness:
            menor_fitness = populacao[index].fitness
            menorf_index = index
    # print("melhor indv", populacao[menorf_index].fitness)
    indiv_aleatorio = random.randint(0, len(pop_intermediaria) - 1)
    pop_intermediaria[indiv_aleatorio] = populacao[menorf_index]



def WriteFiles(instancia, execucao, df):
    folder_name = "instancia" + instancia        
    if not os.path.exists(folder_name): #criapasta para resultados da instancia
        os.makedirs(folder_name)
        os.chdir(folder_name)
    else: #pasta já existe, entra nela
        os.chdir(folder_name)
    f = open("readme.txt", "+w")
    f.write("Taxa de Mutação = " + str(taxa_mutacao) +"\nTaxa de Cruzamento = " + str(taxa_cruzamento)+
    "\nTamanho da População = " + str(npop)+ "\nNúmero de Gerações = " + str(ngen))
    path = ""
    df.to_csv (os.path.join(path,r'execucao' + execucao +'.csv'), index = False, header=True)

def GenerateDataframe(avg_fitness, melhor_da_geracao):
    avg_fitness_calculate = []
    std_fitness_calculate = []
    gen_array = []
    for i in range(len(avg_fitness)):
        std_fitness_calculate.append(np.std(avg_fitness[i]))
        avg_fitness_calculate.append(np.mean(avg_fitness[i]))
        gen_array.append(i)
    df = pd.DataFrame(list(zip(gen_array,avg_fitness_calculate, std_fitness_calculate, melhor_da_geracao)), 
               columns =['gen','avg_fitness', 'std_fitness', 'best_of_gen']) 
    WriteFiles(instancia, execucao, df)
    # print(df)

def ImprimePop(populacao):
    for indiv in populacao:
        print("Id:", indiv.id, "Gen:", indiv.geracao, "-> ", indiv.fitness)




taxa_mutacao = float(sys.argv[1])
taxa_cruzamento = float(sys.argv[2])
npop = int(sys.argv[3])
ngen = int(sys.argv[4])
execucao = sys.argv[5]
instancia = sys.argv[6]
dimensao = 2
gen_atual = 0
alpha = 0.75
beta = 0.25


#variaveis p/ os plots
avg_fitness = []
gen_fitness = []
melhor_da_geracao = []

print_argumentos(taxa_mutacao, taxa_cruzamento, npop, ngen, execucao, instancia)
populacao = CriaGeracaoInicial(npop, gen_atual)
for indv in populacao:
    indv.fitness = func_obj(indv.rep_real)
    gen_fitness.append(indv.fitness)
melhor_da_geracao.append(max(gen_fitness)) 
avg_fitness.append(gen_fitness)
gen_fitness = []

gen_atual += 1
while gen_atual < ngen:
    pais_sorteados_roleta = Roleta(npop, populacao)
    pop_intermediaria = Cruzamento(pais_sorteados_roleta, taxa_cruzamento, gen_atual, alpha, beta)
    Mutacao(npop, pop_intermediaria, taxa_mutacao)
    Elitismo(populacao, pop_intermediaria)
    populacao = pop_intermediaria[:]
    for indv in populacao:
        indv.fitness = func_obj(indv.rep_real)
        gen_fitness.append(indv.fitness)
    melhor_da_geracao.append(max(gen_fitness))
    avg_fitness.append(gen_fitness)
    gen_fitness = []
    gen_atual += 1


GenerateDataframe(avg_fitness, melhor_da_geracao)
# PlotGenGraph(avg_fitness, instancia, execucao)
# ImprimePop(populacao)






