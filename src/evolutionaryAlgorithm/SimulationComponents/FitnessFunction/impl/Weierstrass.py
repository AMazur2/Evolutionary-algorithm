from typing import List

import numpy as np

from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.FitnessFunctionInterface import \
    FitnessFunctionInterface


class Weierstrass(FitnessFunctionInterface):

    def evaluate(self, representation: List[float]) -> float:
        temp = representation
        tab = np.array(temp)
        tab = 0.005 * tab
        k = np.arange(start=0, stop=21, step=1)
        ak = 0.5 ** k
        bk = np.pi * (3 ** k)
        sm = 0.0
        for i in range(0, len(tab)):
            kcs = ak * np.cos(2 * (tab[i] + 0.5) * bk)
            ksm = 0.0
            for j in range(0, 21):
                ksm += kcs[j]
            sm += ksm
        kcs = ak * np.cos(bk)
        ksm = 0.0
        for j in range(0, 21):
            ksm += kcs[j]
        val = sm - len(tab) * ksm
        return val
