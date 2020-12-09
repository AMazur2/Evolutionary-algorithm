from src.evolutionaryAlgorithm.SimulationComponents.Recombinator import RecombinatorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.impl.averageRecombinator import averageRecombinator
from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.impl.signlePointRecombinator import \
    singlePointRecombinator
from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.impl.twoPointRecombination import twoPointRecombinator
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface


class RecombinatorFactory(SimulationComponentFactoryInterface):
    @staticmethod
    def validate(config: dict):
        pass

    @staticmethod
    def build(config: dict) -> RecombinatorInterface:
        recombinator = config["Recombinator"]
        if recombinator["Type"] == "singlePointRecombinator":
            return singlePointRecombinator(recombinator["Arguments"]["Probability"])
        elif recombinator["Type"] == "twoPointRecombinator":
            return twoPointRecombinator(recombinator["Arguments"]["Probability"])
        elif recombinator["Type"] == "averageRecombinator":
            return averageRecombinator(recombinator["Arguments"]["Probability"])

        else:
            raise NotImplementedError()
