from typing import List
from random import randint
from random import random

from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.RecombinatorInterface import RecombinatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual \
    import FloatingPointIndividual


class singlePointRecombinator(RecombinatorInterface):

    def __init__(self, probability: float):
        self.probability = probability

    def recombine(self, marriages: List[List[IndividualInterface]]) -> List[IndividualInterface]:
        i = len(marriages[0][0].getRepresentation())-1
        k = randint(0, i)
        childrens = []
        for el in marriages:
            temp1, temp2 = [], []
            if random() <= self.probability:
                t1 = el[0].getRepresentation()
                t2 = el[1].getRepresentation()
                for j in range(i+1):
                    if j < k:
                        temp1.append(t1[j])
                        temp2.append(t2[j])
                    else:
                        temp1.append(t2[j])
                        temp2.append(t1[j])
            else:
                temp1 = el[0].getRepresentation()
                temp2 = el[1].getRepresentation()
            childrens.append(FloatingPointIndividual(temp1))
            childrens.append(FloatingPointIndividual(temp2))
        return childrens
