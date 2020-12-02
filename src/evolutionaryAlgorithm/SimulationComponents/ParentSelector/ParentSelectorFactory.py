from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector import ParentSelectorInterface
from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.impl.simpleParentSelector import simpleParentSelector
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface
from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.impl.rouletteParentSelector import \
    rouletteParentSelector


class ParentSelectorFactory(SimulationComponentFactoryInterface):
    @staticmethod
    def validate(config: dict):
        pass

    @staticmethod
    def build(config: dict) -> ParentSelectorInterface:
        parentSelector = config["ParentSelector"]
        if parentSelector["Type"] == "simpleParentSelector":
            return simpleParentSelector()
        elif parentSelector["Type"] == "rouletteParentSelector":
            return rouletteParentSelector()

        else:
            raise NotImplementedError()
