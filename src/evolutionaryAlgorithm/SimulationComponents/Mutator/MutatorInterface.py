from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface
from abc import abstractmethod
from typing import List
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class MutatorInterface(SimulationComponentInterface):
    
    @abstractmethod
    def mutate(self, population: List[IndividualInterface], offspring: List[IndividualInterface]):
        pass
