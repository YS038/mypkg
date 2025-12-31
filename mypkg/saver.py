import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    node.get_logger().info("Listen: %d" % msg.data)
    with open("log.txt", "a") as f:
        f.write(str(msg.data) + "\n")

def main():
    global node
    rclpy.init()
    node = Node("saver")
    sub = node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

