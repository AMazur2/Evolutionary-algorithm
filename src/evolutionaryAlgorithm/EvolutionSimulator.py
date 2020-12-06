from typing import List

from src.evolutionaryAlgorithm.Observers.ObserverInterface import ObserverInterface
from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.FitnessFunctionInterface import \
    FitnessFunctionInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.Initializator.InitializatorInerface import InitializatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Mutator.MutatorInterface import MutatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.ParentSelectorInterface import \
    ParentSelectorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.RecombinatorInterface import RecombinatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.SurviviorSelector.SurviviorSelectorInterface import \
    SurviviorSelectorInterface


class EvolutionSimulator:
    initializator: InitializatorInterface
    recombinator: RecombinatorInterface
    mutator: MutatorInterface
    parentSelector: ParentSelectorInterface
    survivorSelector: SurviviorSelectorInterface
    fitnessFunction: FitnessFunctionInterface
    population: List[IndividualInterface]

    def __init__(self, initializator, recombinator, mutator, parentSelector, survivorSelector, fitnessFunction,
                 observers: List[ObserverInterface],
                 maxSteps=20):
        self.observers = observers
        self.maxSteps = maxSteps
        self.isEndSimulation = False
        self.initializator = initializator
        self.recombinator = recombinator
        self.mutator = mutator
        self.parentSelector = parentSelector
        self.survivorSelector = survivorSelector
        self.fitnessFunction = fitnessFunction

    @staticmethod
    def fromSimulationComponentList(SimulationComponents, observers: List[ObserverInterface]):
        initializator = SimulationComponents["Initializator"]
        recombinator = SimulationComponents["Recombinator"]
        mutator = SimulationComponents["Mutator"]
        parentSelector = SimulationComponents["ParentSelector"]
        survivorSelector = SimulationComponents["SurvivorSelector"]
        fitnessFunction = SimulationComponents["FitnessFunction"]

        return EvolutionSimulator(initializator, recombinator, mutator, parentSelector, survivorSelector,
                                  fitnessFunction, observers)

    def run(self):
        population = self.initialize_population()
        # marriages = self.marry(population)
        self.simulationStep = 0

        while (not self.endSimulation()):
            parents = self.selectParents(population)
            offspring = self.applyRecombinations(parents)
            mutated = self.applyMutations(offspring)
            population = self.selectNewGeneration(mutated, population)

            self.observe(population, self.simulationStep)
            self.simulationStep += 1

    def initialize_population(self) -> List[IndividualInterface]:
        return self.initializator.initialize()

    def marry(self, population: List[IndividualInterface]) -> List[List[IndividualInterface]]:
        pass

    def endSimulation(self) -> bool:
        if self.simulationStep >= self.maxSteps:
            return True
        return False

    def selectParents(self, population: List[IndividualInterface]) -> List[List[IndividualInterface]]:
        return self.parentSelector.getParents(population)

    def applyRecombinations(self, parents: List[List[IndividualInterface]]) -> List[IndividualInterface]:
        return self.recombinator.recombine(parents)

    def applyMutations(self, offspring: List[IndividualInterface]) -> List[IndividualInterface]:
        newPopulation = self.mutator.mutate(offspring)
        return newPopulation

    def selectNewGeneration(self, offspring: List[IndividualInterface], population: List[IndividualInterface]) -> List[
        IndividualInterface]:
        return self.survivorSelector.selectSurvivor(population, offspring)

    def observe(self, population: List[IndividualInterface], step: int):
        for observer in self.observers:
            observer.observe(population, step)
