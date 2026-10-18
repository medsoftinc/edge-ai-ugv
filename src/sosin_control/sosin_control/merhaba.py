import rclpy
from rclpy.node import Node


class MerhabaNode(Node):
    def __init__(self):
        super().__init__('merhaba')
        self.get_logger().info('Sosın çevrimiçi.')


def main():
    rclpy.init()
    node = MerhabaNode()
    node.destroy_node()
    rclpy.shutdown()
