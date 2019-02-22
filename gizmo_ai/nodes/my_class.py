#!/usr/bin/env python
import rospy
import sys
import time

from phoenix_msgs.msg import Ir_State
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class MyClass:
    def __init__(self):
        rospy.Subscriber("ir_state", Ir_State, self._onIrStateReceived)
        self._VelocityCommandPublisher = rospy.Publisher("cmd_vel", Twist, queue_size=1)  
        #self.rospy.init_node("auto")
        self.docked = 0

    def dock(self):
        print 'Auto dock started'
        #rospy.Subscriber("ir_state", Ir_State, self._onIrStateReceived)

    def _onIrStateReceived(self, data):
        print 'ir start'
        print data
        LT = 0
        RT = 0
        self.left_ir = data.right
        #self.right_ir = data.left
        #self.rear_bumper = data.rear
       


    def driveX(self, angle, speed):
        velocityCommand = Twist()
        velocityCommand.linear.x = float(speed) # going backwards m/s
        velocityCommand.angular.z = float(angle) 
        #print("sending vel command" + str(velocityCommand))
        if self.docked == 0:
            self._VelocityCommandPublisher.publish(velocityCommand)
        return 'SUCCESS'

if __name__ == '__main__':
    rospy.init_node('ir_state')
    AutoDock = AutoDock()
    try:
        AutoDock.start()
        rospy.spin()

    finally:
        AutoDock.close()


