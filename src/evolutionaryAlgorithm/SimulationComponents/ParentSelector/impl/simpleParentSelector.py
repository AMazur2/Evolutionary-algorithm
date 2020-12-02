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
        num = int(len(population)/2)
        for i in range(num):
            temp = []
            for j in range(2):
                k = randint(0, len(population)-1)
                temp.append(population[k])
            marriages.append(temp)
        return marriages
