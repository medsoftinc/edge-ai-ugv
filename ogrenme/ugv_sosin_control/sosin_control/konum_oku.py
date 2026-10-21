import math
import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from nav_msgs.msg import Odometry


def yaw_hesapla(q):
    return math.atan2(2.0 * (q.w * q.z + q.x * q.y), 1.0 - 2.0 * (q.y * q.y + q.z * q.z))


class KonumOku(Node):
    def __init__(self):
        super().__init__('konum_oku')
        self.sub = self.create_subscription(
            Odometry, '/model/vehicle_blue/odometry', self.konum_geldi, 10)

    def konum_geldi(self, mesaj):
        p = mesaj.pose.pose.position
        yon = math.degrees(yaw_hesapla(mesaj.pose.pose.orientation))
        self.get_logger().info(
            f'x = {p.x:+.2f} m   y = {p.y:+.2f} m   yön = {yon:+.1f}°',
            throttle_duration_sec=1.0)


def main():
    rclpy.init()
    node = KonumOku()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    node.destroy_node()
    rclpy.try_shutdown()
