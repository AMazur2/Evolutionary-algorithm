from src.evolutionaryAlgorithm.SimulationComponents.Initializator.InitializatorInerface import InitializatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface


class MutatorFactory(SimulationComponentFactoryInterface):
    @staticmethod
    def validate(config: dict):
        pass

    @staticmethod
    def build(config: dict) -> InitializatorInterface:
        pass
