from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface


class SurviviorSelectorFactory(SimulationComponentFactoryInterface):

    @staticmethod
    def build(config: dict):  # TODO: implement me
        pass
    #     if (config["survivor_type"] == "simplesurvivor"):
    #         return SimpleSurvivor(...)
    #     elif (config["survivor_type"] == "complexsurvivor"):
    #         return ComplexSurvivor(...)
