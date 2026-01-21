#!/usr/bin/python3
# SPDX-FileCopyrightText:2025 YS038
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

count = 0
total = 0

def cb(msg):
    global count, total
    count += 1
    total += msg.data

    with open("mylog.csv", "a") as f:
        f.write(f"{count},{msg.data},{total}\n")

    print(f"received={msg.data}, count={count}, total={total}")

def main():
    rclpy.init()
    node = Node("logger")
    node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

