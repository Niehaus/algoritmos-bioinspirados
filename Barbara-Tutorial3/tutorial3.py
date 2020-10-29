# -*- coding: utf-8 -*-
# Python with shell script example
# Barbara Boechat
# Outubro 2020


import math
import os
import random
import sys


"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd """
 
def print_argumentos(taxa_mutacao, taxa_cruzamento, npop, ngen, execucao, instancia):
    print("Execução: " + str(execucao), "Instancia: " + str(instancia))
    print("Taxa de Mutação = " + str(taxa_mutacao))
    print("Taxa de Cruzamento = " + str(taxa_cruzamento))
    print("Tamanho da População = " + str(npop))
    print("Número de Gerações = " + str(ngen))
    print("--" * 12)
    print("\n")


def GeradorParametros(pasta):
    os.chdir('datasets')
    os.chdir(pasta)
    profits = []
    pesos = []
    sol_otima = []
    with open("p" + pasta + "_s.txt") as f:
        for line in f:
            sol_otima.append(int(line.replace('\n', '')))
    with open("p" + pasta +"_c.txt") as f:
        for line in f:
            capacidade = int(line)
    with open("p" + pasta +"_p.txt") as f:
        for line in f:
            profits.append(int(line.replace('\n', '').strip()))
    with open("p" + pasta +"_w.txt") as f:
        for line in f:
            pesos.append(int(line.replace('\n', '').strip()))
    tamanho_mochila = len(profits)
    return profits, pesos, capacidade, tamanho_mochila, sol_otima

def Somatorio(pesos, sol):
    peso_mochila = 0
    for k in range(len(sol)):
       if sol[k] == 1:
           peso_mochila += pesos[k]
    return peso_mochila

def func_obj(pesos, pr, c, sol):
    if Somatorio(pesos, sol) <= c:
        return Somatorio(pr, sol)
    else: # Houve excesso de peso
        return Somatorio(pr, sol) * (1 - (Somatorio(pesos, sol) - c) / c)


"""Def da mochila de tamanho x"""
class Mochila:
    def __init__(self, id, geracao):
        self.id = id
        self.geracao = geracao
        self.rep_binaria = []
        self.fitness = 0


"""Gera mochila random de tamanho n, setar igual ao do tutorial1"""
def GeradorMochila(tamanho_mochila):
    mochilas_tmp = []
    for index in range(tamanho_mochila):
        mochilas_tmp.append(random.randint(0, 1))
    return mochilas_tmp


"""Inicializa cada mochila e sua representacao binaria"""
def CriaGeracaoInicial(npop, gen_atual, tamanho_mochila):
    populacao = []
    for i in range(npop):
        populacao.append(Mochila(i, gen_atual))
        populacao[-1].rep_binaria = GeradorMochila(tamanho_mochila)
    return populacao


"""Considerando uma funcção de maximização"""
def Torneio(npop, populacao):
    vpais = []
    pv = 0.9  # Chance do pior pai vencer
    i = 0
    
    if (npop / 2) % 2 != 0: i = -1
    while(i < npop):
        p1 = random.randrange(0, npop)
        p2 = random.randrange(0, npop)
        while(p1 == p2):
            p2 = random.randrange(0, npop)
        r = random.random()
        # print(r)
        if populacao[p2].fitness > populacao[p1].fitness: # p2 é o melhor
            vencedor_index = p2
            if r > pv:
                vencedor_index = p1
        else: # p1 é o melhor
            vencedor_index = p1
            if r > pv:
                vencedor_index = p2
        vpais.append(populacao[vencedor_index])
        i += 1
    return vpais


def OrganizaPares(pais_sorteados):
    mv_indv = Mochila(0, 0)
    for i in range(0, len(pais_sorteados), 2):
        if i == len(pais_sorteados) - 1:
            break
        if pais_sorteados[i].rep_binaria == pais_sorteados[i + 1].rep_binaria:
            # print("sao iguais2")
            prox_pai = i + 2
            for j in range(prox_pai, len(pais_sorteados)):
                if pais_sorteados[i].id != pais_sorteados[j].id:
                    mv_indv = pais_sorteados[j]
                    pais_sorteados[j] = pais_sorteados[i + 1]
                    pais_sorteados[i + 1] = mv_indv
                    break


