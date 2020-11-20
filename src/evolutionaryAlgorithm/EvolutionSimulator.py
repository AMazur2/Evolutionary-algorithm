from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.Initializator.InitializatorFactory import InitializatorFactory
from src.evolutionaryAlgorithm.SimulationComponents.Mutator.MutatorFactory import MutatorFactory
from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.ParentSelectorFactory import ParentSelectorFactory
from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.RecombinatorFactory import RecombinatorFactory
from src.evolutionaryAlgorithm.SimulationComponents.SurviviorSelector.SurviviorSelectorFactory import \
    SurviviorSelectorFactory


class EvolutionSimulator:
    initializator: InitializatorFactory
    recombinator: RecombinatorFactory
    mutator: MutatorFactory
    parentSelector: ParentSelectorFactory
    survivorSelector: SurviviorSelectorFactory

    population: List[IndividualInterface]

    def __init__(self, initializator, recombinator, mutator, parentSelector, survivorSelector):
        self.isEndSimulation = False
        self.initializator = initializator
        self.recombinator = recombinator
        self.mutator = mutator
        self.parentSelector = parentSelector
        self.survivorSelector = survivorSelector

    @staticmethod
    def fromSimulationComponentList(SimulationComponents):
        initializator = SimulationComponents["Initializator"]
        recombinator = SimulationComponents["Recombinator"]
        mutator = SimulationComponents["Mutator"]
        parentSelector = SimulationComponents["ParentSelector"]
        survivorSelector = SimulationComponents["SurvivorSelector"]

        return EvolutionSimulator(initializator, recombinator, mutator, parentSelector, survivorSelector)

    def run(self):
        population = self.initialize_population()

        while (not self.endSimulation()):
            parents = self.selectParents()
            offspring = self.applyRecombinations(parents)
            offspring = self.applyMutations(offspring, population)
            newGenerationCandidats = self.selectNewGeneration(offspring, population)
            population = self.selectPopulation(newGenerationCandidats)

            self.isEndSimulation = True  # TODO Remove me

    def initialize_population(self) -> List[IndividualInterface]:
        pass

    def endSimulation(self) -> bool:
        return self.isEndSimulation

    def selectParents(self) -> List[IndividualInterface]:
        pass

    def applyRecombinations(self, parents: List[IndividualInterface]) -> List[IndividualInterface]:
        pass

    def selectPopulation(self, newGenerationCandidats: List[IndividualInterface]) -> List[IndividualInterface]:
        pass

    def applyMutations(self, offspring: List[IndividualInterface], population: List[IndividualInterface]) -> List[
        IndividualInterface]:
        pass

    def selectNewGeneration(self, offspring: List[IndividualInterface], population: List[IndividualInterface]) -> List[
        IndividualInterface]:
        pass
