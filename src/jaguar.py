from robot import Robot
from parts import Arm, Base


class Jaguar(Robot):

    def __init__(self):
        super(self.__class__, self).__init__("jaguar")
        self._setup_part(Arm, "arm")
        self._setup_part(Base, "base")