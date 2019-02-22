#!/usr/bin/env python

import rospy
import sys
import time

from phoenix_msgs.msg import Ir_State
from geometry_msgs.msg import Twist
from std_msgs.msg import String, Bool, Float64, Empty

class AutoDock(object):
      
    def __init__(self):
        #self._VelocityCommandPublisher = rospy.Publisher("cmd_vel", Twist, queue_size=1) 
        self._Ir_ThetaCommandPublisher = rospy.Publisher("ir_theta", Float64, queue_size=5)  
        self._RearBumperCommandPublisher = rospy.Publisher("rear_bumper", Empty, queue_size=10, latch=True)   
        
 
    def start(self):
            rospy.Subscriber("ir_state", Ir_State, self._onIrStateReceived)        

    def _onIrStateReceived(self, data):
        LT = 0
        RT = 0
        look = 0
        left_ir = data.right
        right_ir = data.left
        rear_bumper = bool(data.rear)
       
        if (right_ir == 1 ) and (left_ir == 1 ): # add a slow turn in a direction with a tile loop
            print "no signal"
            look = -0.2            
        if left_ir < 1:
            LT = 0.02
        if right_ir < 1:
            RT = -0.02
            
        angle = LT + RT + look
        print angle
        #self._RearBumperCommandPublisher.publish(rear_bumper) 
        self._Ir_ThetaCommandPublisher.publish(angle)


if __name__ == '__main__':
    rospy.init_node('ir_state')
    AutoDock = AutoDock()
    try:
        AutoDock.start()
        rospy.spin()

    finally:
        pass #AutoDock.close()


