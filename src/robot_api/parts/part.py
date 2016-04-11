from abc import ABCMeta, abstractproperty


class Part(object):
    __metaclass__ = ABCMeta

    def __init__(self, robot_name, name, configuration):
        # Check if the name is a string
        if not isinstance(name, str):
            raise Exception("The part name should be a string")

        self._name = name

        # Check if the configuration is a dictionary
        if not isinstance(configuration, dict):
            raise Exception("The part configuration should be a dictionary")

        self._configuration = configuration

    @abstractproperty
    def connection_information(self):
        pass

    @property
    def name(self):
        return self._name

    @property
    def configuration(self):
        return self._configuration
