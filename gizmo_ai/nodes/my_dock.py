#!/usr/bin/env python
import rospy
import sys
from phoenix_msgs.msg import Ir_State

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.rear)
    if data.rear == 0:
        rospy.signal_shutdown('reason')
        print "iff"
        
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    #rospy.Subscriber("chatter", String, callback)
    rospy.Subscriber("ir_state", Ir_State, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

