from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividualFactory import \
    FloatingPointIndividualFactory


def test_FloatingPointIndividualFactory():
    # FloatingPointIndividualFactory.createFactory("FitnessFunctionQuadratic", isModivied = True)
    factory = FloatingPointIndividualFactory.getFactory()

    # assert factory.fitnessFunction == FitnessFunctionQuadratic()
    assert factory.isModivied == True
