from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.impl.signlePointRecombinator import \
    singlePointRecombinator
from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.impl.twoPointRecombination import \
    twoPointRecombinator
from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.impl.averageRecombinator import \
    averageRecombinator
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual import \
    FloatingPointIndividual


def test_Recombinator():
    marriages = [[FloatingPointIndividual([1, 2, 3, 4]), FloatingPointIndividual([5, 6, 7, 8])]]
    recombinator = singlePointRecombinator(1.0)
    childrens = recombinator.recombine(marriages)

    for children in childrens:
        for j in range(2):
            assert children.getRepresentation() != marriages[0][j].getRepresentation()

    recombinator = twoPointRecombinator(1.0)
    childrens = recombinator.recombine(marriages)

    for children in childrens:
        for i in range(2):
            assert children.getRepresentation() != marriages[0][i].getRepresentation()

    recombinator = averageRecombinator(1.0)
    children = recombinator.subcross(marriages[0], 0.5)
    assert children.getRepresentation() == [3, 4, 5, 6]

    childrens = recombinator.recombine(marriages)
    for children in childrens:
        for i in range(2):
            assert children.getRepresentation() != marriages[0][i].getRepresentation()
