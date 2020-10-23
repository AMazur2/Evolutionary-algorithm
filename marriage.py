import random
import numpy as np

Dim = 5         #Wymiar zmiennej
num = 4         #Wielkość populacji
counter = 10    #Maksymalna ilość populacji

def createPopulation():
    population = np.zeros([num,Dim])    
    for i in range(num):
        for j in range(Dim):
            population[i][j] = random.randrange(10)
    return population  

def marry():
    list = []
    for i in range(num):
        list.append(i)
    l = int(num/2)                              #ilość małżeństw
    marriages = np.zeros([l,2])
    for i in range(l):
        for j in range(2):
            k = random.randrange(len(list))
            marriages[j][i] = list[k]
            list.pop(k)
    return marriages

tab = createPopulation()
print(tab)