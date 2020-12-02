from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction import FitnessFunctionInterface
from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.weierstrass import weierstrass
from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.expandedSchaffers import expandedSchaffers
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface


class FitnessFunctionFactory(SimulationComponentFactoryInterface):
    @staticmethod
    def validate(config: dict):
        pass

    @staticmethod
    def build(config: dict) -> FitnessFunctionInterface:

        fitnessFunction = config["FitnessFunction"]
        if fitnessFunction["Type"] == "weierstrass":
            return weierstrass()
        elif fitnessFunction["Type"] == "expandedSchaffers":
            return expandedSchaffers()
        else:
            raise NotImplementedError()
