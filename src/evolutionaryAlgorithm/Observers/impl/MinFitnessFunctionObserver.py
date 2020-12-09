from typing import List

from src.evolutionaryAlgorithm.Observers.ObserverInterface import ObserverInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class MinFitnessFunctionObserver(ObserverInterface):

    def __init__(self, path: str) -> None:
        self.fileName = path
        with open(self.fileName, 'w') as f:
            f.write("")

    def observe(self, population: List[IndividualInterface], step: int):
        evaluationMin = population[0].getEvaluation()
        for individual in population:
            evaluation = individual.getEvaluation()
            if evaluation < evaluationMin:
                evaluationMin = evaluation

        self.writeToFile(step, evaluationMin)

    def writeToFile(self, step: int, evaluationMin: float):

        with open(self.fileName, 'a') as f:
            f.write(f"{step} : {evaluationMin}")
            f.write("\n")
