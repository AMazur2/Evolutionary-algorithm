from abc import abstractmethod

from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface


class IndividualInterface(SimulationComponentInterface):

    @abstractmethod
    def getRepresentation(self):
        pass
