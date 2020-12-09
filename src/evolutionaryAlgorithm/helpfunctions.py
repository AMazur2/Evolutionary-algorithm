from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface


def getPartners(population: List[IndividualInterface]):
    if len(population) % 2 is not 0:
        raise Exception("Population isn't dividable by 2")

    for indyvidual1 in population:
        if not indyvidual1.havePartner():
            for indyvidual2 in population:
                if not indyvidual2.havePartner() and indyvidual1 is not indyvidual2:
                    indyvidual1.setPartner(indyvidual2)
                    break;

    for indyvidual in population:
        if not indyvidual.havePartner():
            raise Exception("Not everyone have pair")
        if indyvidual.getPartner() == indyvidual:
            raise Exception("indyvidual is in pair with itself")
    return population
