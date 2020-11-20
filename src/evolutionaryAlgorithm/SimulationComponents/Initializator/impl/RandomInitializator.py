from random import uniform
from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual import \
    FloatingPointIndividual
from src.evolutionaryAlgorithm.SimulationComponents.Initializator.InitializatorInerface import InitializatorInterface


class RandomInitializator(InitializatorInterface):

    def __init__(self, populationSize: int, dimensions: int, rangeMin: int, rangeMax: int):
        self.populationSize = populationSize
        self.dimensions = dimensions
        self.rangeMax = rangeMax
        self.rangeMin = rangeMin

    def initialize(self) -> List[IndividualInterface]:
        return [FloatingPointIndividual(  # TODO find why this is warning, how to cast to interface
            [uniform(self.rangeMin, self.rangeMax)
             for i in range(self.dimensions)])
            for j in range(self.populationSize)]
