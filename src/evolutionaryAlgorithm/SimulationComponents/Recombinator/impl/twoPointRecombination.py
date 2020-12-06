from random import randint
from random import random
from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividualFactory import \
    FloatingPointIndividualFactory
from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.RecombinatorInterface import RecombinatorInterface


class twoPointRecombinator(RecombinatorInterface):

    def __init__(self, probability: float):
        self.probability = probability
        self.individualFactory = FloatingPointIndividualFactory.getFactory()

    def recombine(self, marriages: List[List[IndividualInterface]]) -> List[IndividualInterface]:
        dim = len(marriages[0][0].getRepresentation()) - 1
        firstPoint = randint(0, dim)
        secondPoint = randint(firstPoint, dim)
        childrens = []
        for el in marriages:
            temp1, temp2 = [], []
            if random() <= self.probability:
                for j in range(dim+1):
                    t1 = el[0].getRepresentation()
                    t2 = el[1].getRepresentation()
                    if j < firstPoint or j >= secondPoint:
                        temp1.append(t1[j])
                        temp2.append(t2[j])
                    else:
                        temp1.append(t2[j])
                        temp2.append(t1[j])
            else:
                temp1 = el[0]
                temp2 = el[1]
            childrens.append(self.individualFactory.getIndividual(temp1))
            childrens.append(self.individualFactory.getIndividual(temp2))
        return childrens
