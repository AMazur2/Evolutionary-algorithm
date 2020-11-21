from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface


class MutatorFactory(SimulationComponentFactoryInterface):
    @staticmethod
    def validate(config: dict):
        pass

    @staticmethod
    def build(config: dict) -> InitializatorInterface:
        mutator = config["Mutator"]
        if mutator["Type"] == "Gauss":
            return GaussMutator(mutator["Arguments"]["Sigma"])

        else:
            raise NotImplementedError()
