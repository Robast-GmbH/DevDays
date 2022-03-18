from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_sub',
            namespace='',
            executable='listener',
            name='HoerZu'
        ),
        Node(
            package='proximity_check',
            namespace='',
            executable='proximity_check',
            name='AAAarrrgh gonna hit something'
        ),
    ])