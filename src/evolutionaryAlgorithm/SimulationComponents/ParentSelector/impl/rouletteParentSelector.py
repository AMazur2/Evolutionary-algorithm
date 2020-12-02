from typing import List
from random import uniform

from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.ParentSelectorInterface \
    import ParentSelectorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class rouletteParentSelector(ParentSelectorInterface):

    def __init__(self):
        pass

    def getParents(self, population: List[IndividualInterface]) -> List[List[IndividualInterface]]:
        popNum = len(population)
        fitness = []
        for el in population:
            fitness.append(el.getFitnessFunctionEvaluation())
        max, min, sum = 0, fitness[0], 0
        for i in range(popNum):
            sum += fitness[i]
            if min > fitness[i]:
                min = fitness[i]
            if max < fitness[i]:
                max = fitness[i]

        param = max - min
        fitnessPrim = []
        for i in range(popNum):         #q' = (q-min(q))*(max(q)-min(q))
            a = fitness[i]-min
            b = a*param                 #q" = 1-q'
            c = (2-b)/2
            if(c < 0):
                c = 0
            fitnessPrim.append(c)

        marriages = []
        for i in range(int(popNum/2)):
            parents = []
            for j in range(2):
                temp = self.chooseOne(population, fitnessPrim, sum)
                parents.append(temp)
            marriages.append(parents)
        return marriages

    def chooseOne(self, population: List[IndividualInterface], fitness: List[float], maximum: float) -> \
            IndividualInterface:
        pick = uniform(0, maximum)
        current = 0
        i = 0
        for individual in population:
            current += fitness[i]
            if current > pick:
                return individual
            i = i+1

