from part import Part


class Arm(Part):

    def __init__(self, robot_name, name, configuration={}):
        super(Arm, self).__init__(robot_name, name, configuration)

    @property
    def connection_information(self):
        return {}
