#!/usr/bin/env python
import rospy
from phoenix_msgs.msg import Ir_State

class Speaker():
    def __init__(self):
        rospy.init_node('speaker', anonymous=True)
        rospy.Subscriber("ir_state", Ir_State, self.handle_say)
        self.right = None
        self.left = None
        self.rear = None       
    def handle_say(self, req):
        self.right = req.right
        self.left = req.left
        self.rear = req.rear
        print self.right

    def dock(self, data):
        print self.right
        print 'Auto dock started'
        if self.right == 1:
            print 'end'
            return

if __name__ == '__main__':
    try:
        speaker = Speaker()
        rospy.spin()
    except rospy.ROSInterruptException: pass

