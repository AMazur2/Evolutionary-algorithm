from typing import List
from random import random

from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.RecombinatorInterface import RecombinatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface

class averageRecombinator(RecombinatorInterface):

    def __init__ (self)

    def subcross(self, marriage, w):
        temp = []
        for i in range(len(marriage[0])):
            temp.append(w*os1[0][i]+(1-w)*os2[1][i])
        return temp

    def recombine(self, Marriages: List):
        childrens = []
        for i in range(len(Marriages):)
            j = random()
            childrens.append(subcross(Marriages[i], j))
            k = random()
            childrens.append(subcross(Marriages[i], k))
        return childrens
    
