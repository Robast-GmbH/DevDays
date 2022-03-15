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
            package='py_pub',
            namespace='',
            executable='talker',
            name='SachAn'
        ),
    ])