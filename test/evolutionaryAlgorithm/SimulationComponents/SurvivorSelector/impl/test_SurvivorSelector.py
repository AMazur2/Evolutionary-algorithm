from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.FitnessFunctionQuadratic import \
    FitnessFunctionQuadratic
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividualFactory import \
    FloatingPointIndividualFactory
from src.evolutionaryAlgorithm.SimulationComponents.SurviviorSelector.impl.eliteSurvivor import eliteSurvivor


def test_SurvivorSelector():

    factory = FloatingPointIndividualFactory(FitnessFunctionQuadratic())

    population = [factory.getIndividual([1, 1, 1]), factory.getIndividual([2, 2, 2]),
                  factory.getIndividual([3, 3, 3]), factory.getIndividual([4, 4, 4])]

    offspring = [factory.getIndividual([5, 5, 5]), factory.getIndividual([6, 6, 6]),
                 factory.getIndividual([7, 7, 7]), factory.getIndividual([8, 8, 8])]

    temporary = []
    for el in population:
        temporary.append(el.getRepresentation())

    for el in offspring:
        temporary.append(el.getRepresentation())

    selector = eliteSurvivor()
    survivors = selector.selectSurvivor(population, offspring)

    num = len(survivors)

    assert num == 4

    for el in survivors:
        assert el.getRepresentation() in temporary
