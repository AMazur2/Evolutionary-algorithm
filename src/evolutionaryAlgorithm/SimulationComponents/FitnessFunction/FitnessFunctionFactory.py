from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction import FitnessFunctionInterface
from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.ExpandedSchaffers import ExpandedSchaffers
from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.FitnessFunctionQuadratic import \
    FitnessFunctionQuadratic
from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.Weierstrass import Weierstrass
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface


class FitnessFunctionFactory(SimulationComponentFactoryInterface):
    @staticmethod
    def validate(config: dict):
        pass

    @staticmethod
    def build(config: dict) -> FitnessFunctionInterface:

        fitnessFunction = config["FitnessFunction"]
        if fitnessFunction["Type"] == "Weierstrass":
            return Weierstrass()
        elif fitnessFunction["Type"] == "ExpandedSchaffers":
            return ExpandedSchaffers()
        elif fitnessFunction["Type"] == "FitnessFunctionQuadratic":
            return FitnessFunctionQuadratic()
        else:
            raise NotImplementedError()
