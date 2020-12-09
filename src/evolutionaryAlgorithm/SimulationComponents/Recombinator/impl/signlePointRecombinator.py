from random import randint
from random import random
from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividualFactory import \
    FloatingPointIndividualFactory
from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.RecombinatorInterface import RecombinatorInterface


class singlePointRecombinator(RecombinatorInterface):

    def __init__(self, probability: float):
        self.probability = probability
        self.individualFactory: FloatingPointIndividualFactory = FloatingPointIndividualFactory.getFactory()

    def recombine(self, marriages: List[List[IndividualInterface]]) -> List[IndividualInterface]:
        i = len(marriages[0][0].getRepresentation()) - 1
        k = randint(0, i)
        childrens = []
        for el in marriages:
            temp1, temp2 = [], []
            if random() <= self.probability:
                t1 = el[0].getRepresentation()
                t2 = el[1].getRepresentation()
                for j in range(i + 1):
                    if j < k:
                        temp1.append(t1[j])
                        temp2.append(t2[j])
                    else:
                        temp1.append(t2[j])
                        temp2.append(t1[j])
            else:
                temp1 = el[0].getRepresentation()
                temp2 = el[1].getRepresentation()
            childrens.append(self.individualFactory.getIndividual(temp1))
            childrens.append(self.individualFactory.getIndividual(temp2))
        return childrens
