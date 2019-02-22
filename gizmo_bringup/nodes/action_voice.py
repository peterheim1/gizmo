#! /usr/bin/env python

import rospy

import actionlib
import subprocess
import phoenix_msgs.msg

class VoiceAction(object):
    # create messages that are used to publish feedback/result
    _feedback = phoenix_msgs.msg.VoiceActionFeedback()
    _result = phoenix_msgs.msg.VoiceActionResult()

    def __init__(self):
        self._action_name = "voice_action"
        self._as = actionlib.SimpleActionServer(self._action_name, phoenix_msgs.msg.VoiceAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()
      
    def execute_cb(self, goal):
        # helper variables
        r = rospy.Rate(1)
        success = True
        subprocess.call(["espeak", "-v", "english", goal.text]) 
        # publish info to the console for the user
        #rospy.loginfo(goal)
        
        print goal.text
            #r.sleep()
          
        if success:
            #self._result.sequence = self._feedback.sequence
            #rospy.loginfo('%s: Succeeded' % self._action_name)
            self._as.set_succeeded()
        
if __name__ == '__main__':
    rospy.init_node('Voice_action')
    server = VoiceAction()
    rospy.spin()
