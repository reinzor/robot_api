from parts.part import Part


class Robot(object):

    def __init__(self, name):
        self._name = name

    def get_robot_name(self):
        return self._name

    def _setup_part(self, part_class, part_name, part_configuration={}):
        # Check if the part_class inherits from class
        if not issubclass(part_class, Part):
            raise Exception("Part %s (%s) does not inherit from Part" % (part_name, part_class))

        # Construct the part
        try:
            part = part_class(part_name, part_configuration)
        except Exception as e:
            raise Exception("Failed to setup part '%s': %s" % (part_name, e))

        setattr(self, part_name, part)

