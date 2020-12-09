from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividualFactory import \
    FloatingPointIndividualFactory
from src.evolutionaryAlgorithm.helpfunctions import getPartners


def test_get_partners():
    FloatingPointIndividualFactory.createFactory("FitnessFunctionQuadratic", True)
    factory = FloatingPointIndividualFactory.getFactory()
    population = [factory.getIndividual([i, i]) for i in range(4)]
    population = getPartners(population)
    assert population[0].getPartner() == population[1]
    assert population[1].getPartner() == population[0]
    assert population[2].getPartner() == population[3]
    assert population[3].getPartner() == population[2]
