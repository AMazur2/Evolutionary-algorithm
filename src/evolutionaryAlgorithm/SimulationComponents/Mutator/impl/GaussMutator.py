from typing import List
from random import gauss
from random import random

from src.evolutionaryAlgorithm.SimulationComponents.Mutator.MutatorInerface import MutatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface

class GaussMutator(MutatorInterface):

    def __init__ (self, sigma: float, probability: float):
        self.sigma = sigma
        self.probability = probability

    def mutate (self, Population: List[IndividualInterface]):
        #mutated = []
        for el in Population:
            if random() <= self.probability:
                temp = []
                for i in range(len(el)):
                    temp.append(el[i] + gauss(0,sigma))
                el = temp
            #mutated.append(temp)
        #return mutated
