from src.evolutionaryAlgorithm.SimulationComponents.Initializator.InitializatorInerface import InitializatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Mutator import MutatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Mutator.impl.GaussMutator import GaussMutator
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface


class MutatorFactory(SimulationComponentFactoryInterface):
    @staticmethod
    def validate(config: dict):
        pass

    @staticmethod
    def build(config: dict) -> MutatorInterface:

        mutator = config["Mutator"]
        if mutator["Type"] == "Gauss":
            return GaussMutator(mutator["Arguments"]["Sigma"], mutator["Arguments"]["Probability"])
        else:
            raise NotImplementedError()
