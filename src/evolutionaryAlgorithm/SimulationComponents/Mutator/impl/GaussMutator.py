from typing import List
from random import gauss
from random import random

from src.evolutionaryAlgorithm.SimulationComponents.Mutator.MutatorInterface import MutatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class GaussMutator(MutatorInterface):

    def __init__(self, sigma: float, probability: float):
        self.sigma = sigma
        self.probability = probability

    def mutate(self, population: List[IndividualInterface], offspring: List[IndividualInterface]):
        mutated = []
        for el in population:
            if random() <= self.probability:
                temp = []
                for i in range(len(el)):
                    temp.append(el[i] + gauss(0, self.sigma))
                mutated.append(temp)
            else:
                mutated.append(el)

        for el in offspring:
            if random() <= self.probability:
                temp = []
                for i in range(len(el)):
                    temp.append(el[i]+gauss(0, self.sigma))
                mutated.append(temp)
            else:
                mutated.append(el)

        return mutated
