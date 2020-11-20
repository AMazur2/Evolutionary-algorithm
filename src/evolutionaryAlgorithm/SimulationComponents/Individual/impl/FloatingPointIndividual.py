from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class FloatingPointIndividual(IndividualInterface):

    def FloatingPointIndividual(self, representation: List[float]) -> IndividualInterface:
        self.representation = representation

    def getRepresentation(self):
        return self.representation
