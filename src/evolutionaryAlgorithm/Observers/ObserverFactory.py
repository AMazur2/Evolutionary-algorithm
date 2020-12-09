import os
from pathlib import Path

from src.evolutionaryAlgorithm.Observers.impl.MinFitnessFunctionObserver import MinFitnessFunctionObserver


class ObserverFactory():

    @staticmethod
    def validate(config: dict):
        pass

    @staticmethod
    def build(observer_config: dict, workingDirectoryPath: str, simulationName: str):
        dir_path = os.path.join(workingDirectoryPath, simulationName, observer_config["Arguments"]["OutputDirectory"])
        if observer_config["Type"] == "MinFitnessFunctionObserver":
            Path(workingDirectoryPath).mkdir(exist_ok=True)
            Path(os.path.join(workingDirectoryPath, simulationName)).mkdir(exist_ok=True)
            Path(dir_path).mkdir(exist_ok=True)
            return MinFitnessFunctionObserver(
                path=os.path.join(dir_path, observer_config["Arguments"][
                    "OutputFileName"]))
        elif observer_config["Type"] == "AverageAndDeviationObserver":
            Path(workingDirectoryPath).mkdir(exist_ok=True)
            Path(os.path.join(workingDirectoryPath, simulationName)).mkdir(exist_ok=True)
            Path(dir_path).mkdir(exist_ok=True)
            return AverageAndDeviationObserver(pathAverage=os.path.join(dir_path, observer_config["Arguments"][
                "OutputFileName"][0]), pathDeviation=os.path.join(dir_path, observer_config["Arguments"][
                "OutputFileName"][1]))
        else:
            raise NotImplementedError()
