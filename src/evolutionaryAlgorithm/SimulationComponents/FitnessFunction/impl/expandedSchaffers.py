from typing import List
import numpy as np
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.FitnessFunctionInterface import \
    FitnessFunctionInterface


class expandedSchaffers(FitnessFunctionInterface):

    def evaluate(self, representation: List[IndividualInterface]):
        for el in representation:
            temp = el.getRepresentation()
            tab = np.array(temp)
            sm = 0.0
            for i in range(0, len(tab) - 1):
                t = tab[i] * tab[i] + tab[i + 1] * tab[i + 1]
                t1 = np.sin(np.sqrt(t))
                t1 = t1 * t1 - 0.5
                t2 = 1 + 0.001 * t
                t2 = t2 * t2
                sm += 0.5 + t1 / t2
            el.setFitnessFunctionEvaluation(sm)
