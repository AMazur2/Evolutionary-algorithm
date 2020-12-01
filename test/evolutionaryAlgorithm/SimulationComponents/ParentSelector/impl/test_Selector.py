from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.impl.rouletteParentSelector import \
    rouletteParentSelector
from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.impl.simpleParentSelector import \
    simpleParentSelector
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual import \
    FloatingPointIndividual


def test_select():
    selector = rouletteParentSelector()
    fitness = [0.2, 0.4, 0.5, 0.9]
    population = [FloatingPointIndividual([1, 1, 1]), FloatingPointIndividual([2, 2, 2]),
                  FloatingPointIndividual([3, 3, 3]), FloatingPointIndividual([4, 4, 4])]
    chosen = selector.chooseOne(fitness, 2.0)

    assert chosen < len(fitness)

    marriages = selector.getParents(population, fitness)

    for el in marriages:
        for individual in el:
            assert individual in population

    selector = simpleParentSelector()
    marriages = selector.getParents(population, fitness)

    for el in marriages:
        for individual in el:
            assert individual in population
