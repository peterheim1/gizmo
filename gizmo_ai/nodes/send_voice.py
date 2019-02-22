#! /usr/bin/python

import rospy
import actionlib
from actionlib_msgs.msg import *
from phoenix_msgs.msg import *

rospy.init_node('talking', anonymous=True)

client = actionlib.SimpleActionClient('voice_action', VoiceAction)
client.wait_for_server()

g = VoiceGoal()
g.text = "hi there"
print g


client.send_goal(g)
client.wait_for_result()

if client.get_state() == GoalStatus.SUCCEEDED:
    print "Succeeded"
else:
    print "Failed"

