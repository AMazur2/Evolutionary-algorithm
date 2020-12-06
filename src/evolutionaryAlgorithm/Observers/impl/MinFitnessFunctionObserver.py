from typing import List

from src.evolutionaryAlgorithm.Observers.ObserverInterface import ObserverInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


class MinFitnessFunctionObserver(ObserverInterface):
    fileName = "minFitnessFunctionObserver.txt"  # TODO change this
    open(fileName, 'w').close()

    @classmethod
    def observe(cls, population: List[IndividualInterface], step: int):
        evaluationMin = 999999  # TODO change this
        for individual in population:
            evaluation = individual.getEvaluation()
            if evaluation < evaluationMin:
                evaluationMin = evaluation

        cls.writeToFile(step, evaluationMin)

    @classmethod
    def writeToFile(cls, step: int, evaluationMin: float):

        with open(cls.fileName, 'a') as f:
            f.write(f"{step} : {evaluationMin}")
            f.write("\n")
