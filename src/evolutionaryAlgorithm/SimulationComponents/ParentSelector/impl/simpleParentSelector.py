from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.ParentSelectorInterface \
    import ParentSelectorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual \
    import FloatingPointIndividual


class simpleParentSelector(ParentSelectorInterface):

    def __init__(self):
        pass
    
    def getParents(self, population: List[List[IndividualInterface]]) -> List[List[IndividualInterface]]:
        temporaryPopulation = []
        for el in population:
            marriage = []
            marriage.append(FloatingPointIndividual(el[0].getRepresentation()))
            marriage.append(FloatingPointIndividual(el[1].getRepresentation()))
            temporaryPopulation.append(marriage)

        return temporaryPopulation
