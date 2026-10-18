import math
import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from geometry_msgs.msg import Twist


class AcikDonguKare(Node):
    HIZ = 0.5          # m/s
    DONUS_HIZI = 0.5   # rad/s
    KENAR = 2.0        # m
    DT = 0.1           # s

    def __init__(self):
        super().__init__('acik_dongu_kare')
        self.pub = self.create_publisher(Twist, '/model/vehicle_blue/cmd_vel', 10)
        ileri_adim = int(self.KENAR / self.HIZ / self.DT)
        donus_adim = int((math.pi / 2) / self.DONUS_HIZI / self.DT)
        self.plan = (['ileri'] * ileri_adim + ['don'] * donus_adim) * 4
        self.adim = 0
        self.timer = self.create_timer(self.DT, self.gonder)
        self.get_logger().info('Açık döngü kare: 4 x 2 m.')

    def gonder(self):
        mesaj = Twist()
        if self.adim < len(self.plan):
            if self.plan[self.adim] == 'ileri':
                mesaj.linear.x = self.HIZ
            else:
                mesaj.angular.z = self.DONUS_HIZI
        elif self.adim == len(self.plan):
            self.get_logger().info('Kare tamamlandı.')
        self.pub.publish(mesaj)
        self.adim += 1


def main():
    rclpy.init()
    node = AcikDonguKare()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    node.destroy_node()
    rclpy.try_shutdown()
