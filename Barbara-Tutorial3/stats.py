import os
import sys
import pandas as pd
import numpy as np  

def OrganizaPasta(avg_fitness, best, pasta, instancia, execucao):
    folder_name = 'resultados' + pasta
    folder_instancia = 'instancia' + instancia
    if not os.path.exists(folder_name): #cria pasta para resultados da instancia
        os.makedirs(folder_name)
        os.chdir(folder_name)
        os.makedirs(folder_instancia)
        os.chdir(folder_instancia)
    else: #pasta já existe, entra nela
        os.chdir(folder_name)
        if not os.path.exists(folder_instancia):
            os.makedirs(folder_instancia)
            os.chdir(folder_instancia)
        else:
            os.chdir(folder_instancia)        
    EscreveSolucao(GenerateDataframe(avg_fitness, best), execucao)

def GenerateDataframe(avg_fitness, best):
    avg_fitness_calculate = []
    std_fitness_calculate = []
    gen_array = []
    for i in range(len(avg_fitness)):
        std_fitness_calculate.append(np.std(avg_fitness[i]))
        avg_fitness_calculate.append(np.mean(avg_fitness[i]))
        gen_array.append(i)
    df = pd.DataFrame(list(zip(gen_array, avg_fitness_calculate, std_fitness_calculate, best)),
                      columns=['gen', 'avg_fitness', 'std_fitness', 'best_of_gen'])
    return df

def EscreveSolucao(df, execucao):
    # f = open("readme.txt", "+w")
    # f.write("Taxa de Mutação = " + str(taxa_mutacao) + "\nTaxa de Cruzamento = " + str(taxa_cruzamento) +
    #         "\nTamanho da População = " + str(npop) + "\nNúmero de Gerações = " + str(ngen))
    path = ""
    df.to_csv(os.path.join(path, r'execucao' + execucao + '.csv'),
              index=False, header=True)
