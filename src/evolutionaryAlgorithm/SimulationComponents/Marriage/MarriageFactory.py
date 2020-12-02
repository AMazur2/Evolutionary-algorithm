from src.evolutionaryAlgorithm.SimulationComponents.Marriage.impl.simpleMarraige import simpleMarriage
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface
from src.evolutionaryAlgorithm.SimulationComponents.Marriage.MarriageInterface import MarriageInterface


class MarriageFactory(SimulationComponentFactoryInterface):
    @staticmethod
    def validate(config: dict):
        pass

    @staticmethod
    def build(config: dict) -> MarriageInterface:
        marriage = config["Marriage"]
        if marriage["Type"] == "simpleMarriage":
            return simpleMarriage()
        else:
            raise NotImplementedError()
