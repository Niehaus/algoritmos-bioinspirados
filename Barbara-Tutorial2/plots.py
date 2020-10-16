import math
import os
import random
import sys

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


list_dir = os.listdir() #pega todos os arquivos na pasta
root_folder = os.getcwd()
title = ['1-6', '6-12']

def PlotCumulative(dfs):
    fig, ax = plt.subplots()
    for df in dfs:
        # png_label = file.split('.csv')
        x= df['gen']
        y= df['best_of_gen']
        ax.plot(x,y)
    ax.set(xlabel='Geração', ylabel='Best Fitness na Geração',
    title='Best Fitness nas Gerações')
    ax.grid()
    fig.savefig("plot_cumulative.png")    
    plt.close()
        
def PlotStacked(dfs):
    df_index = 0
    count = 1
    for index in range(2):
        fig, axs = plt.subplots(3, 2)
        fig.suptitle('Best Fitness nas Gerações: Execução ' +  title[index])
        for i in range(3):
            for j in range(2):
                if df_index >= len(dfs): break
                x = dfs[df_index]['gen']
                y = dfs[df_index]['best_of_gen']
        
                axs[i, j].plot(x, y)
                df_index += 1
        
        for ax in axs.flat:
            ax.set(xlabel='Geração', ylabel='Best Fitness')
            ax.legend(['Exec: ' + str(count)])
            ax.grid()
            count+=1
        # Hide x labels and tick labels for top plots and y ticks for right plots.
        for ax in axs.flat:
            ax.label_outer()

        plt.savefig("plot_all_gen_best"+str(index)+".png")    
    plt.close()

def PlotStackedAVG(dfs):
    df_index = 0
    for index in range(2):
        fig, axs = plt.subplots(3, 2)
        fig.suptitle('Média de Fitness e Desvio Padrão por Geração: Execução ' +  title[index])
        for i in range(3):
            for j in range(2):
                if df_index >= len(dfs): break
                x = dfs[df_index]['gen']
                
                y = dfs[df_index]['avg_fitness']
                axs[i, j].plot(x, y, label='media', color='blue') #plot avg

                y = dfs[df_index]['std_fitness']
                axs[i, j].plot(x, y, linestyle='dotted', label='desvio', color='red')#plot desvio padrão
                df_index += 1

        for ax in axs.flat:
            ax.set(xlabel='Geração', ylabel='Fitness')
            ax.legend(['Média', 'Desvio. P'])
            ax.grid()
        # # Hide x labels and tick labels for top plots and y ticks for right plots.
        for ax in axs.flat:
            ax.label_outer()
        plt.savefig("plot_all_gen_avg"+str(index)+".png")    
    plt.close()

def GetPlotDone():
    count = 0
    dfs = []
    for folder in list_dir:
        if 'instancia' in folder: #seleciona apenas as pastas das instancias
            os.chdir(folder)
            for file in os.listdir():
                if 'execucao' in file: 
                    #print(file)
                    try: 
                        df = pd.read_csv(file)
                        dfs.append(df)
                    except: 
                        print ("Dataframe error to load from csv\nPlease check if csv file really exists.\nCheck into path: "+ os.getcwd())   
                    count += 1
            if not os.path.exists('figures'): #criapasta para resultados da instancia
                os.makedirs('figures')
                os.chdir('figures')
            else: #pasta já existe, entra nela
                os.chdir('figures')
            PlotCumulative(dfs)
            PlotStacked(dfs)
            PlotStackedAVG(dfs)
            dfs = []
            count = 0
            print("Plot Done!")
        os.chdir(root_folder)


GetPlotDone()
plt.close('all')

