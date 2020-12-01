from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.FitnessFunctionQuadratic import \
    FitnessFunctionQuadratic
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class FloatingPointIndividual(IndividualInterface):
    fitnessFunction = FitnessFunctionQuadratic()  # TODO add this as parameter of individual factory, also constructor should be privet

    def __init__(self, representation: List[float]):
        self.representation = representation
        self.fitnessFunctionEvaluation = FloatingPointIndividual.fitnessFunction.evaluate(representation)

    def getRepresentation(self):
        return self.representation

    def getEvaluation(self):
        return self.fitnessFunctionEvaluation
