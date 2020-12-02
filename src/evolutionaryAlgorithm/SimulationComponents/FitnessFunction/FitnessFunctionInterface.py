from abc import abstractmethod
from typing import List
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class FitnessFunctionInterface:

    @abstractmethod
    def evaluate(self, representation: List[IndividualInterface]):
        pass