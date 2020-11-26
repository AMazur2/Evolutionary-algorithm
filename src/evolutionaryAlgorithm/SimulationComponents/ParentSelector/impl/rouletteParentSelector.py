from typing import List
from random import uniform

from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.ParentSelectorInterface \
    import ParentSelectorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class rouletteParentSelector(ParentSelectorInterface):

    def __init__(self):
        pass

    def marry(self, Population: List[IndividualInterface], fitness: List[float]):
        popNum = len(Population)
        max = 0
        for i in range(popNum):
            max += fitness[i]
        marriages = []
        for i in range(int(popNum/2)):
            parents = []
            for j in range(2):
                k = self.chooseOne(fitness, max)
                parents.append(Population[k])
            marriages.append(parents)
        return marriages

    def chooseOne(self, fitness: List[float], maximum: float):
        pick = uniform(0, maximum)
        current = 0
        for i in range(len(fitness)):
            current += fitness[i]
            if current > pick:
                return i
