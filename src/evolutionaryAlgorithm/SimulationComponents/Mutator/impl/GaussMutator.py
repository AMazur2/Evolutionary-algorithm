from random import gauss
from random import random
from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividualFactory import \
    FloatingPointIndividualFactory
from src.evolutionaryAlgorithm.SimulationComponents.Mutator.MutatorInterface import MutatorInterface


class GaussMutator(MutatorInterface):

    def __init__(self, sigma: float, probabilityOfMutation: float):
        self.sigma = sigma
        self.probabilityOfMutation = probabilityOfMutation
        self.individualFactory: FloatingPointIndividualFactory = FloatingPointIndividualFactory.getFactory()

    def mutate(self, offspring: List[IndividualInterface]) -> List[IndividualInterface]:
        mutatedIndividuals = []

        for individual in offspring:
            newIndividualFeatures = []
            temp = individual.getRepresentation()
            for i in range(len(temp)):
                if random() <= self.probabilityOfMutation:
                    newIndividualFeatures.append(temp[i] + gauss(0, self.sigma))
                else:
                    newIndividualFeatures.append(temp[i])
            mutatedIndividuals.append(self.individualFactory.getIndividual(newIndividualFeatures))
        return mutatedIndividuals
