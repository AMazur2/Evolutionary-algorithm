from abc import abstractmethod
from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class ObserverInterface(object):
    @abstractmethod
    def observe(self, population: List[IndividualInterface], step: int):
        pass
