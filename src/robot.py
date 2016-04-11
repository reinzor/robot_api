import rospy, sys
from parts.part import Part


class Robot(object):

    def __init__(self, name):
        # Store the robot_name
        self._name = name
        self._parts = []

        # Error if we are using a namespace
        ns = rospy.get_namespace()
        if ns != "/":
            rospy.logerr("The robot api instance should not be created within a namespace, exit 1")
            sys.exit(1)

    @property
    def name(self):
        return self._name

    @property
    def connection_information(self):
        return {part.name: part.connection_information for part in self._parts}

    def _setup_part(self, part_class, part_name, part_configuration={}):
        # Check if the part_class inherits from class
        if not issubclass(part_class, Part):
            raise Exception("Part %s (%s) does not inherit from Part" % (part_name, part_class))

        # Construct the part
        try:
            part = part_class(self._name, part_name, part_configuration)
        except Exception as e:
            raise Exception("Failed to setup part '%s': %s" % (part_name, e))

        setattr(self, part_name, part)
        self._parts.append(part)

