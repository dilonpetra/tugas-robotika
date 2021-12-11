from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='convert_teleop_ros1_to_ros2',
            executable='convert_teleop_ros1_to_ros2',
            output='screen'),
    ])
