from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface
from src.evolutionaryAlgorithm.SimulationComponents.SurviviorSelector.impl.RouletteSurvivorSelector import \
    RouletteSurvivorSelector


class SurviviorSelectorFactory(SimulationComponentFactoryInterface):

    @staticmethod
    def build(config: dict):
        parentSelector = config["SurvivorSelector"]
        if parentSelector["Type"] == "RouletteSurvivorSelector":
            return RouletteSurvivorSelector
        else:
            raise NotImplementedError()

    @staticmethod
    def validate(config: dict):
        pass
