from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface
from src.evolutionaryAlgorithm.SimulationComponents.SurviviorSelector.impl.eliteSurvivors import \
    eliteSurvivor


class SurviviorSelectorFactory(SimulationComponentFactoryInterface):

    @staticmethod
    def build(config: dict):
        parentSelector = config["SurvivorSelector"]
        if parentSelector["Type"] == "eliteSurvivor":
            return eliteSurvivor()
        else:
            raise NotImplementedError()

    @staticmethod
    def validate(config: dict):
        pass
