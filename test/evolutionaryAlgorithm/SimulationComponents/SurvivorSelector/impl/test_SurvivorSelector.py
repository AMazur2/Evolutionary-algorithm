from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual import \
    FloatingPointIndividual
from src.evolutionaryAlgorithm.SimulationComponents.SurviviorSelector.impl.RouletteSurvivorSelector import \
    RouletteSurvivorSelector


def test_SurvivorSelector():
    selector = RouletteSurvivorSelector()
    fitness = [0.2, 0.4, 0.5, 0.9]
    population = [FloatingPointIndividual([1, 1, 1]), FloatingPointIndividual([2, 2, 2]),
                  FloatingPointIndividual([3, 3, 3]), FloatingPointIndividual([4, 4, 4])]
    i = 0
    for el in population:
        el.setFitnessFunctionEvaluation(fitness[i])
        i = i + 1

    survivors = selector.selectSurvivor(population)
    num = len(survivors)

    assert num == 2

    for el in survivors:
        assert el in population