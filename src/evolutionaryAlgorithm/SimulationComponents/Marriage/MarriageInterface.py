from abc import abstractmethod
from typing import List
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface


class MarriageInterface(SimulationComponentInterface):

    @abstractmethod
    def marry(self, population: List[IndividualInterface]):
        pass