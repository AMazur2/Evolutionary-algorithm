import abc


class OtherElementsOnlyValidationReneameMeFactory():  # TODO rename me (im not factory im validator)

    @staticmethod
    @abc.abstractmethod
    def validate(config: dict):
        pass
