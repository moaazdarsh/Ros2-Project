#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from time import sleep

class Mover(Node): 
    def __init__(self): 
        super().__init__('Mover')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(10, self.draw) 

    def draw(self):
        msg = Twist()
        shape = [(0, -0.7), (7, 6.283), (0, -1.57), (1, 0), (0, -3.1415), (4,0)]
        for linear, angular in shape:
            msg.linear.x = float(linear)
            msg.angular.z = float(angular)
            self.publisher.publish(msg)
            sleep(1)
        

rclpy.init(args=None)
node = Mover()
node.draw()
rclpy.spin(node) 
node.destroy_node() 
rclpy.shutdown()