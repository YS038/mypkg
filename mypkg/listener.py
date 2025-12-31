import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    node.get_logger().info("listen:%d" % msg.data)

def main():
    global node
    rclpy.init()
    node = Node("listener")
    sub = node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

