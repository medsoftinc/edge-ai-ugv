import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from geometry_msgs.msg import Twist


class IleriGit(Node):
    def __init__(self):
        super().__init__('ileri_git')
        self.pub = self.create_publisher(Twist, '/model/vehicle_blue/cmd_vel', 10)
        self.adim = 0
        self.timer = self.create_timer(0.1, self.gonder)
        self.get_logger().info('İleri: 0.5 m/s, 5 saniye.')

    def gonder(self):
        mesaj = Twist()
        if self.adim < 50:
            mesaj.linear.x = 0.5
        elif self.adim == 50:
            self.get_logger().info('Durdu.')
        self.pub.publish(mesaj)
        self.adim += 1


def main():
    rclpy.init()
    node = IleriGit()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    node.destroy_node()
    rclpy.try_shutdown()
