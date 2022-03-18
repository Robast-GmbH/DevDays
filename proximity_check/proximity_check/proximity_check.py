from turtle import TurtleScreen
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from rclpy.qos import QoSProfile, QoSReliabilityPolicy


class ProximityChecker(Node):

        isTooClose = False
        turnLeft = False
        turnRight = False

        def __init__(self):
                super().__init__('proximity_check')
                self.subscription = self.create_subscription(
                        LaserScan,
                        'scan',
                        self.listener_callback,
                        QoSProfile(depth=10, reliability=QoSReliabilityPolicy.BEST_EFFORT))
                self.subscription  # prevent unused variable warning

                self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
                timer_period = 0.5  # seconds
                self.timer = self.create_timer(timer_period, self.publisher_callback)


        def listener_callback(self, msg):
                if (msg.ranges[0] < 1.0):
                        self.isTooClose = True
                        if (msg.ranges[89] > 1.0 and msg.ranges[-90] < 1.0):     
                                self.turnLeft = True
                                self.turnRight = False
                        elif (msg.ranges[89] < 1.0 and msg.ranges[-90] > 1.0):
                                self.turnRight = True
                                self.turnLeft = False
                        else:
                                self.turnLeft = True
                else:
                        self.isTooClose = False
                        self.turnLeft = False
                        self.turnRight = False


        def publisher_callback(self):
                msg = Twist()
                if (self.isTooClose):
                        if (self.turnRight):
                                msg.linear.x = 0.0
                                msg.angular.z = -1.0

                        msg.linear.x = 0.0
                        msg.angular.z = 1.0

                else:
                        msg.linear.x = 0.5
                        msg.angular.z = 0.0

                self.publisher_.publish(msg)


def main(args=None):
        rclpy.init(args=args)

        proximity_checker = ProximityChecker()

        rclpy.spin(proximity_checker)

        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        proximity_checker.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()