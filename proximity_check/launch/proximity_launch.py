from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='proximity_check',
            namespace='',
            executable='proximity_check',
            name='AAAarrrgh_gonna_hit_something'
        ),
    ])