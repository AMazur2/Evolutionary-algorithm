from abc import abstractmethod
from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface


class ParentSelectorInterface(SimulationComponentInterface):
    
    @abstractmethod
    def marry(self, population: List):
        pass
