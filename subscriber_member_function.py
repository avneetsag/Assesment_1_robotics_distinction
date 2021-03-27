# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
import datetime
from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.publisher_ = self.create_publisher(String, '/clock/setalarm', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.m = datetime.datetime.now()
        self.subscription = self.create_subscription(
            String,
            '/clock/alarm',
            self.listener_callback,
            10)

    def timer_callback(self):
        msg = String()
        self.var_a = '12'
        self.var_b = '9'
        self.var_c = '50'
        self.var_d = '2021'
        self.var_f = '3'
        self.var_g = '27'
        msg.data = '%s-%s-%s %s:%s:%s' % (self.var_d,self.var_f,self.var_g, self.var_a, self.var_b, self.var_c)
        self.publisher_.publish(msg)
        self.get_logger().info('Alarm is going to turn on : "%s"' % msg.data)
        
                     
    def listener_callback(self, msg):
        self.get_logger().info('yes')
        self.get_logger().info(msg.data)
        exit()
        
        
 

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
