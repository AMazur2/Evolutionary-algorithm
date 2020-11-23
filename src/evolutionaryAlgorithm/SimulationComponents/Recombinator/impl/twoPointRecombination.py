from typing import List
from random import randint
from random import random

from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.RecombinatorInterface import RecombinatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface

class twoPointRecombinator(RecombinatorInterface):

    def __init__ (self, probability: float):
        self.probability = probability

    def recombine(self, marriages: List):
        dim = len(marriages[0][0])
        firstPoint = randint(0, dim)
        secondPoint = randint(firstPoint, dim)
        childrens = []
        for el in marriages:
            temp1, temp2 = [], []
            if random() <= self.probability:
                for j in range(dim):
                    if j < firstPoint or j >= secondPoint:
                        temp1.append(el[0][j])
                        temp2.append(el[1][j])
                    else:
                        temp1.append(el[1][j])
                        temp2.append(el[0][j])
            else:
                temp1 = el[0]
                temp2 = el[1]
            childrens.append(temp1)
            childrens.append(temp2)    
        return childrens