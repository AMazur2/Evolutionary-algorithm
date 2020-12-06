import json

from src.evolutionaryAlgorithm.EvolutionSimulatorBuilder import EvolutionSimulatorBuilder

if __name__ == '__main__':
    configFile = "config.json"

    with open(configFile, 'r') as f:
        config = json.load(f)

    evolutionSimulator = EvolutionSimulatorBuilder.createEvolutionSimulatorFromDict(config)

    evolutionSimulator.run()
