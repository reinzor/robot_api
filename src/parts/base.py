import rospy
from geometry_msgs.msg import Twist

from part import Part


class Base(Part):

    def __init__(self, robot_name, name, configuration={}):
        super(Base, self).__init__(robot_name, name, configuration)

        # Create ROS Connections
        self._cmd_vel_publisher = rospy.Publisher("/%s/%s/cmd_vel" % (robot_name, name), Twist, queue_size=20)

    @property
    def connection_information(self):
        return {
            self._cmd_vel_publisher.name : self._cmd_vel_publisher.type
        }

    def send_cmd_vel(self, vx, vth):
        self._publish_2d_twist_message(vx, 0, vth)

    def send_goal(self, x, t, th, frame_id="/map"):
        rospy.logwarn("This function is not yet implemented")
        pass

    def _publish_2d_twist_message(self, vx, vy, vth):
        msg = Twist()
        msg.linear.x = vx
        msg.linear.y = vy
        msg.angular.z = vth

        self._cmd_vel_publisher.publish(msg)
