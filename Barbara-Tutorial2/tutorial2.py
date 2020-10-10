# -*- coding: utf-8 -*-
# Python shell script example
# Barbara Boechat
# Outubro 2020

import sys

taxa_mutacao = sys.argv[1]
taxa_cruzamento = sys.argv[2]
npop = sys.argv[3]
ngen = sys.argv[4]


print("Taxa de Mutação = " + taxa_mutacao)
print("Taxa de Cruzamento = " + taxa_cruzamento)
print("Tamanho da População = " + npop)
print("Número de Gerações = " + ngen)
print("--" * 10)
print("\n")