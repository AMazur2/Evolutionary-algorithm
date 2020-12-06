from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividualFactory import \
    FloatingPointIndividualFactory
from src.evolutionaryAlgorithm.SimulationComponents.OtherElementsOnlyValidationReneameMeFactory import \
    OtherElementsOnlyValidationReneameMeFactory


class IndividualFactory(OtherElementsOnlyValidationReneameMeFactory):
    # TODO ensure that this object is not created in simulation builder
    @staticmethod
    def validate(config: dict):
        pass

    @staticmethod
    def build(config: dict):
        individual = config["Individual"]
        if individual["Type"] == "floatingPointIndividual":
            return FloatingPointIndividualFactory(
                config["FitnessFunction"])  # TODO add dispathcer to create fitness funtion corectly

        else:
            raise NotImplementedError()
