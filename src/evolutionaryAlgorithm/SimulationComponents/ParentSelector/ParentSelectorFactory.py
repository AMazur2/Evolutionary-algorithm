from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface


class ParentSelectorFactory(SimulationComponentFactoryInterface):
    @staticmethod
    def validate(config: dict):
        pass

    @staticmethod
    def build(config: dict) -> InitializatorInterface:
        parentSelector = config["ParentSelector"]
        if parentSelector["Type"] == "simpleParentSelector":
            return simpleParentSelector()

        else:
            raise NotImplementedError()
