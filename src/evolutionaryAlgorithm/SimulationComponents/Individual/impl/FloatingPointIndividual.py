from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.FitnessFunctionInterface import \
    FitnessFunctionInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class FloatingPointIndividual(IndividualInterface):

    @classmethod
    def create_from_representation_list(cls, representation: List[float], fitnessFunction: FitnessFunctionInterface):
        return cls(representation, fitnessFunction, _is_direct=False)

    def __init__(self, representation: List[float], fitnessFunction: FitnessFunctionInterface, _is_direct=True):
        # don't initialize me directly
        if _is_direct:
            raise TypeError("create with Foo.create_from_*")

        self.__representation = representation
        self.__fitnessFunctionEvaluation = fitnessFunction.evaluate(representation)

    def getRepresentation(self) -> List[float]:
        return list(self.__representation)

    def getEvaluation(self) -> float:
        return self.__fitnessFunctionEvaluation
