import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    with open("/home/yui31/mylogs/mylog.csv", "a") as f:
        f.write(str(msg.data) + "\n")
    print("Listen:", msg.data)

def main():
    rclpy.init()
    node = Node("saver")
    sub = node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

