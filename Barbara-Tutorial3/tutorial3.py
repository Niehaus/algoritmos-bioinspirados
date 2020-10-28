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
    return profits, pesos, capacidade, tamanho_mochila


def func_obj(x):
    pass

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


""" Seta parametros do problema da mochila"""
profits = []
pesos = []
capacidade = 0
tamanho_mochila = 0
pasta = '01' # Pasta dos parametros

profits, pesos, capacidade, tamanho_mochila = GeradorParametros(pasta)
print(tamanho_mochila)

""" Parametros do AG 
taxa_mutacao = float(sys.argv[1])
taxa_cruzamento = float(sys.argv[2])
npop = int(sys.argv[3])
ngen = int(sys.argv[4])
execucao = sys.argv[5]
instancia = sys.argv[6] """
