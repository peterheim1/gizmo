#!/usr/bin/env python
from Tkinter import *
import rospy
from std_msgs.msg import Float64
from dynamixel_workbench_msgs.srv import JointCommand

def move_servo_client(name, value):
    rospy.wait_for_service('/joint_command')
    try:
        add_two_ints = rospy.ServiceProxy('/joint_command', JointCommand)
        add_two_ints("rad", name, value)
        #return resp1
    except rospy.ServiceException, e:
        print "Service call failed   vv: %s"%e


def show_values():

    #pan = rospy.Publisher('/pan', Float64, queue_size=2)
    #tilt = rospy.Publisher('/tilt', Float64, queue_size=1)
    x = float(w1.get()*0.01)
    y= float(w2.get()*0.01)
    move_servo_client(3, y)
    move_servo_client(7, x)
    #pan.publish(x)
    #tilt.publish(y)
    #print (x)

rospy.init_node("slider_test")
master = Tk()
w1 = Scale(master, from_=-20, to=30)
w1.set(0)
w1.pack()
print w1.get()
w2 = Scale(master, from_=-70, to=70, orient=HORIZONTAL)
w2.set(0)
w2.pack()

Button(master, text='move', command=show_values).pack()

mainloop()
