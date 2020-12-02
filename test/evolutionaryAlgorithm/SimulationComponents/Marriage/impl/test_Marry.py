from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual import \
    FloatingPointIndividual
from src.evolutionaryAlgorithm.SimulationComponents.Marriage.impl.simpleMarraige import simpleMarriage


def test_Marry():
    marriage = simpleMarriage()
    population = [FloatingPointIndividual([1, 1, 1]), FloatingPointIndividual([2, 2, 2]),
                  FloatingPointIndividual([5, 5, 5]), FloatingPointIndividual([6, 6, 6])]

    marriages = marriage.marry(population)

    temp = []
    for i in range(4):
        temp.append(population[i].getRepresentation())

    for couple in marriages:
        for individual in couple:
            assert individual.getRepresentation() in temp
