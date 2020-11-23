from typing import List
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface
from abc import abstractmethod


class RecombinatorInterface(SimulationComponentInterface):
    @abstractmethod
    def recombine(self, population: List[IndividualInterface]):
        pass
