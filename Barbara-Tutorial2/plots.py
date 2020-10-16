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

for folder in list_dir:
    if 'instancia' in folder: #seleciona apenas as pastas das instancias
        os.chdir(folder)
        for file in os.listdir():
            count = 0
            if 'execucao' in file: 
                print(file)
                try: 
                    df = pd.read_csv(file)
                except: 
                    print ("Dataframe error to load from csv\nPlease check if csv file really exists.\nCheck into path: "+ os.getcwd())   
                ax = plt.gca()
                png_label = file.split('.csv')
                df.reset_index().plot(kind='line', x='index', y='avg_fitness', label= png_label[0], ax=ax)
                #df.reset_index().plot(kind='line',x='index',y='best_of_gen', ax=ax)
                ax.set(xlabel='Generation', ylabel='Best Fitness in Gen',
                title='Best Fitness Over Generations')
                plt.savefig("plot_all_gen" +str(count)+ ".png")
                df.iloc[0:0]
            count += 1
        print("Plot Done!")
            # plt.show()
            # print(os.listdir())
    os.chdir(root_folder)