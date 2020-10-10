# -*- coding: utf-8 -*-
# Python3 code to demonstrate  
# to compute all possible permutations 
# using list comprehension  

#create file
file_obj  = open("arguments.txt", "w+")
  
# initializing lists 
taxa_mutacao = [0.01, 0.05, 0.1] 
taxa_cruzamento = [0.6, 0.8, 1] 
npop = [25, 50, 100]
ngen = [25, 50, 100]
  
# printing lists  
print ("A lista de parametros são: " + str(taxa_mutacao) +
                               " " + str(taxa_cruzamento) + 
                               " " + str(npop) +
                               " " + str(ngen)) 
  
# using list comprehension  
# to compute all possible permutations 
res = [[i, j, k, l] for i in taxa_mutacao  
                 for j in taxa_cruzamento 
                 for k in npop
                 for l in ngen] 

  
# printing result 
#print ("All possible permutations are : " +  str(res)) 
string_form = ""
for combination in res:
    for argument in combination:
        string_form += " " + str(argument)
    string_form += "\n"

print("Todas as combinações foram escritas com sucesso!")
file_obj.write(string_form)
