from typing import List
from random import gauss
from random import random
from abc import abstractmethod

from src.evolutionaryAlgorithm.SimulationComponents.Mutator.MutatorInterface import MutatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class GaussMutator(MutatorInterface):

    def __init__(self, sigma: float, probability: float):
        self.sigma = sigma
        self.probability = probability

    @abstractmethod
    def mutate(self, offspring: List[IndividualInterface]):
        mutated = []
        for el in offspring:
            temp = []
            for i in range(len(el)):
                if random() <= self.probability:
                    temp.append(el[i]+gauss(0, self.sigma))
                else:
                    temp.append(el[i])
            mutated.append(temp)
        return mutated
