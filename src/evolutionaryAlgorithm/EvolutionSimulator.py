from typing import List
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
    initializator : InitializatorInterface
    recombinator : RecombinatorInterface
    mutator: MutatorInterface
    parentSelector: ParentSelectorInterface
    survivorSelector: SurviviorSelectorInterface
    fitnessFunction: FitnessFunctionInterface
    population: List[IndividualInterface]

    def __init__(self, initializator, recombinator, mutator, parentSelector, survivorSelector, fitnessFunction):
        self.isEndSimulation = False
        self.initializator = initializator
        self.recombinator = recombinator
        self.mutator = mutator
        self.parentSelector = parentSelector
        self.survivorSelector = survivorSelector
        self.fitnessFunction = fitnessFunction

    @staticmethod
    def fromSimulationComponentList(SimulationComponents):
        initializator = SimulationComponents["Initializator"]
        recombinator = SimulationComponents["Recombinator"]
        mutator = SimulationComponents["Mutator"]
        parentSelector = SimulationComponents["ParentSelector"]
        survivorSelector = SimulationComponents["SurvivorSelector"]
        fitnessFunction = SimulationComponents["FitnessFunction"]

        return EvolutionSimulator(initializator, recombinator, mutator, parentSelector, survivorSelector,
                                  fitnessFunction)

    def run(self):
        population = self.initialize_population()
        self.markPopulation(population)
        # marriages = self.marry(population)

        while (not self.endSimulation()):
            parents = self.selectParents(population)
            offspring = self.applyRecombinations(parents)
            mutated = self.applyMutations(offspring)
            self.markPopulation(mutated)
            population = self.selectNewGeneration(mutated, population)

            self.isEndSimulation = True  # TODO Remove me

    def initialize_population(self) -> List[IndividualInterface]:
        return self.initializator.initialize()

    def marry(self, population: List[IndividualInterface]) -> List[List[IndividualInterface]]:
        pass

    def markPopulation(self, population: List[IndividualInterface]):
        self.fitnessFunction.evaluate(population)

    def endSimulation(self) -> bool:
        return self.isEndSimulation

    def selectParents(self, population: List[IndividualInterface]) -> List[List[IndividualInterface]]:
        return self.parentSelector.getParents(population)

    def applyRecombinations(self, parents: List[List[IndividualInterface]]) -> List[IndividualInterface]:
        return self.recombinator.recombine(parents)

    def applyMutations(self, offspring: List[IndividualInterface]) -> List[IndividualInterface]:
        newPopulation = self.mutator.mutate(offspring)
        return newPopulation

    def selectNewGeneration(self, offspring: List[IndividualInterface], population: List[IndividualInterface]) -> List[
        IndividualInterface]:
        temporary = []
        for el in offspring:
            temporary.append(el)
        for el in population:
            temporary.append(el)
        return self.survivorSelector.selectSurvivor(temporary)
