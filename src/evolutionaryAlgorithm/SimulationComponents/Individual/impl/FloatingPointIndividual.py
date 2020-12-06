from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.FitnessFunctionQuadratic import \
    FitnessFunctionQuadratic
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class FloatingPointIndividual(IndividualInterface):
    fitnessFunction = FitnessFunctionQuadratic()  # TODO add this as parameter of individual factory, also constructor should be privet

    def __init__(self, representation: List[float]):
        self.__representation = representation
        self.__fitnessFunctionEvaluation = FloatingPointIndividual.fitnessFunction.evaluate(representation)

    def getRepresentation(self):
        return list(self.__representation)

    def getEvaluation(self):
        return self.__fitnessFunctionEvaluation

    def setFitnessFunctionEvaluation(self, value: float):
        self.__fitnessFunctionEvaluation = value