from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.FitnessFunctionInterface import \
    FitnessFunctionInterface
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
    def createFactory(cls, fitnessFunction: FitnessFunctionInterface):
        if cls.instance == None:
            cls.instance = FloatingPointIndividualFactory(fitnessFunction)
        elif cls.instance.fitnessFunction == fitnessFunction:
            return
        else:
            raise Exception("Factory is created ")
