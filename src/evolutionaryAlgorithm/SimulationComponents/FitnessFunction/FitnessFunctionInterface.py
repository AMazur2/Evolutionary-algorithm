from abc import abstractmethod
from typing import List


class FitnessFunctionInterface:

    @abstractmethod
    def evaluate(self, representation: List[float]) -> float:
        '''
        Count fitness function for floating pointed representation of individual
        :param representation: #TODO fill me
        :return:
        '''
        pass
