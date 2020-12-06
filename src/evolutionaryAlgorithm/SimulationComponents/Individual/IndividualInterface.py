from abc import abstractmethod

from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface


class IndividualInterface(SimulationComponentInterface):

    @abstractmethod
    def getRepresentation(self):
        pass

    @abstractmethod
    def getFitnessFunctionEvaluation(self):
        pass

    @abstractmethod
    def setFitnessFunctionEvaluation(self, value: float):
        pass