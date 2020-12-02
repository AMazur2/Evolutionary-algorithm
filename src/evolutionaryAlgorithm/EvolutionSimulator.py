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
from src.evolutionaryAlgorithm.SimulationComponents.Marriage.MarriageInterface import MarriageInterface


class EvolutionSimulator:
    initializator: InitializatorInterface
    recombinator: RecombinatorInterface
    mutator: MutatorInterface
    parentSelector: ParentSelectorInterface
    survivorSelector: SurviviorSelectorInterface
    fitnessFunction: FitnessFunctionInterface
    population: List[IndividualInterface]
    marriageSelector: MarriageInterface
    marriage: List[List[IndividualInterface]]

    def __init__(self, initializator, recombinator, mutator, parentSelector, survivorSelector, fitnessFunction,
                 marriageSelector):
        self.isEndSimulation = False
        self.initializator = initializator
        self.recombinator = recombinator
        self.mutator = mutator
        self.parentSelector = parentSelector
        self.survivorSelector = survivorSelector
        self.fitnessFunction = fitnessFunction
        self.marriageSelector = marriageSelector

    @staticmethod
    def fromSimulationComponentList(SimulationComponents):
        initializator = SimulationComponents["Initializator"]
        recombinator = SimulationComponents["Recombinator"]
        mutator = SimulationComponents["Mutator"]
        parentSelector = SimulationComponents["ParentSelector"]
        survivorSelector = SimulationComponents["SurvivorSelector"]
        fitnessFunction = SimulationComponents["FitnessFunction"]
        marriageSelector = SimulationComponents["Marriage"]

        return EvolutionSimulator(initializator, recombinator, mutator, parentSelector, survivorSelector,
                                  fitnessFunction, marriageSelector)

    def run(self):
        population = self.initialize_population()
        self.markPopulation(population)
        marriages = self.marry(population)

        while (not self.endSimulation()):
            parents = self.selectParents(marriages)
            offspring = self.applyRecombinations(parents)
            mutated = self.applyMutations(offspring)
            self.markPopulation(mutated)
            newMarriages = self.marry(mutated)
            # self.markPopulation(mutated)
            marriages = self.selectNewGeneration(marriages, newMarriages)

            self.isEndSimulation = True  # TODO Remove me

    def initialize_population(self) -> List[IndividualInterface]:
        return self.initializator.initialize()

    def marry(self, population: List[IndividualInterface]) -> List[List[IndividualInterface]]:
        return self.marriageSelector.marry(population)

    def markPopulation(self, population: List[IndividualInterface]):
        self.fitnessFunction.evaluate(population)

    def endSimulation(self) -> bool:
        return self.isEndSimulation

    def selectParents(self, population: List[List[IndividualInterface]]) -> List[List[IndividualInterface]]:
        return self.parentSelector.getParents(population)

    def applyRecombinations(self, parents: List[List[IndividualInterface]]) -> List[IndividualInterface]:
        return self.recombinator.recombine(parents)

    def applyMutations(self, offspring: List[IndividualInterface]) -> List[IndividualInterface]:
        newPopulation = self.mutator.mutate(offspring)
        return newPopulation

    def selectNewGeneration(self, population: List[List[IndividualInterface]],
                            offspring: List[List[IndividualInterface]]) -> List[IndividualInterface]:
        return self.survivorSelector.selectSurvivor(offspring, population)
