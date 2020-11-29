from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class FloatingPointIndividual(IndividualInterface):

    def __init__(self, representation: List[float]):
        self.__representation = representation

    def getRepresentation(self):
        return list(self.__representation)
