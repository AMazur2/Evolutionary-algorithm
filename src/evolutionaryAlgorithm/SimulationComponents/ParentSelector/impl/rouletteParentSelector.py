from typing import List
from random import uniform

from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.ParentSelectorInterface \
    import ParentSelectorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual import \
    FloatingPointIndividual


class rouletteParentSelector(ParentSelectorInterface):

    def __init__(self):
        pass

    def getParents(self, population: List[List[IndividualInterface]]) -> List[List[IndividualInterface]]:
        popNum = len(population)
        print(popNum)
        fitness = []
        for el in population:
            fitness.append(el[0].getFitnessFunctionEvaluation())
        max, min, sum = 0, fitness[0], 0
        for i in range(popNum):
            sum += fitness[i]
            if min > fitness[i]:
                min = fitness[i]
            if max < fitness[i]:
                max = fitness[i]

        param = max - min
        fitnessPrim = []
        sum = 0
        for i in range(popNum):         #q' = (q-min(q))*(max(q)-min(q))
            a = fitness[i]-min
            b = a*param                 #q" = 1-q'
            c = (2-b)/2
            if(c < 0):
                c = 0
            fitnessPrim.append(c)
            sum = sum + c

        marriages = []
        for i in range(int(popNum)):
            temp = []
            k = self.chooseOne(fitnessPrim, sum)
            temp.append(FloatingPointIndividual(population[k][0].getRepresentation()))
            temp.append(FloatingPointIndividual(population[k][1].getRepresentation()))
            marriages.append(temp)
        return marriages

    def chooseOne(self, fitness: List[float], maximum: float) -> int:
        pick = uniform(0, maximum)
        current = 0
        for i in range(len(fitness)):
            current += fitness[i]
            if current > pick:
                return i
