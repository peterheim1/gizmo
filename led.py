#!/usr/bin/python
import wx
import random
blues=['#0000ff','#4682b4','#00008b','#00bfff','#0d4f60']
class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Led')
        panel = wx.Panel(self)
        self.led1 =  wx.StaticBox(panel, wx.ID_ANY, "", size=(20,20), pos=(10,10))
        self.led2 =  wx.StaticBox(panel, wx.ID_ANY, "", size=(20,20), pos=(31,10))
        self.led3 =  wx.StaticBox(panel, wx.ID_ANY, "", size=(20,20), pos=(52,10))
        self.led4 =  wx.StaticBox(panel, wx.ID_ANY, "", size=(20,20), pos=(73,10))
        self.led5 =  wx.StaticBox(panel, wx.ID_ANY, "", size=(20,20), pos=(94,10))
        self.led1.SetBackgroundColour(wx.Colour( 255, 0, 0 ) )
        self.led2.SetBackgroundColour(blues[1])
        self.led3.SetBackgroundColour(blues[2])
        self.led4.SetBackgroundColour(blues[3])
        self.led5.SetBackgroundColour(blues[4])
        self.counter = -5
        self.timer = wx.Timer(self)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.Show()

    def OnTimer(self, evt):
        self.led1.SetBackgroundColour(wx.Colour( 0, 255, 0 ) )
        self.led2.SetBackgroundColour(random.choice(blues))
        self.led3.SetBackgroundColour(random.choice(blues))
        self.led4.SetBackgroundColour(random.choice(blues))
        self.led5.SetBackgroundColour(random.choice(blues))

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()
