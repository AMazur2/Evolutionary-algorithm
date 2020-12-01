from typing import List
from random import random

from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.RecombinatorInterface import RecombinatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class averageRecombinator(RecombinatorInterface):

    def __init__ (self, probability: float):
        self.probability = probability

    def subcross(self, marriage, w):
        temp = []
        for i in range(len(marriage[0])):
            temp.append(w*marriage[0][i]+(1-w)*marriage[1][i])
        return temp

    def recombine(self, marriages: List) -> List[IndividualInterface]:
        childrens = []
        for i in range(len(marriages)):
            if random() <= self.probability:
                j = random()
                childrens.append(self.subcross(marriages[i], j))
                k = random()
                childrens.append(self.subcross(marriages[i], k))
            else:
                childrens.append(marriages[i][0])
                childrens.append(marriages[i][1])
        return childrens
