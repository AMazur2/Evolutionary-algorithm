from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual import \
    FloatingPointIndividual


def test_fitness_function_quadratic():
    fpi = FloatingPointIndividual([1, 2])
    assert 5 == fpi.getEvaluation()

    fpi = FloatingPointIndividual([0, 0])
    assert 0 == fpi.getEvaluation()
