from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.FitnessFunctionQuadratic import \
    FitnessFunctionQuadratic
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividualFactory import \
    FloatingPointIndividualFactory
from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.impl.rouletteParentSelector import \
    rouletteParentSelector
from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.impl.simpleParentSelector import \
    simpleParentSelector


def test_select():
    factory = FloatingPointIndividualFactory(FitnessFunctionQuadratic())
    selector = rouletteParentSelector()
    population = [factory.getIndividual([1, 1, 1]), factory.getIndividual([2, 2, 2]),
                  factory.getIndividual([3, 3, 3]), factory.getIndividual([4, 4, 4])]
    fitness = []
    for el in population:
        fitness.append(el.getEvaluation())

    maximum = 0
    for el in fitness:
        if maximum < el:
            maximum = el

    chosen = selector.chooseOne(population, fitness, maximum)

    assert chosen in population

    marriages = selector.getParents(population)

    for el in marriages:
        for individual in el:
            assert individual in population

    selector = simpleParentSelector()
    marriages = selector.getParents(population)

    for el in marriages:
        for individual in el:
            assert individual in population
