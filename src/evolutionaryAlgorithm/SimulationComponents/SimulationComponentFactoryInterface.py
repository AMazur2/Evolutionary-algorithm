import abc


class SimulationComponentFactoryInterface():

    @staticmethod
    @abc.abstractmethod
    def validate(config: dict):
        pass

    @staticmethod
    @abc.abstractmethod
    def build(config: dict):
        pass
