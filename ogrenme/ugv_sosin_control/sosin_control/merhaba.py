import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException


class MerhabaNode(Node):
    def __init__(self):
        super().__init__('merhaba')
        self.sayac = 0
        self.timer = self.create_timer(1.0, self.kalp_atisi)
        self.get_logger().info('Sosın çevrimiçi.')

    def kalp_atisi(self):
        self.sayac += 1
        self.get_logger().info(f'Kalp atışı #{self.sayac}')


def main():
    rclpy.init()
    node = MerhabaNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    node.destroy_node()
    rclpy.try_shutdown()
