from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.Initializator.InitializatorInerface import InitializatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Mutator.MutatorInterface import MutatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.ParentSelectorInterface import \
    ParentSelectorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.RecombinatorInterface import RecombinatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.SurviviorSelector.SurviviorSelectorInterface import \
    SurviviorSelectorInterface


class EvolutionSimulator:
    initializator = InitializatorInterface
    recombinator = RecombinatorInterface
    mutator: MutatorInterface
    parentSelector: ParentSelectorInterface
    survivorSelector: SurviviorSelectorInterface

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
        fitness = self.markPopulation(population)

        while (not self.endSimulation()):
            parents = self.selectParents(population, fitness)
            offspring = self.applyRecombinations(parents)
            mutated = self.applyMutations(offspring)
            newGenerationCandidats = self.selectNewGeneration(offspring, population)
            population = self.selectPopulation(newGenerationCandidats)

            self.isEndSimulation = True  # TODO Remove me

    def initialize_population(self) -> List[IndividualInterface]:
        return self.initializator.initialize()

    def markPopulation(self, population: List[IndividualInterface]) -> List[float]:
        fitness = []
        for el in population:
            i = 0
        #    i = ocena(el)
            fitness.append(i)
        return fitness

    def endSimulation(self) -> bool:
        return self.isEndSimulation

    def selectParents(self, population: List[IndividualInterface]) -> List[IndividualInterface]:
        # return self.parentSelector.marry(population)
        pass

    def applyRecombinations(self, parents: List[IndividualInterface]) -> List[IndividualInterface]:
        # return self.recombinator.recombine(parents)
        pass

    def selectPopulation(self, newGenerationCandidats: List[IndividualInterface]) -> List[IndividualInterface]:
        pass

    def applyMutations(self, offspring: List[IndividualInterface]) -> List[IndividualInterface]:
        # newPopulation = self.mutator.mutate(offspring)
        # return newPopulation
        pass

    def selectNewGeneration(self, offspring: List[IndividualInterface], population: List[IndividualInterface]) -> List[
        IndividualInterface]:
        pass
