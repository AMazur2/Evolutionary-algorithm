from typing import List
from random import gauss
from random import random

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual import \
    FloatingPointIndividual
from src.evolutionaryAlgorithm.SimulationComponents.Mutator.MutatorInterface import MutatorInterface


class GaussMutator(MutatorInterface):

    def __init__(self, sigma: float, probabilityOfMutation: float):
        self.sigma = sigma
        self.probabilityOfMutation = probabilityOfMutation

    def mutate(self, offspring: List[IndividualInterface]) -> List[IndividualInterface]:
        mutatedIndividuals = []

        for individual in offspring:
            newIndividualFeatures = []
            for feature in individual.getRepresentation():
                if random() <= self.probabilityOfMutation:
                    newIndividualFeatures.append(feature+gauss(0, self.sigma))
                else:
                    newIndividualFeatures.append(feature)
            mutatedIndividuals.append(FloatingPointIndividual(newIndividualFeatures))
        return mutatedIndividuals
