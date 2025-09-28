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
        shape = [(2.0, 50/n) for n in range(1, 100)]
        for linear, angular in shape:
            msg.linear.x = linear
            msg.angular.z = angular
            self.publisher.publish(msg)
            sleep(0.3)
        

rclpy.init(args=None)
node = Mover()
node.draw()
rclpy.spin(node) 
node.destroy_node() 
rclpy.shutdown()