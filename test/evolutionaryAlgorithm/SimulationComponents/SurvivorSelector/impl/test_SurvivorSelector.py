from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual import \
    FloatingPointIndividual
from src.evolutionaryAlgorithm.SimulationComponents.SurviviorSelector.impl.eliteSurvivors import eliteSurvivor


def test_SurvivorSelector():
    selector = eliteSurvivor()
    fitness = [0.2, 0.4, 0.5, 0.9]
    population = [FloatingPointIndividual([1, 1, 1]), FloatingPointIndividual([2, 2, 2])]
    offspring = [FloatingPointIndividual([3, 3, 3]), FloatingPointIndividual([4, 4, 4])]

    temp = [population[0].getRepresentation(), offspring[0].getRepresentation()]

    population[0].setFitnessFunctionEvaluation(fitness[0])
    population[1].setFitnessFunctionEvaluation(fitness[1])
    offspring[0].setFitnessFunctionEvaluation(fitness[2])
    offspring[1].setFitnessFunctionEvaluation(fitness[3])

    survivors = selector.selectSurvivor(population, offspring)
    num = len(survivors)

    assert num == 2

    for el in survivors:
        assert el.getRepresentation() in temp
