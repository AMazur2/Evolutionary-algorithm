from src.evolutionaryAlgorithm.EvolutionSimulator import EvolutionSimulator
from src.evolutionaryAlgorithm.EvolutionSimulatorBuilder import EvolutionSimulatorBuilder


def test_create_evolution_simulator_from_dict():
    config = {
        "SimulationName": "testName",
        "WorkingDirectoryPath": "testPath",
        "NumberOfSimulationSteps": 3,
        "Initializator": {
            "Type": "Random",
            "Arguments": {
                "PopulationSize": 10
            }},
        "IndividualRepresentation": {"Type": "FloatingPointRepresentation",
                                     "Arguments": {
                                         "Dimensions": 2,
                                         "Range": {
                                             "Min": -10,
                                             "Max": 10
                                         }
                                     }},
        "FitnessFunction": {"Type": "Weierstrass"},
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
        "SurvivorSelector": {"Type": "eliteSurvivor"},
        "Observers": [{"Type": "MinFitnessFunctionObserver",
                       "Arguments": {
                           "OutputDirectory": "",
                           "OutputFileName": "test.txt"
                       }}]
    }

    evolutionSimulator = EvolutionSimulatorBuilder.createEvolutionSimulatorFromDict(config)

    assert evolutionSimulator.__class__ == EvolutionSimulator
    evolutionSimulator.run()
