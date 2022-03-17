import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class SimplePublisher(Node):

    def __init__(self):
        # erstellt base node mit namen "simple_publisher"
        super().__init__('simple_publisher') 
        # fügt der node einen publisher hinzu, der auf das topic namens "topic" eine nachricht vom typ "String" published
        self.publisher_ = self.create_publisher(String, 'topic', 10) 
        timer_period = 0.5  # seconds
        # kleiner timer, der alle "timer_period" sekunden die angegebene funktion aufruft
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher)
    simple_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
