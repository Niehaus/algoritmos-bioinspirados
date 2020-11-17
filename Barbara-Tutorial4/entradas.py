# -*- coding: utf-8 -*-
# Python3 code to demonstrate  
# to compute all possible permutations 
# using list comprehension  

# create file
file_obj = open("arguments.txt", "w+")

# initializing lists 
taxa_mutacao = [50, 75, 85, 95, 100]
taxa_cruzamento = [0.05, 0.1, 0.5, 0.75, 0.95]
arquivos = ['kn57_dist.txt', 'lau15_dist.txt', 'sgb128_dist.txt', 'wg22_dist.txt', 'wg59_dist.txt']

# pasta = ['01', '02', '03', '04', '05', '06', '07', '08']
# printing lists  
print("A lista de parametros são: " + str(taxa_mutacao) +
      " " + str(taxa_cruzamento))
# using list comprehension  
# to compute all possible permutations 
res = [[i, j, k] for i in taxa_mutacao
       for j in taxa_cruzamento
       for k in arquivos]

# printing result 
# print ("All possible permutations are : " +  str(res))
string_form = ""
for combination in res:
    for argument in combination:
        string_form += " " + str(argument)
    string_form += "\n"

print("Todas as combinações foram escritas com sucesso!")
file_obj.write(string_form)
