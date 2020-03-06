# coding: utf-8
import math
import numpy as np
import random

def func_obj(x):

	n = float(len(x))
	f_exp = -0.2 * math.sqrt(1/n * sum(np.power(x, 2)))

	t = 0
	for i in range(0, len(x)):
		t += np.cos(2 * math.pi * x[i])

	s_exp = 1/n * t
	f = -20 * math.exp(f_exp) - math.exp(s_exp) + 20 + math.exp(1)
    
	return f

#x=[0,2,0,5,0,9]
#print(func_obj(x))



# 1º Definir População 
# -- População Inicial -- Definir Dimensão -> 2D:|------|------| (x1, x2) -> INDIVIDUO <- 
# Vetor auxiliar de Fitness

class Individuo:
	def __init__(self, x1, x2):
		self.x1 = x1
		self.x2 = x2


def GeraIndividuo():
	individuo = []
	for i in range(6):
		escolhe = random.random()
		if escolhe > 0.5:
			individuo.append(1) 
		else:
			individuo.append(0)
	return individuo

individuos = []
valoresReais = []
for i in range(30):
	individuos.append(Individuo(GeraIndividuo(), GeraIndividuo()))


# 2º Função de Representação
# Utilizar uma maneira de representar um individuo como número real
# Indivuo 2D é preciso de duas variaveis a serem ajustadas

def RepresentacaoReal(individuo):
	xmin = -2
	xmax = 2
	n = 6
	tupla = []
	xReal = xmin + ((xmax - xmin)/(2**n -1)) * intBin(individuo.x1, n)
	tupla.append(xReal)
	xReal = xmin + ((xmax - xmin)/(2**n -1)) * intBin(individuo.x2, n)
	tupla.append(xReal)
	print(tupla)

	return 0
def intBin(bin, n):
	valor = 0 
	for i in range(0, n):
		valor += 2**i * bin[i]
	return valor

for individuo in individuos:
#print("X1")
#print(individuo.x1)
#print("X2")
#print(individuo.x2)
	RepresentacaoReal(individuo)