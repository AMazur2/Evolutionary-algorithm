from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface
from abc import abstractmethod


class MutatorInterface(SimulationComponentInterface):
    
    @abstractmethod
    def mutate(self):
        pass
