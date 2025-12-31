import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def main():
    rclpy.init()
    node = Node("talker")
    pub = node.create_publisher(Int16, "countup", 10)

    count = 1
    while rclpy.ok() and count <= 20:
        msg = Int16()
        msg.data = count
        node.get_logger().info("Publish: %d" % count)
        pub.publish(msg)
        count += 1
        rclpy.spin_once(node, timeout_sec=0.2)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

