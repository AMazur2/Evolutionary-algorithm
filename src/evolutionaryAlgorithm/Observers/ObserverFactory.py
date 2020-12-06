import os
from pathlib import Path

from src.evolutionaryAlgorithm.Observers.impl.MinFitnessFunctionObserver import MinFitnessFunctionObserver


class ObserverFactory():

    @staticmethod
    def validate(config: dict):
        pass

    @staticmethod
    def build(observer_config: dict):
        if observer_config["Type"] == "MinFitnessFunctionObserver":
            Path(observer_config["Arguments"]["OutputDirectory"]).mkdir(exist_ok=True)
            return MinFitnessFunctionObserver(
                path=os.path.join(observer_config["Arguments"]["OutputDirectory"], observer_config["Arguments"][
                    "OutputFileName"]))

        else:
            raise NotImplementedError()
