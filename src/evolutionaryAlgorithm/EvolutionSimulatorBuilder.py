from typing import Dict

from src.evolutionaryAlgorithm.EvolutionSimulator import EvolutionSimulator, ObserverInterface
from src.evolutionaryAlgorithm.Observers.impl.MinFitnessFunctionObserver import MinFitnessFunctionObserver
from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.FitnessFunctionFactory import \
    FitnessFunctionFactory
from src.evolutionaryAlgorithm.SimulationComponents.FitnessFunction.impl.FitnessFunctionQuadratic import \
    FitnessFunctionQuadratic
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividualFactory import \
    FloatingPointIndividualFactory
from src.evolutionaryAlgorithm.SimulationComponents.Initializator.InitializatorFactory import InitializatorFactory
from src.evolutionaryAlgorithm.SimulationComponents.Mutator.MutatorFactory import MutatorFactory
from src.evolutionaryAlgorithm.SimulationComponents.ParentSelector.ParentSelectorFactory import ParentSelectorFactory
from src.evolutionaryAlgorithm.SimulationComponents.Recombinator.RecombinatorFactory import RecombinatorFactory
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface
from src.evolutionaryAlgorithm.SimulationComponents.SurviviorSelector.SurviviorSelectorFactory import \
    SurviviorSelectorFactory


class EvolutionSimulatorBuilder:
    # implementedComponents = {
    #     "Initializator": InitializatorFactory,
    #     ...
    # }
    # simulationComponentsClasses: Dict[str, SimulationComponentInterface] = {
    #     "Initializator": InitializatorInterface,
    #     "Recombinator": RecombinatorInterface,
    #     "Mutator": MutatorInterface,
    #     "ParentSelector": ParentSelectorInterface,
    #     "SurvivorSelector": SurviviorSelectorInterface
    # }

    componentsFactory: Dict[str, SimulationComponentFactoryInterface] = {
        "Initializator": InitializatorFactory,
        "Recombinator": RecombinatorFactory,
        "Mutator": MutatorFactory,
        "ParentSelector": ParentSelectorFactory,
        "SurvivorSelector": SurviviorSelectorFactory,
        "FitnessFunction": FitnessFunctionFactory
    }

    observersFactory: Dict[str, ObserverInterface] = {
        "MinFitnessFunctionObserver": MinFitnessFunctionObserver
    }

    @classmethod
    def createEvolutionSimulatorFromDict(cls, config: dict):
        # componentsFactory = cls.getComponentsFactory(config)

        try:
            for componentFactory in cls.componentsFactory.values():
                componentFactory.validate(
                    config)  # TODO add also validation on OtherElementsOnlyValidationReneameMeFactory elemnents
        except ValueError as err:
            print(f"For component {componentFactory}, parameter is invalid. {err}")

        componentsImpl: Dict[str, SimulationComponentInterface] = {}

        FloatingPointIndividualFactory.createFactory(
            FitnessFunctionQuadratic())  # TODO change argument to this config["FitnessFunction"]

        for componentName, componentFactory in cls.componentsFactory.items():
            componentsImpl[componentName] = componentFactory.build(config)

        observers = []
        for observer in config["Observers"]:  # TODO add observers valdation
            observers.append(cls.observersFactory[observer[
                "Type"]])  # TODO cant pass arguments to observers in this architecture to do this use factory method pattern as in components Factory

        return EvolutionSimulator.fromSimulationComponentList(componentsImpl, observers)

    # @classmethod
    # def getComponentsFactory(cls, config: dict):
    #     componentsFactory = []
    #     try:
    #         for key, component_name in config["SimulationComponents"]:
    #             componentsFactory.append(cls.createComponentFactoryFromName(key, component_name))
    #     except KeyError:
    #         print("Wrong name pass ")  # TODO change error msg
    #
    #     return componentsFactory

    # @classmethod
    # def createComponentFactoryFromName(cls, key, component_name):
    #     if component_name in cls.implementedComponents[key]:
    #         return cls.implementedComponents[key].get(component_name)#TODO thing of this design
    #     else:
    #         raise KeyError(f"{component_name} method not implemented")
