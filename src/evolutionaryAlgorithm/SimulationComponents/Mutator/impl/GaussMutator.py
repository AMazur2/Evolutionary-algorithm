from typing import List
from random import gauss
from random import random

from src.evolutionaryAlgorithm.SimulationComponents.Mutator.MutatorInterface import MutatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class GaussMutator(MutatorInterface):

    def __init__(self, sigma: float, probability: float):
        self.sigma = sigma

    def mutate(self, offspring: List[IndividualInterface]):
        mutated = []
        for el in offspring:
            temp = []
            for i in range(len(el)):
                temp.append(el[i]+gauss(0, self.sigma))
            mutated.append(temp)
        return mutated
