from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.impl.rouletteParentSelector import \
    rouletteParentSelector
from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.impl.simpleParentSelector import \
    simpleParentSelector
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual import \
    FloatingPointIndividual
from src.evolutionaryAlgorithm.SimulationComponents.Marriage.impl.simpleMarraige import simpleMarriage


def test_select():
    selector = rouletteParentSelector()
    fitness = [0.2, 0.4, 0.5, 0.9]
    population = [FloatingPointIndividual([1, 1, 1]), FloatingPointIndividual([2, 2, 2]),
                  FloatingPointIndividual([3, 3, 3]), FloatingPointIndividual([4, 4, 4])]
    i = 0
    for el in population:
        el.setFitnessFunctionEvaluation(fitness[i])
        i = i + 1

    fitnessPrim = [fitness[0], fitness[2]]
    marriage = simpleMarriage()
    newPopulation = marriage.marry(population)
    chosen = selector.chooseOne(fitnessPrim, 0.7)

    assert chosen < 2

    marriages = selector.getParents(newPopulation)

    temp = []
    for i in range(len(newPopulation)):
        for j in range(2):
            temp.append(newPopulation[i][j].getRepresentation())
    for el in marriages:
        for individual in el:
            assert individual.getRepresentation() in temp

    selector = simpleParentSelector()
    marriages = selector.getParents(newPopulation)

    temp = []
    for i in range(len(newPopulation)):
        temp.append(newPopulation[i][0].getRepresentation())
        temp.append(newPopulation[i][1].getRepresentation())
    for el in marriages:
        for i in range(2):
            assert el[i].getRepresentation() in temp
