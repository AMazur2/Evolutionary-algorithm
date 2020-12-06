from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.FitnessFunctionQuadratic import \
    FitnessFunctionQuadratic
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividualFactory import \
    FloatingPointIndividualFactory
from src.evolutionaryAlgorithm.SimulationComponents.Mutator.impl.GaussMutator import GaussMutator


def test_mutate():
    gm = GaussMutator(sigma=1.0, probabilityOfMutation=1.0)
    factory = FloatingPointIndividualFactory(FitnessFunctionQuadratic())
    offspring = [factory.getIndividual([1, 1]), factory.getIndividual([0, 0])]
    mutated = gm.mutate(offspring=offspring)

    assert offspring[0].getRepresentation() == [1, 1]

    assert offspring[0].getRepresentation() != mutated[0].getRepresentation()
    assert offspring[1].getRepresentation() != mutated[1].getRepresentation()
