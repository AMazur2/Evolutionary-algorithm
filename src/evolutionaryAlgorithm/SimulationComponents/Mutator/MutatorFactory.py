from src.evolutionaryAlgorithm.SimulationComponents.Mutator.impl.GaussMutator import GaussMutator
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface
from src.evolutionaryAlgorithm.SimulationComponents.Mutator.MutatorInterface import MutatorInterface


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
