#!/usr/bin/env python
from Tkinter import *
import rospy
#from std_msgs.msg import Float64
from phoenix_msgs.msg import Arm_joint

def show_values():

    
    right_joints = rospy.Publisher('/arm_joint/command', Arm_joint, queue_size=5)
    j0 = w1.get()
    j1 = w2.get()
    j2 = w3.get()
    j3 = w4.get()
    j4 = w5.get()
    j5 = w6.get()
    j6 = w7.get()
    j7 = w8.get()
    right = Arm_joint()    
    right.j1 = j0
    right.j2 = j1
    right.j3 = j2
    right.j4 = j3
    right_joints.publish(right)
rospy.init_node("slider_test")
master = Tk()
w1 = Scale(master, from_=-90, to=90)
w1.set(0)
w1.pack(padx=5, pady=20, side=LEFT)
w2 = Scale(master, from_=-90, to=90)
w2.set(77)
w2.pack(padx=5, pady=20, side=LEFT)
w3 = Scale(master, from_=-90, to=90)
w3.set(-90)
w3.pack(padx=5, pady=20, side=LEFT)
w4 = Scale(master, from_=-90, to=90)
w4.set(-90)
w4.pack(padx=5, pady=20, side=LEFT)
w5 = Scale(master, from_=-90, to=90)
w5.set(0)
w5.pack(padx=5, pady=20, side=LEFT)
w6 = Scale(master, from_=-90, to=90)
w6.set(0)
w6.pack(padx=5, pady=20, side=LEFT)
w7 = Scale(master, from_=-90, to=90)
w7.set(0)
w7.pack(padx=5, pady=20, side=LEFT)
w8 = Scale(master, from_=-90, to=90)
w8.set(0)
w8.pack(padx=5, pady=20, side=LEFT)
#print w1.get()

Button(master, text='move', command=show_values).pack()

mainloop()
