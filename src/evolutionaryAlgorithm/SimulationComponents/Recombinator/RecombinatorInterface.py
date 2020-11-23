from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface
from abc import abstractmethod


class RecombinatorInterface(SimulationComponentInterface):
    @abstractmethod
    def recombine(self):
        pass
