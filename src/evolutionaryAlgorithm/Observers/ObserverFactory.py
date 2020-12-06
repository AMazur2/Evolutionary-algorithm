import os

from src.evolutionaryAlgorithm.Observers.impl.MinFitnessFunctionObserver import MinFitnessFunctionObserver


class ObserverFactory():

    @staticmethod
    def validate(config: dict):
        pass

    @staticmethod
    def build(observer_config: dict):
        if observer_config["Type"] == "MinFitnessFunctionObserver":
            os.mkdir(observer_config["Arguments"]["OutputDirectory"])
            return MinFitnessFunctionObserver(
                path=os.path.join(observer_config["Arguments"]["OutputDirectory"], observer_config["Arguments"][
                    "OutputFileName"]))

        else:
            raise NotImplementedError()
