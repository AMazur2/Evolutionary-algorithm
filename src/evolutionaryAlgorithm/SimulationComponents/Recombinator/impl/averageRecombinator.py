from typing import List
from random import random

from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.RecombinatorInterface import RecombinatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class averageRecombinator(RecombinatorInterface):

    def __init__ (self, probability: float):
        self.probability = probability

    def subcross(self, marriage: List[IndividualInterface], w: float):
        temp = []
        t1 = marriage[0].getRepresentation()
        t2 = marriage[1].getRepresentation()
        for i in range(len(t1)):
            temp.append(w*t1[i]+(1-w)*t2[i])
        return temp

    def recombine(self, marriages: List[List[IndividualInterface]]) -> List[IndividualInterface]:
        childrens = []
        for marriage in marriages:
            if random() <= self.probability:
                j = random()
                childrens.append(self.subcross(marriage, j))
                k = random()
                childrens.append(self.subcross(marriage, k))
            else:
                childrens.append(marriage[0])
                childrens.append(marriage[1])
        return childrens
