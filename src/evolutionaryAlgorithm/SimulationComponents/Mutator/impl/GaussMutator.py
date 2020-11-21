from typing import List
from ranfom import gauss

from src.evolutionaryAlgorithm.SimulationComponents.Mutator.MutatorInerface import MutatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface

class GaussMutator(MutatorInterface):

    def __init__ (self, sigma: float):
        self.sigma = sigma

    def mutate (self, Population: List[IndividualInterface]):
        #mutated = []
        for el in Population:
            temp = []
            for i in range(len(el)):
                temp.append(el[i] + gauss(0,sigma))
            el = temp
            #mutated.append(temp)
        #return mutated
