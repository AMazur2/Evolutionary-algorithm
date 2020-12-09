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
        self.fitnessFunctionEvaluation = fitnessFunction.evaluate(representation)
        self.partner: FloatingPointIndividual = None
        self.isModivied = isModivied

    def getRepresentation(self) -> List[float]:
        return list(self.__representation)

    def havePartner(self):
        return self.partner != None

    def getPartner(self):
        return self.partner

    def setPartner(self, partner):  #: FloatingPointIndividual
        if self.isModivied:
            if self.partner is None:
                self.partner = partner
                partner.partner = self
            else:
                raise Exception("Individual already have partner")
        else:
            raise Exception("Individual is not modivied, don't set it's Partner")

    def getEvaluation(self) -> float:
        if self.isModivied:
            if self.partner is None:
                raise Exception("Individual doesn't have partner")
            else:
                return min(self.fitnessFunctionEvaluation, self.partner.fitnessFunctionEvaluation)
        else:
            return self.fitnessFunctionEvaluation
