#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def talker():
  pub = rospy.Publisher('greeting', String, queue_size=10)
  pub_cmd = rospy.Publisher('commands', Twist, queue_size=10)
  
  rospy.init_node('talker')
  rate = rospy.Rate(10) # 10hz

  cmd_msg = Twist()

  cmd_msg.linear.x = 1
  cmd_msg.linear.y = 0
  cmd_msg.linear.z = 0
  cmd_msg.angular.x = 0
  cmd_msg.angular.y = 0
  cmd_msg.angular.z = 2

  while not rospy.is_shutdown():
    hello_str = "hello world %s" % rospy.get_time()
    pub.publish(hello_str)
    print(hello_str)
    
    pub_cmd.publish(cmd_msg)

    rate.sleep() 

if __name__ == '__main__':
  try:
    talker()
  except rospy.ROSInterruptException:
    pass