import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


msg_terminal = """ Reading from keyboard
---------------------------
Use 'WASD' to translate
Use 'QE' to yaw
Press 'Shift' to run """

class teleopPublisher(Node):

    def __init__(self):
        super().__init__('convert_teleop_ros1_to_ros2')
        self.publishers = self.create_publisher(Twist, 'cmd_vel', 1)


def main(args=None):
    rclpy.init(args=args)
    print(msg_terminal)
    teleop_publisher = teleopPublisher()
    rclpy.spin(teleop_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main() #call the main function