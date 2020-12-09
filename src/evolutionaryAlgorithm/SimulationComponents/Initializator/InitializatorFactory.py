from src.evolutionaryAlgorithm.SimulationComponents.Initializator.InitializatorInerface import InitializatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Initializator.impl.RandomInitializator import RandomInitializator
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface


class InitializatorFactory(SimulationComponentFactoryInterface):
    @staticmethod
    def validate(config: dict):
        pass

    @staticmethod
    def build(config: dict) -> InitializatorInterface:
        initializator = config["Initializator"]
        if initializator["Type"] == "Random":
            return RandomInitializator(initializator["Arguments"]["PopulationSize"],
                                       config["IndividualRepresentation"]["Arguments"]["Dimensions"],
                                       config["IndividualRepresentation"]["Arguments"]["Range"]["Min"],
                                       config["IndividualRepresentation"]["Arguments"]["Range"]["Max"])

        else:
            raise NotImplementedError()
