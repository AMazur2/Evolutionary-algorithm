from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.FitnessFunctionInterface import \
    FitnessFunctionInterface


class FitnessFunctionQuadratic(FitnessFunctionInterface):

    def __init__(self):
        pass

    def evaluate(self, representation: List[float]) -> float:
        suma = 0
        for feauture in representation:
            suma += feauture * feauture
        return suma
