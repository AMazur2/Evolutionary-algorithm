from typing import List
from math import sqrt
from src.evolutionaryAlgorithm.Observers.ObserverInterface import ObserverInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface

class AverageAndDeviationObserver(ObserverInterface):

    def __init__(self, pathDeviation: str, pathAverage) -> None:
        self.fileName1 = pathDeviation
        self.fileName2 = pathAverage
        with open(self.fileName1, 'w') as f:
            f.write("")
        with open(self.fileName2, 'w') as f:
            f.write("")

    def observe(self, population: List[IndividualInterface], step: int):
        fitness = []
        sumAll = 0.0
        for individual in population:
            fitness.append(individual.getEvaluation())
            sumAll = sumAll + individual.getEvaluation()

        average = sumAll / len(fitness)
        self.writeToFileAverage(step, average)

        variance = 0
        for el in fitness:
            variance = variance + (el - sumAll)**2

        variance = variance / len(fitness)
        standarDeviation = sqrt(variance)

        self.writeToFileDeviation(step, standarDeviation)

    def writeToFileAverage(self, step: int, average: float):
        with open(self.fileName1, 'a') as f:
            f.write(f"{step} : {average}")
            f.write("\n")


    def writeToFileDeviation(self, step: int, deviation: float):
        with open(self.fileName2, 'a') as f:
            f.write(f"{step} : {deviation}")
            f.write("\n")
