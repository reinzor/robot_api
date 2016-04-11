from robot_api import Robot
from robot_api.parts import Arm, Base


class Jaguar(Robot):

    def __init__(self):
        super(self.__class__, self).__init__("jaguar")
        self.add_part(Arm, "arm")
        self.add_part(Base, "base")