"""Cruzamento entre dois ultimos bits dos pais"""
def Cruzamento(g, taxa_cruzamento, pais, tam):
    pop_intermediaria = []
    OrganizaPares(pais)
    for k in range(0, len(pais), 2):
        if k + 1 >= len(pais): break
        chance_cruzamento = random.random()
        if chance_cruzamento <= taxa_cruzamento:
            
            # print("pais", pais[k].id, pais[k + 1].id)
            # print(pais[k].id, pais[k].rep_binaria)
            # print(pais[k + 1].id, pais[k + 1].rep_binaria)
            # print("---" * 10)
            # Gera Filho 1
            pop_intermediaria.append(Mochila(k, g))
            filho = pais[k].rep_binaria[:tam - 2] + \
                pais[k + 1].rep_binaria[tam - 2:tam + 1]
            pop_intermediaria[-1].rep_binaria = filho
            # print(pop_intermediaria[-1].id, pop_intermediaria[-1].rep_binaria)
            # Gera Filho 2
            pop_intermediaria.append(Mochila(k + 1, g))
            filho = pais[k + 1].rep_binaria[:tam - 2] + \
                pais[k].rep_binaria[tam - 2:tam + 1]
            pop_intermediaria[-1].rep_binaria = filho
            # print(pop_intermediaria[-1].id, pop_intermediaria[-1].rep_binaria)
            # print('\n')
        else:
            # print("pais")
            # print(pais[k].id, pais[k].rep_binaria)
            # print(pais[k + 1].id, pais[k + 1].rep_binaria)
            # print("---" * 10)
            pop_intermediaria.append(pais[k])
            # print(pop_intermediaria[-1].id, pop_intermediaria[-1].rep_binaria)
            pop_intermediaria.append(pais[k + 1])
            # print(pop_intermediaria[-1].id, pop_intermediaria[-1].rep_binaria)
            # print('\n')
    return pop_intermediaria


"""Mutar a rep_real de uma dimensão sorteada"""
def Mutacao(npop, pop_intermediaria, taxa_mutacao):
    for indv in pop_intermediaria:
        for alelo in range(len(indv.rep_binaria)):
            chance_mutacao = random.random()
            if chance_mutacao <= taxa_mutacao:
                # print("mutou", chance_mutacao)
                if indv.rep_binaria[alelo] == 0:
                    indv.rep_binaria[alelo] = 1
                else:
                    indv.rep_binaria[alelo] = 0


def Elitismo(populacao, pop_intermediaria):
    maior_fitness = -1000000
    maiorf_index = 0

    for index in range(len(populacao)):
        if populacao[index].fitness > maior_fitness:
            maior_fitness = populacao[index].fitness
            maiorf_index = index
    # print("melhor indv", populacao[maiorf_index].fitness)
    indiv_aleatorio = random.randint(0, len(pop_intermediaria) - 1)
    pop_intermediaria[indiv_aleatorio] = populacao[maiorf_index]
    

""" Seta parametros do problema da mochila"""
s = [] # Solução ótima
pr = [] # Profits
pesos = [] # Pesos
c = 0 # Capacidad
tam_mochila = 0
pasta = sys.argv[7]

pr, pesos, c, tam_mochila, s = GeradorParametros(pasta) 


""" Parametros do AG """
taxa_mutacao = float(sys.argv[1])
taxa_cruzamento = float(sys.argv[2])
npop = int(sys.argv[3])
ngen = int(sys.argv[4])
execucao = sys.argv[5]
instancia = sys.argv[6]

print_argumentos(taxa_mutacao, taxa_cruzamento, npop, ngen, execucao, instancia)

g = 0
populacao = CriaGeracaoInicial(npop, 0, tam_mochila)
for indv in populacao:
    indv.fitness = func_obj(pesos, pr, c, indv.rep_binaria)
    # print(indv.geracao, indv.fitness, indv.rep_binaria)

g += 1
while g < ngen:
    pais_select = Torneio(npop, populacao)
    
    pop_intermediaria = Cruzamento(g, taxa_cruzamento, pais_select, tam_mochila)
    # for indv in pais_select:
    #     print(indv.geracao, indv.id, indv.fitness, indv.rep_binaria)
    Mutacao(npop, pop_intermediaria, taxa_mutacao)
    Elitismo(populacao, pop_intermediaria)
    populacao = pop_intermediaria[:]
    for indv in populacao:
        indv.fitness = func_obj(pesos, pr, c, indv.rep_binaria)
    g += 1
#print(populacao[0].rep_binaria, capacidade)
# Somatorio(pesos, populacao[0].rep_binaria)
# for indv in populacao:
# for indv in populacao:
    # print(indv.geracao, indv.id, indv.fitness)
print('Ótimo: ', func_obj(pesos, pr, c, s))

