from typing import List
from random import randint

from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.ParentSelectorInterface \
    import ParentSelectorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class simpleParentSelector(ParentSelectorInterface):

    def __init__(self):
        pass

    def getParents(self, population: List[IndividualInterface]) -> List[List[IndividualInterface]]:
        marriages = []
        temporaryPopulation = []
        for i in range(len(population)):
            temporaryPopulation.append(population[i])

        num = int(len(temporaryPopulation) / 2)
        for i in range(num):
            temp = []
            for j in range(2):
                k = randint(0, len(temporaryPopulation) - 1)
                temp.append(temporaryPopulation[k])
                del (temporaryPopulation[k])
            marriages.append(temp)
        return marriages
