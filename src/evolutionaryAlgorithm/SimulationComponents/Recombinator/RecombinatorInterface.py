from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface


class RecombinatorInterface(SimulationComponentInterface):
    @abstractmethod
    def recombinate(self):
        pass
