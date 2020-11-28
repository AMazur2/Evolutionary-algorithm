from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual import \
    FloatingPointIndividual
from src.evolutionaryAlgorithm.SimulationComponents.Mutator.impl.GaussMutator import GaussMutator


def test_mutate():
    gm = GaussMutator(sigma=1.0)
    offspring = [FloatingPointIndividual([1, 1]), FloatingPointIndividual([0, 0])]
    mutated = gm.mutate(offspring=offspring)

    assert offspring[0].getRepresentation() != mutated[0].getRepresentation()
    assert offspring[1].getRepresentation() != mutated[1].getRepresentation()

    assert offspring[0].getRepresentation() == [1, 1]
