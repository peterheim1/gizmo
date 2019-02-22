#!/usr/bin/env python

import rospy
import sys
import time

from phoenix_msgs.msg import Ir_State
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class AutoDock(object):
      
    def __init__(self):
        self._VelocityCommandPublisher = rospy.Publisher("cmd_vel", Twist, queue_size=1)
        #rospy.Subscriber("auto_dock", String, self.dock)   
        self.docked = 0
    def start(self):
            #rospy.Subscriber("auto_dock", String, self.dock)   

            rospy.Subscriber("ir_state", Ir_State, self._onIrStateReceived)

    def dock(self, data):
            print data
            if data =="dock":
                print"starting auto dock"
                rospy.Subscriber("ir_state", Ir_State, self._onIrStateReceived)
        

    def _onIrStateReceived(self, data):
        LT = 0
        RT = 0
        left_ir = data.right
        right_ir = data.left
        rear_bumper = data.rear
       
        if (right_ir == 1 ) and (left_ir == 1 ): # add a slow turn in a direction with a tile loop
            print "no signal"
        if left_ir < 1:
            LT = 0.02
        if right_ir < 1:
            RT = -0.02
            speed = -0.04
            angle = LT + RT
            #print angle
            self.driveX(angle, speed)
        if rear_bumper == 0:
            #print"stop"
            #angle = 0
            #speed = 0
            self._VelocityCommandPublisher.publish(Twist())
            #self.driveX(angle, speed)
            self.docked = 1


    def driveX(self, angle, speed):
        velocityCommand = Twist()
        velocityCommand.linear.x = float(speed) # going backwards m/s
        velocityCommand.angular.z = float(angle) 
        #print("sending vel command" + str(velocityCommand))
        if self.docked == 0:
            self._VelocityCommandPublisher.publish(velocityCommand)
        return

    def close(self):
        print("Closing")

if __name__ == '__main__':
    rospy.init_node('ir_state')
    AutoDock = AutoDock()
    try:
        AutoDock.start()
        rospy.spin()

    finally:
        AutoDock.close()
