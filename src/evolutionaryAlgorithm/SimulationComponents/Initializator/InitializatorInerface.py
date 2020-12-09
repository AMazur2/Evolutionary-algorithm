from abc import abstractmethod

from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface


class InitializatorInterface(SimulationComponentInterface):
    @abstractmethod
    def initialize(self):
        pass  # TODO change all pass to NotImplementedException to be sure that correct method are run
