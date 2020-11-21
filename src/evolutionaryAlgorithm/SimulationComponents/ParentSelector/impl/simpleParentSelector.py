from typing import List
from random import randint

from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.ParentSelectorInterface import ParentSelectorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface

class simpleParentSelector(ParentSelectorInterface):

    def __init__ (self)
    
    def marry(self, Population: List[IndividualInterface]):
        marriages = []
        num = int(len(Population)/2)
        for i in range(num):
            temp = []
            for j in range(2):
                k = randint(0,len(Population))
                temp.append(Population[k])
                del Population[k]
            marriages.append(temp)
        return marriages
        

