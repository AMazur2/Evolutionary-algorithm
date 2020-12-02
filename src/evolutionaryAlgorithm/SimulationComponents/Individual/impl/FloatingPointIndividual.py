from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class FloatingPointIndividual(IndividualInterface):

    def __init__(self, representation: List[float]):
        self.__representation = representation
        self.__fitnessFunctionEvaluation = 0.0

    def getRepresentation(self):
        return list(self.__representation)

    def getFitnessFunctionEvaluation(self):
        return self.__fitnessFunctionEvaluation

    def setFitnessFunctionEvaluation(self, value: float):
        self.__fitnessFunctionEvaluation = value
