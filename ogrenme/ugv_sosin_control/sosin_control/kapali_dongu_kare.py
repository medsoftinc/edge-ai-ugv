import math
import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


def yaw_hesapla(q):
    return math.atan2(2.0 * (q.w * q.z + q.x * q.y), 1.0 - 2.0 * (q.y * q.y + q.z * q.z))


def aci_farki(hedef, mevcut):
    return math.atan2(math.sin(hedef - mevcut), math.cos(hedef - mevcut))


class KapaliDonguKare(Node):
    KENAR = 2.0                    # m
    HIZ = 0.5                      # m/s
    KP = 1.5                       # P-kontrol katsayısı
    MAX_DONUS = 0.8                # rad/s
    ACI_TOL = math.radians(1.0)    # dönüş hassasiyeti

    def __init__(self):
        super().__init__('kapali_dongu_kare')
        self.pub = self.create_publisher(Twist, '/model/vehicle_blue/cmd_vel', 10)
        self.sub = self.create_subscription(
            Odometry, '/model/vehicle_blue/odometry', self.odom_geldi, 10)
        self.timer = self.create_timer(0.05, self.kontrol)
        self.konum = None
        self.durum = 'BASLA'
        self.kenar = 0
        self.get_logger().info('Kapalı döngü kare: odometri bekleniyor...')

    def odom_geldi(self, m):
        p = m.pose.pose.position
        self.konum = (p.x, p.y, yaw_hesapla(m.pose.pose.orientation))

    def kontrol(self):
        if self.konum is None:
            return
        x, y, yaw = self.konum
        cmd = Twist()

        if self.durum == 'BASLA':
            self.baslangic = (x, y, yaw)
            self.hedef_yon = yaw
            self.kenar_basi = (x, y)
            self.durum = 'ILERI'
            self.get_logger().info(
                f'Başlangıç: x={x:+.2f} y={y:+.2f} yön={math.degrees(yaw):+.1f}°')

        elif self.durum == 'ILERI':
            gidilen = math.hypot(x - self.kenar_basi[0], y - self.kenar_basi[1])
            if gidilen >= self.KENAR:
                self.hedef_yon = aci_farki(self.hedef_yon + math.pi / 2, 0.0)
                self.durum = 'DON'
            else:
                cmd.linear.x = self.HIZ
                cmd.angular.z = self.KP * aci_farki(self.hedef_yon, yaw)

        elif self.durum == 'DON':
            hata = aci_farki(self.hedef_yon, yaw)
            if abs(hata) < self.ACI_TOL:
                self.kenar += 1
                self.get_logger().info(f'Kenar {self.kenar}/4 tamam.')
                if self.kenar == 4:
                    self.durum = 'BITTI'
                    bx, by, byaw = self.baslangic
                    uzaklik = math.hypot(x - bx, y - by) * 100
                    yon_hatasi = math.degrees(aci_farki(yaw, byaw))
                    self.get_logger().info(
                        f'Kare bitti. Başlangıca uzaklık: {uzaklik:.1f} cm, '
                        f'yön hatası: {yon_hatasi:+.1f}°')
                else:
                    self.kenar_basi = (x, y)
                    self.durum = 'ILERI'
            else:
                cmd.angular.z = max(-self.MAX_DONUS, min(self.MAX_DONUS, self.KP * hata))

        self.pub.publish(cmd)


def main():
    rclpy.init()
    node = KapaliDonguKare()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    node.destroy_node()
    rclpy.try_shutdown()
