from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.SurviviorSelector.SurviviorSelectorInterface import \
    SurviviorSelectorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual import \
    FloatingPointIndividual


class eliteSurvivor(SurviviorSelectorInterface):

    def __init__(self):
        pass

    def selectSurvivor(self, population: List[List[IndividualInterface]],
                       offspring: List[List[IndividualInterface]]) -> List[List[IndividualInterface]]:

        t = len(population) / 2
        newGeneration = []

        fitness = []
        for el in population:
            fitness.append(el[0].getFitnessFunctionEvaluation())

        for i in range(int(t)):
            k = fitness[0]
            index = 0
            for j in range(len(fitness)):
                if k > fitness[j]:
                    k = fitness[j]
                    index = j
            del (fitness[index])
            temp = [FloatingPointIndividual(population[index][0].getRepresentation()),
                    FloatingPointIndividual(population[index][1].getRepresentation())]
            newGeneration.append(temp)
            del (population[index])

        fitness = []
        for el in offspring:
            fitness.append(el[0].getFitnessFunctionEvaluation())

        for i in range(int(t)):
            k = fitness[0]
            index = 0
            for j in range(len(fitness)):
                if k > fitness[j]:
                    k = fitness[j]
                    index = k
            del (fitness[index])
            temp = [FloatingPointIndividual(offspring[index][0].getRepresentation()),
                    FloatingPointIndividual(offspring[index][1].getRepresentation())]
            newGeneration.append(temp)
            del (offspring[index])

        return newGeneration
