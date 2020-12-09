from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.FitnessFunctionQuadratic import \
    FitnessFunctionQuadratic
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividualFactory import \
    FloatingPointIndividualFactory


def test_pair_individuals():
    factory = FloatingPointIndividualFactory(FitnessFunctionQuadratic(), isModivied=True)
    # factory.createFactory()
    a = factory.getIndividual([1, 1])
    b = factory.getIndividual([2, 2])

    test_variable = False
    try:
        a.getEvaluation()
    except Exception:
        # assert Exception
        test_variable = True

    assert test_variable == True

    a.setPartner(b)
    assert a.getEvaluation() == 2.0
    assert b.getEvaluation() == 2.0
