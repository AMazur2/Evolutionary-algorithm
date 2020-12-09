from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividualFactory import \
    FloatingPointIndividualFactory
from src.evolutionaryAlgorithm.SimulationComponents.SurviviorSelector.SurviviorSelectorInterface import \
    SurviviorSelectorInterface


class eliteSurvivor(SurviviorSelectorInterface):

    def __init__(self):
        self.individualFactory: FloatingPointIndividualFactory = FloatingPointIndividualFactory.getFactory()

    def selectSurvivor(self, population: List[IndividualInterface], offspring: List[IndividualInterface]) -> \
            List[IndividualInterface]:

        t = len(population) / 4  # TODO population size must be defidable by 4
        if len(population) % 4 != 0:
            raise Exception("Population Size not dividable by 4")
        newGeneration = []

        for i in range(int(t)):
            bestIndyvidual = population[0]
            for individual in population:
                if bestIndyvidual.getEvaluation() > individual.getEvaluation():
                    bestIndyvidual = individual
            newGeneration.append(bestIndyvidual)
            newGeneration.append(bestIndyvidual.getPartner())
            population.remove(bestIndyvidual.getPartner())
            population.remove(bestIndyvidual)

        for i in range(int(t)):
            bestIndyvidual = offspring[0]
            for individual in offspring:
                if bestIndyvidual.getEvaluation() > individual.getEvaluation():
                    bestIndyvidual = individual
            newGeneration.append(bestIndyvidual)
            newGeneration.append(bestIndyvidual.getPartner())
            offspring.remove(bestIndyvidual.getPartner())
            offspring.remove(bestIndyvidual)

        return newGeneration
