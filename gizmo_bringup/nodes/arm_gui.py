#!/usr/bin/python
from Tkinter import *
import rospy
from phoenix_msgs.msg import Right_joint, Left_joint
from SerialDataGateway import SerialDataGateway


def show_values():

    x = w2.get()
    y= w1.get()
    z= w3.get()
    lj1 = l1.get()
    lj2 = l2.get()
    lj3 = l3.get()
    lj4 = l4.get()
    lj5 = l5.get()
    rj1 = r1.get()
    rj2 = r2.get()
    rj3 = r3.get()
    rj4 = r4.get()
    rj5 = r5.get()
    right_joints = rospy.Publisher('/right_joints', Right_joint, queue_size=5)
    #left_joints = rospy.Publisher('/left_joints', Left_joint, queue_size=5)
    right = Right_joint()
    right.j0 = x
    right.j1 = y
    right.j2 = rj1
    right.j3 = rj2
    right.j4 = rj3
    right.j5 = rj4
    right.j6 = rj5
    right_joints.publish(right)
    left = Left_joint()
    left.j0 = lj1
    left.j1 = lj2
    left.j2 = lj3
    left.j3 = lj4
    left.j4 = lj5
    left.j5 = z
    #left_joints.publish(left)

    #print x, y,z
    #print rj1, rj2, rj3, rj4, rj5
    #print lj1, lj2, lj3, lj4, lj5

def move_left():

    x = w2.get()
    y= w1.get()
    z= w3.get()
    lj1 = l1.get()
    lj2 = l2.get()
    lj3 = l3.get()
    lj4 = l4.get()
    lj5 = l5.get()
    rj1 = r1.get()
    rj2 = r2.get()
    rj3 = r3.get()
    rj4 = r4.get()
    rj5 = r5.get()
    #right_joints = rospy.Publisher('/right_joints', Right_joint, queue_size=5)
    left_joints = rospy.Publisher('/left_joints', Left_joint, queue_size=5)
    right = Right_joint()
    right.j0 = x
    right.j1 = y
    right.j2 = rj1
    right.j3 = rj2
    right.j4 = rj3
    right.j5 = rj4
    right.j6 = rj5
    #right_joints.publish(right)
    left = Left_joint()
    left.j0 = lj1
    left.j1 = lj2
    left.j2 = lj3
    left.j3 = lj4
    left.j4 = lj5
    left.j5 = z
    left_joints.publish(left)

    #print x, y,z
    #print rj1, rj2, rj3, rj4, rj5
    #print lj1, lj2, lj3, lj4, lj5

def netural():
    l1.set(90)
    l2.set(90)
    l3.set(90)
    l4.set(90)
    l5.set(90)
    w1.set(90)
    w2.set(90)
    w3.set(90)
    r1.set(140)
    r2.set(79)
    r3.set(90)
    r4.set(90)
    r5.set(90)
    print "reset pos"


rospy.init_node("servo_test")
root = Tk()
root.title('Bentley')
#root.geometry('{}x{}'.format(750, 350))
root.geometry('1050x350+300+200')

# create all of the main containers
top_frame = Frame(root, bg='cyan', width=250, height=50, pady=3)
center = Frame(root, bg='gray2', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(root, bg='white', width=450, height=45, pady=3)
#btm_frame2 = Frame(root, bg='lavender', width=450, height=60, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ns")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3,)
#btm_frame2.grid(row=4, sticky="ew")

# create the widgets for the bottom frame frame
#t1 = Label(btm_frame, text='bottom frame')
button = Button(btm_frame,
                   text="QUIT",
                   fg="red",
                   command=quit)

button1 = Button(btm_frame,
                   text="Move Right",
                   fg="black",
                   command=show_values)

button3 = Button(btm_frame,
                   text="Netural",
                   fg="black",
                   command=netural)

button4 = Button(btm_frame,
                   text="Move Left",
                   fg="black",
                   command=move_left)


# layout the widgets in the bottom frame
#t1.grid(row=0, columnspan=3)
button4.grid(row=0, column=1)
button3.grid(row=0, column=2)
button1.grid(row=0, column=3)
button.grid(row=0, column=6)

# create the widgets for the top frame
model_label = Label(top_frame, text='Bentley Servo Control')
#width_label = Label(top_frame, text='Width:')
#length_label = Label(top_frame, text='Length:')
#entry_W = Entry(top_frame, background="pink")
#entry_L = Entry(top_frame, background="orange")


# layout the widgets in the top frame
model_label.grid(row=0, columnspan=3)
#width_label.grid(row=1, column=0)
#length_label.grid(row=1, column=2)
#entry_W.grid(row=1, column=1)
#entry_L.grid(row=1, column=3)


# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = Frame(center, bg='blue', width=250, height=190)
ctr_mid = Frame(center, bg='yellow', width=250, height=190, padx=3, pady=3)
ctr_right = Frame(center, bg='green', width=250, height=190, padx=3, pady=3)
ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="ns")
#left pane
Lab1 = Label(ctr_left, text='Left Arm')
l1 = Scale(ctr_left, from_=0, to=180)
l1.set(64)
l2 = Scale(ctr_left, from_=0, to=180)
l2.set(90)
l3 = Scale(ctr_left, from_=0, to=180)
l3.set(90)
l4 = Scale(ctr_left, from_=0, to=180)
l4.set(90)
l5 = Scale(ctr_left, from_=0, to=180,label= 'gripper')
l5.set(90)
Lab1.grid(row=0, columnspan=3)
l1.grid(row=1, column=1)
l2.grid(row=1, column=2)
l3.grid(row=1, column=3)
l4.grid(row=1, column=4)
l5.grid(row=1, column=5)

#center pane
L1 = Label(ctr_mid, text='Torso')
w1 = Scale(ctr_mid, from_=53, to=148, orient=HORIZONTAL, label= 'pan')
w1.set(90)
w2 = Scale(ctr_mid, from_=48, to=103, label= 'tilt')
w2.set(90)
w3 = Scale(ctr_mid, from_=0, to=180, orient=HORIZONTAL,label= 'waist')
w3.set(90)
L1.grid(row=0, columnspan=2)
w1.grid(row=1, column=1)
w2.grid(row=1, column=2)
w3.grid(row=1, column=3)

#right pane
R1 = Label(ctr_right, text='Right Arm')
r1 = Scale(ctr_right, from_=56, to=140)
r1.set(140)
r2 = Scale(ctr_right, from_=0, to=180)
r2.set(79)
r3 = Scale(ctr_right, from_=0, to=180)
r3.set(90)
r4 = Scale(ctr_right, from_=0, to=180)
r4.set(90)
r5 = Scale(ctr_right, from_=0, to=180, label= 'gripper')
r5.set(90)
R1.grid(row=0, columnspan=3)
r1.grid(row=1, column=1)
r2.grid(row=1, column=2)
r3.grid(row=1, column=3)
r4.grid(row=1, column=4)
r5.grid(row=1, column=5)



root.mainloop()
