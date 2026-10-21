import rclpy
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy
from px4_msgs.msg import OffboardControlMode, TrajectorySetpoint, VehicleCommand

rclpy.init()
node = rclpy.create_node("kalkis")
qos = QoSProfile(depth=1, reliability=ReliabilityPolicy.BEST_EFFORT, durability=DurabilityPolicy.TRANSIENT_LOCAL)
mod_pub = node.create_publisher(OffboardControlMode, "/fmu/in/offboard_control_mode", qos)
hedef_pub = node.create_publisher(TrajectorySetpoint, "/fmu/in/trajectory_setpoint", qos)
komut_pub = node.create_publisher(VehicleCommand, "/fmu/in/vehicle_command", qos)
sayac = 0

def zaman():
    return node.get_clock().now().nanoseconds // 1000

def komut(kod, p1=0.0, p2=0.0):
    komut_pub.publish(VehicleCommand(command=kod, param1=p1, param2=p2, target_system=1, target_component=1,
                                     source_system=1, source_component=1, from_external=True, timestamp=zaman()))

def her_100ms():
    global sayac
    mod_pub.publish(OffboardControlMode(position=True, timestamp=zaman()))
    hedef_pub.publish(TrajectorySetpoint(position=([0.0, 0.0, -5.0] if sayac < 80 else [10.0, 0.0, -5.0]), yaw=0.0, timestamp=zaman()))
    if sayac == 10:
        komut(VehicleCommand.VEHICLE_CMD_DO_SET_MODE, 1.0, 6.0)
        komut(VehicleCommand.VEHICLE_CMD_COMPONENT_ARM_DISARM, 1.0)
        print("Offboard + arm komutu gonderildi")
    sayac += 1

node.create_timer(0.1, her_100ms)
rclpy.spin(node)
