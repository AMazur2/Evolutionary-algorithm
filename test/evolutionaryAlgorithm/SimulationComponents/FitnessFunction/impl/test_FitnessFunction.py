from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.weierstrass import weierstrass
from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.expandedSchaffers import expandedSchaffers
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual import \
    FloatingPointIndividual

def test_evaluate():
    x = [FloatingPointIndividual([1.0, 0.5, 3.0])]
    temp = x[0].getFitnessFunctionEvaluation()
    evaluation = weierstrass()
    evaluation.evaluate(x)

    assert temp != x[0].getFitnessFunctionEvaluation()

    y = [FloatingPointIndividual([-0.4, -2.4, 5.6])]
    temp = y[0].getFitnessFunctionEvaluation()
    evaluation = expandedSchaffers()
    evaluation.evaluate(y)

    assert temp != y[0].getFitnessFunctionEvaluation()
