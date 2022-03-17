from example_interfaces.srv import PrintName

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(PrintName, 'name', self.process_name)

    def process_name(self, request, response):
        response.message = "herzlichen glückwunsch " + request.name
        self.get_logger().info('Incoming request\na: %s' % (request.name))

        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()