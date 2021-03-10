#!/usr/bin/env python

import rospy
from my_package.msg import my_message

def talker():
  pub = rospy.Publisher('customized_msg', my_message, queue_size=10)
  rospy.init_node('test_msg')
  rate = rospy.Rate(10) # 10hz
  count = 0
  while not rospy.is_shutdown():

    msg = my_message()
    msg.x = count
    msg.y = 2
    msg.z = 4
    print(msg)
  
    pub.publish(msg)
    count = count + 1
    rate.sleep() 

if __name__ == '__main__':
  try:
    talker()
  except rospy.ROSInterruptException:
    pass