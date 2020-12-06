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

    def __eq__(self, o: object) -> bool:  # TODO refactor if use parameters
        if isinstance(o, FitnessFunctionQuadratic):
            return True
        return False
