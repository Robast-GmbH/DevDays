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

        # start driving
        msg = Twist()
        msg.linear = Vector3(x = 0.5)
        self.publisher_.publish(msg)

        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        self.i += 1

    def lidar_callback(self, msg: LaserScan):

        for i in range(10):
            if msg.ranges[len(msg.ranges) - i - 1] < 0.5 or msg.ranges[i] < 0.5:
                self.publisher_.publish(self.resetMsg)



def main(args=None):
    rclpy.init(args=args)
    lidardrive = LidarDrive()
    rclpy.spin(lidardrive)
    lidardrive.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
