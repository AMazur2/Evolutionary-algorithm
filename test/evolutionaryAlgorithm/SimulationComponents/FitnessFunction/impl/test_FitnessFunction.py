from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.ExpandedSchaffers import ExpandedSchaffers
from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.Weierstrass import Weierstrass
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividualFactory import \
    FloatingPointIndividualFactory


def test_weierstreass_fitness_function():
    factory = FloatingPointIndividualFactory(Weierstrass(), isModivied=False)
    x = [factory.getIndividual([0, 0])]
    eveluation = x[0].getEvaluation()

    assert eveluation == 0


def test_weierstreass_extended_fitness_function():
    factory = FloatingPointIndividualFactory(ExpandedSchaffers(), isModivied=False)
    x = [factory.getIndividual([0, 0])]
    eveluation = x[0].getEvaluation()

    assert eveluation == 0
