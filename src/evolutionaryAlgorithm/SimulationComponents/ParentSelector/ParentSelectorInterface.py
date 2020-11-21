from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface


class ParentSelectorInterface(SimulationComponentInterface):
    
    @abstract
    def marry(self):
        pass
