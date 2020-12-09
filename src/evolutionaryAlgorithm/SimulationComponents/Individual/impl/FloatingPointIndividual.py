from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.FitnessFunctionInterface import \
    FitnessFunctionInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class FloatingPointIndividual(IndividualInterface):

    @classmethod
    def create_from_representation_list(cls, representation: List[float], fitnessFunction: FitnessFunctionInterface,
                                        isModivied: bool):
        return cls(representation, fitnessFunction, isModivied, _is_direct=False)

    def __init__(self, representation: List[float], fitnessFunction: FitnessFunctionInterface, isModivied: bool,
                 _is_direct=True):
        # don't initialize me directly
        if _is_direct:
            raise TypeError("create with Foo.create_from_*")

        self.__representation = representation
        self.__fitnessFunctionEvaluation = fitnessFunction.evaluate(representation)
        self.__partner: FloatingPointIndividual = None
        self.__isModivied = isModivied

    def getRepresentation(self) -> List[float]:
        return list(self.__representation)

    def setPartner(self, partner):  #: FloatingPointIndividual
        if self.__isModivied:
            if self.__partner is None:
                self.__partner = partner
                partner.__partner = self
            else:
                raise Exception("Individual already have partner")
        else:
            raise Exception("Individual is not modivied, don't set it's Partner")

    def getEvaluation(self) -> float:
        if self.__isModivied:
            if self.__partner is None:
                raise Exception("Individual doesn't have partner")
            else:
                return min(self.__fitnessFunctionEvaluation, self.__partner.__fitnessFunctionEvaluation)
        else:
            return self.__fitnessFunctionEvaluation
