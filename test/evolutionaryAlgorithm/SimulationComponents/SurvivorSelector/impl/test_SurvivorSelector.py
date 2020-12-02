from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual import \
    FloatingPointIndividual
from src.evolutionaryAlgorithm.SimulationComponents.SurviviorSelector.impl.eliteSurvivors import eliteSurvivor


def test_SurvivorSelector():
    selector = eliteSurvivor()
    fitness = [0.2, 0.4, 0.5, 0.9]
    population = [[FloatingPointIndividual([1, 1, 1]), FloatingPointIndividual([2, 2, 2])],
                  [FloatingPointIndividual([5, 5, 5]), FloatingPointIndividual([6, 6, 6])]]
    offspring = [[FloatingPointIndividual([3, 3, 3]), FloatingPointIndividual([4, 4, 4])],
                 [FloatingPointIndividual([7, 7, 7]), FloatingPointIndividual([8, 8, 8])]]

    temp = [population[0][0].getRepresentation(), population[0][1].getRepresentation(),
            offspring[0][0].getRepresentation(), offspring[0][1].getRepresentation()]

    for i in range(2):
        for j in range(2):
            population[i][j].setFitnessFunctionEvaluation(fitness[i])

    for i in range(2):
        for j in range(2):
            offspring[i][j].setFitnessFunctionEvaluation(fitness[i+2])

    survivors = selector.selectSurvivor(population, offspring)
    num = len(survivors)

    assert num == 2

    for el in survivors:
        for i in range(2):
            assert el[i].getRepresentation() in temp
