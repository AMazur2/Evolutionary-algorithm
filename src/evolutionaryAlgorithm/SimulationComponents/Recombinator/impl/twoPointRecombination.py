from typing import List
from random import randint

from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.RecombinatorInterface import RecombinatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface

class twoPointRecombinator(RecombinatorInterface):

    def __init__ (self)

    def recombine(self, Marriages: List):
        i = len(Marriages[0][0])
        k = randint(0, i)
        childrens = []
        for el in Marraiges:
            temp1, temp2 = [], []
            for j in range(i):
                if j < k or j >= l:
                    temp1.append(el[0][j])
                    temp2.append(el[1][j])
                else:
                    temp1.append(el[1][j])
                    temp2.append(el[0][j])
            childrens.append(temp1)
            childrens.append(temp2)
        return childrens