#!/usr/bin/env python
#-*- coding: utf-8 -*-
import rospy
import sys
from std_msgs.msg import String

def input_str():
	read_str = String()
	read_str.data = raw_input()
	if not read_str:
		print('NULL')
	print(read_str)
	pub.publish(read_str)

if __name__ == '__main__':
	rospy.init_node('messanger')
	pub = rospy.Publisher('/chatter',String,queue_size=10)
	try:
		while not rospy.is_shutdown():
			input_str()
	except rospy.ROSInterruptException:
		pass
