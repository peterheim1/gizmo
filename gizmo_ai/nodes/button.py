#!/usr/bin/env python

import wx
import rospy
import sys
import time
from dock_list import Speaker
from phoenix_msgs.msg import Ir_State
from geometry_msgs.msg import Twist
from std_msgs.msg import String
class MyForm(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Button Tutorial")
        panel = wx.Panel(self, wx.ID_ANY)
        #rospy.Subscriber("ir_state", Ir_State, self._onIrStateReceived)
        button = wx.Button(panel, id=wx.ID_ANY, label="Press Me")
        button.Bind(wx.EVT_BUTTON, self.onButton)
        # self.Bind(wx.EVT_BUTTON, self.onButton, button)
 
    #----------------------------------------------------------------------

    def _onIrStateReceived(self, data):
        print data
        #self.t1 = data

    def onButton(self, event):
        """
        This method is fired when its corresponding button is pressed
        """
        p1 = Speaker()
        p1.dock('dock')
        print "Button pressed!"
 
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
