from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.FitnessFunctionInterface import \
    FitnessFunctionInterface
from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.ExpandedSchaffers import ExpandedSchaffers
from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.FitnessFunctionQuadratic import \
    FitnessFunctionQuadratic
from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.Weierstrass import Weierstrass
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual import \
    FloatingPointIndividual


class FloatingPointIndividualFactory():
    instance = None

    def __init__(self, fitnessFunction: FitnessFunctionInterface) -> None:
        self.fitnessFunction: FitnessFunctionInterface = fitnessFunction

    def getIndividual(self, representation: List[float]) -> FloatingPointIndividual:
        return FloatingPointIndividual.create_from_representation_list(representation, self.fitnessFunction)

    @classmethod
    def getFactory(cls):
        if cls.instance == None:
            raise Exception("Factory not created ")
        else:
            return cls.instance

    @classmethod
    def createFactory(cls, fitnessFunctionName: str):
        if cls.instance == None:
            if fitnessFunctionName == "FitnessFunctionQuadratic":
                cls.instance = FloatingPointIndividualFactory(FitnessFunctionQuadratic())
            elif fitnessFunctionName == "Weierstrass":
                cls.instance = FloatingPointIndividualFactory(Weierstrass())
            elif fitnessFunctionName == "ExpandedSchaffers":
                cls.instance = FloatingPointIndividualFactory(ExpandedSchaffers())
            else:
                raise NotImplementedError
        elif str(cls.instance.fitnessFunction) == fitnessFunctionName:
            return
        else:
            raise Exception("Factory is created ")
