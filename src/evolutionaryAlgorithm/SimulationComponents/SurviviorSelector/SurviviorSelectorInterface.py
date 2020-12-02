from abc import abstractmethod
from typing import List
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class SurviviorSelectorInterface(SimulationComponentInterface):

    @abstractmethod
    def selectSurvivor(self, population: List[IndividualInterface], offspring: List[IndividualInterface]):
        pass
