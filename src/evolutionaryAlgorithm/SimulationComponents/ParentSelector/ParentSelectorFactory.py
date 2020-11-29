from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector import ParentSelectorInterface
from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.impl.simpleParentSelector import simpleParentSelector
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface


class ParentSelectorFactory(SimulationComponentFactoryInterface):
    @staticmethod
    def validate(config: dict):
        pass

    @staticmethod
    def build(config: dict) -> ParentSelectorInterface:
        parentSelector = config["ParentSelector"]
        if parentSelector["Type"] == "simpleParentSelector":
            return simpleParentSelector()

        else:
            raise NotImplementedError()
