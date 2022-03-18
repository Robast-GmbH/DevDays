import math
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan
from rclpy.qos import QoSProfile, QoSReliabilityPolicy

class LidarDrive(Node):

    def __init__(self):
        #namen
        super().__init__('lidardrive')

        self.MODE_DRIVE = 0
        self.MODE_TURN = 1

        self.mode = self.MODE_DRIVE


        #publisher
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

        # subscriber
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.lidar_callback,
            QoSProfile(depth=10, reliability=QoSReliabilityPolicy.BEST_EFFORT))

        # reset vel
        self.resetMsg = Twist()
        self.resetMsg.linear = Vector3()
        self.resetMsg.angular = Vector3()

        self.publisher_.publish(self.resetMsg)

        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        self.i += 1

    def lidar_callback(self, msg: LaserScan):
        print(f"Mode: {self.mode}")

        if self.mode == self.MODE_DRIVE:
            self.publisher_.publish(Twist(linear=Vector3(x = 0.5), angular=Vector3()))
            for i in range(10):
                # wenn er nur noch 50cm platz hat...
                if msg.ranges[len(msg.ranges) - i - 1] < 1 or msg.ranges[i] < 1:
                    # drehen starten
                    self.mode = self.MODE_TURN
                    

        elif self.mode == self.MODE_TURN:

            self.publisher_.publish(Twist(linear=Vector3(), angular=Vector3(z=0.2)))

            longest = max(msg.ranges)

            if math.isinf(longest):
                longest = 3.4

            diff = longest - msg.ranges[0]
            if abs(diff) < 0.05 or math.isinf(msg.ranges[0]):
                self.mode = self.MODE_DRIVE


def main(args=None):
    rclpy.init(args=args)
    lidardrive = LidarDrive()
    rclpy.spin(lidardrive)
    lidardrive.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
