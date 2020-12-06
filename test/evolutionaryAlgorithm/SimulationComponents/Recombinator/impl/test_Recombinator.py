from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.FitnessFunctionQuadratic import \
    FitnessFunctionQuadratic
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividualFactory import \
    FloatingPointIndividualFactory
from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.impl.averageRecombinator import \
    averageRecombinator
from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.impl.signlePointRecombinator import \
    singlePointRecombinator
from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.impl.twoPointRecombination import \
    twoPointRecombinator


def test_Recombinator():
    factory = FloatingPointIndividualFactory(FitnessFunctionQuadratic())
    marriages = [[factory.getIndividual([1, 2, 3, 4]), factory.getIndividual([5, 6, 7, 8])]]
    recombinator = singlePointRecombinator(1.0)
    childrens = recombinator.recombine(marriages)

    sum = 0
    for el in childrens:
        temp = el.getRepresentation()
        for i in range(len(temp)):
            sum = sum + temp[i]

    assert sum == 36

    recombinator = twoPointRecombinator(1.0)
    childrens = recombinator.recombine(marriages)

    sum = 0
    for el in childrens:
        temp = el.getRepresentation()
        for i in range(len(temp)):
            sum = sum + temp[i]

    assert sum == 36

    recombinator = averageRecombinator(1.0)
    children = recombinator.subcross(marriages[0], 0.5)
    assert children.getRepresentation() == [3, 4, 5, 6]

    childrens = recombinator.recombine(marriages)
    for children in childrens:
        for i in range(2):
            assert children.getRepresentation() != marriages[0][i].getRepresentation()
