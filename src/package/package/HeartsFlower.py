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
        #self.timer = self.create_timer(7, self.draw) 

    def draw(self):
        for _ in range(7):
            msg = Twist()
            shape = [(0, 0.75), (1.8, 0), (2, 3.14 + 1.507-0.75), (0, 3.14), (2, 3.14 + 1.507-0.75), (1.8, 0), (0, 0)]
            for linear, angular in shape:
                msg.linear.x = float(linear)
                msg.angular.z = float(angular)
                self.publisher.publish(msg)
                sleep(1)
            sleep(7)
            

rclpy.init(args=None)
node = Mover()
node.draw()
rclpy.spin(node) 
node.destroy_node() 
rclpy.shutdown()