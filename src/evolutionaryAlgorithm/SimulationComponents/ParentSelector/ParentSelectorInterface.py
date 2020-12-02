from abc import abstractmethod
from typing import List
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface


class ParentSelectorInterface(SimulationComponentInterface):
    
    @abstractmethod
    def getParents(self, population: List[IndividualInterface]):
        pass
