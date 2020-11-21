from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface


class MutatorInterface(SimulationComponentInterface):
    
    @abstractmethod
    def mutate(self):
        pass
