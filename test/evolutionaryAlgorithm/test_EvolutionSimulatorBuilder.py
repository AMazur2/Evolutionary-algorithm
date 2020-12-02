from src.evolutionaryAlgorithm.EvolutionSimulator import EvolutionSimulator
from src.evolutionaryAlgorithm.EvolutionSimulatorBuilder import EvolutionSimulatorBuilder


def test_create_evolution_simulator_from_dict():
    config = {
        "Initializator": {
            "Type": "Random",
            "Arguments": {
                "PopulationSize": 50
            }},
        "IndividualRepresentation": {"Type": "FloatingPointRepresentation",
                                     "Arguments": {
                                         "Dimensions": 2,
                                         "Range": {
                                             "Min": -10,
                                             "Max": 10
                                         }
                                     }},
        "FitnessFunction": {"Type": "weierstrass"},
        "Recombinator": {"Type": "singlePointRecombinator",
                         "Arguments": {
                             "Probability": 0.85
                         }},
        "Mutator": {"Type": "Gauss",
                    "Arguments": {
                        "Sigma": 1.0,
                        "Probability": 0.1
                    }},
        "ParentSelector": {"Type": "rouletteParentSelector"},
        "SurvivorSelector": {"Type": "rouletteSurvivorSelector"}
    }

    evolutionSimulator = EvolutionSimulatorBuilder.createEvolutionSimulatorFromDict(config)

    assert evolutionSimulator.__class__ == EvolutionSimulator
    evolutionSimulator.run()
