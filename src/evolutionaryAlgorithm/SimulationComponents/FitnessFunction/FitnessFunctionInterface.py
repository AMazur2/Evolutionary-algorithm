from abc import abstractmethod
from typing import List


class FitnessFunctionInterface:

    @abstractmethod
    def evaluate(self, representation: List[float]):
        pass
