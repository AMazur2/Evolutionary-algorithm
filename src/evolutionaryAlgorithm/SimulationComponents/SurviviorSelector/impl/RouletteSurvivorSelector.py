from random import uniform
from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.SurviviorSelector.SurviviorSelectorInterface import \
    SurviviorSelectorInterface


class RouletteSurvivorSelector(SurviviorSelectorInterface):

    def __init__(self):
        pass

    def selectSurvivor(self, population: List[IndividualInterface]) -> List[IndividualInterface]:
        number = len(population)
        fitness = []
        for el in population:
            fitness.append(el.getFitnessFunctionEvaluation())
        max, min, sum = 0, fitness[0], 0
        for i in range(number):
            sum += fitness[i]
            if min > fitness[i]:
                min = fitness[i]
            if max < fitness[i]:
                max = fitness[i]

        param = max - min
        fitnessPrim = []
        for i in range(number):  # q' = (q-min(q))*(max(q)-min(q))
            a = fitness[i] - min
            b = a * param  # q" = 1-q'
            fitnessPrim.append(1 - b)

        survivors = []
        for i in range(int(number / 2)):
            k = self.chooseOne(fitnessPrim, sum)
            survivors.append(population[k])
        return survivors

    def chooseOne(self, fitness: List[float], maximum: float) -> int:
        pick = uniform(0, maximum)
        current = 0
        for i in range(len(fitness)):
            current += fitness[i]
            if current > pick:
                return i
