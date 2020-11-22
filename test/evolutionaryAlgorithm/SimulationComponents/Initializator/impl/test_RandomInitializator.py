from src.evolutionaryAlgorithm.SimulationComponents.Initializator.impl.RandomInitializator import RandomInitializator


def test_initialize():
    ri = RandomInitializator(populationSize=10, dimensions=5, rangeMin=0, rangeMax=2)
    out = ri.initialize()
    assert len(out) == 10
    assert len(out[0].getRepresentation()) == 5
    # TODO add more tests
