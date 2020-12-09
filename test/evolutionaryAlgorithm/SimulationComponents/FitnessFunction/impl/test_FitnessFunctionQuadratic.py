from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.FitnessFunctionQuadratic import \
    FitnessFunctionQuadratic
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividualFactory import \
    FloatingPointIndividualFactory


def test_fitness_function_quadratic():
    factory = FloatingPointIndividualFactory(FitnessFunctionQuadratic(), isModivied=False)
    fpi = factory.getIndividual([1, 2])
    assert 5 == fpi.getEvaluation()

    fpi = factory.getIndividual([0, 0])
    assert 0 == fpi.getEvaluation()
