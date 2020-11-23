from abc import abstractmethod

from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface


class ParentSelectorInterface(SimulationComponentInterface):
    
    @abstractmethod
    def marry(self):
        pass
