#!/usr/bin/env python
import roslib; roslib.load_manifest('automatica2014_pg70_fake_joint')

import sys

import rospy
from control_msgs.msg import *
from sensor_msgs.msg import *

class FakeJoint:
    def __init__(self):
	rospy.Subscriber("/sia10f/gripper_controller/state", JointTrajectoryControllerState, self.js_callback)
	self.pub = rospy.Publisher('/sia10f/joint_states', JointState)

    def js_callback(self, data):
        #print data
	msg = JointState()
	msg.name = ["finger_right_joint"]
	msg.header.stamp = rospy.Time.now()
	msg.position = data.actual.positions
	print msg
	self.pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node('pg70_fake_joint')
    print "starting fake joint"
    server = FakeJoint()
    print "fake joint started"
    rospy.spin()    
    
    
