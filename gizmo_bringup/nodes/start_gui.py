#!/usr/bin/python
#ping_test.p is quicker when systems off line
import wx
import subprocess
import os
import socket
import thread
class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title='Robbie GUI')

        # Add a panel so it looks correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY)

        #bmp = wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_OTHER, (16, 16))
        titleIco = wx.StaticBitmap(self.panel, wx.ID_ANY)
        title = wx.StaticText(self.panel, wx.ID_ANY, 'Robbie GUI')

        #define buttons
        okBtn = wx.Button(self.panel, wx.ID_ANY, 'Robbie Shutdown')
        cancelBtn = wx.Button(self.panel, wx.ID_ANY, 'Exit')
        sysBtn = wx.Button(self.panel, wx.ID_ANY, 'System Check')
        B1_launch = wx.Button(self.panel, wx.ID_ANY, 'B1 launch')
        B2_launch = wx.Button(self.panel, wx.ID_ANY, 'B2 launch')
        B3_launch = wx.Button(self.panel, wx.ID_ANY, 'B3 launch')
        PowerOffBtn = wx.Button(self.panel, wx.ID_ANY, 'Power Off')

        self.st1 = wx.StaticText(self.panel, wx.ID_ANY, label='12.7')
        BatteryVoltage = wx.StaticText(self.panel, wx.ID_ANY, 'Battery Voltage ')
        #bind event to button
        self.Bind(wx.EVT_BUTTON, self.onOK, okBtn)
        self.Bind(wx.EVT_BUTTON, self.onCancel, cancelBtn)
        self.Bind(wx.EVT_BUTTON, self.OnCheck, sysBtn)
        self.Bind(wx.EVT_BUTTON, self.B1_Start, B1_launch)
        self.Bind(wx.EVT_BUTTON, self.B2_Start, B2_launch)
        self.Bind(wx.EVT_BUTTON, self.B3_Start, B3_launch)
        self.Bind(wx.EVT_BUTTON, self.PowerOff, PowerOffBtn)
        
        topSizer        = wx.BoxSizer(wx.VERTICAL)
        titleSizer      = wx.BoxSizer(wx.HORIZONTAL)
        B1_launchBtnSizer   = wx.BoxSizer(wx.HORIZONTAL)
        B2_launchBtnSizer   = wx.BoxSizer(wx.HORIZONTAL)
        B3_launchBtnSizer   = wx.BoxSizer(wx.HORIZONTAL)
        PowerOfflBtnSizer   = wx.BoxSizer(wx.HORIZONTAL)
        TxtLableSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputFourSizer  = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer        = wx.BoxSizer(wx.HORIZONTAL)

        titleSizer.Add(titleIco, 0, wx.ALL, 5)
        titleSizer.Add(title, 0, wx.ALL, 5)
        TxtLableSizer.Add(BatteryVoltage, 0, wx.ALL, 5)
        TxtLableSizer.Add(self.st1, 0, wx.ALL, 5)
        
        btnSizer.Add(okBtn, 0, wx.ALL, 5) 
        btnSizer.Add(sysBtn, 0, wx.ALL, 5)  
        btnSizer.Add(B1_launch, 0, wx.ALL, 5)
        btnSizer.Add(B2_launch, 0, wx.ALL, 5)
        btnSizer.Add(B3_launch, 0, wx.ALL, 5)
        btnSizer.Add(PowerOffBtn, 0, wx.ALL, 5)    
        btnSizer.Add(cancelBtn, 0, wx.ALL, 5)

        topSizer.Add(titleSizer, 0, wx.CENTER)
        topSizer.Add(wx.StaticLine(self.panel,), 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(TxtLableSizer, 0, wx.ALL|wx.LEFT, 5)
        topSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(btnSizer, 0, wx.ALL|wx.CENTER, 5)

        self.panel.SetSizer(topSizer)
        topSizer.Fit(self)


    def onOK(self, event):
        print "turn off B1 power"
        os.system('ssh -t pi@b1 sudo poweroff')#service call
        print "turn off B2 power"
        os.system('ssh -t pi@b2 sudo poweroff')#service call ssh -t pi@r2 ./shut_down.sh
        print "turn off B3 power"
        os.system('ssh -t pi@b3 sudo poweroff')#service call ssh -t pi@r2 ./shut_down.sh

    def onCancel(self, event):
        self.Close()

    def B1_Start(self,event):
        print "start file on B1"
        self.st1.SetLabel("1234.45")
        thread.start_new_thread(os.system('ssh -t pi@b1 ./r2_start.sh'))


    def B2_Start(self,event):
        print "start file on B2"
        self.st1.SetLabel("1234.45")
        thread.start_new_thread(os.system('ssh -t pi@b2 ./r2_start.sh'))

    def B3_Start(self,event):
        print "start file on B3"
        self.st1.SetLabel("1234.45")
        thread.start_new_thread(os.system('ssh -t pi@b3 ./r2_start.sh'))

    def PowerOff(self,event):
        print "turn off Robbies power"

    def OnCheck(self, event):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(('b1', 22))
            print "b1 is on line"
        except socket.error:# as e:
            print "b1 offline"##print "Error on connect to R1: %s" % e
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(('b2', 22))
            print "b2 is on line"
        except socket.error:# as e:
            print "b2 off line"#print "Error on connect to Robbie: %s" % e
        s.close()
        try:
            s.connect(('b3', 22))
            print "b3 is on line"
        except socket.error:# as e:
            print "b3 off line"#print "Error on connect to Robbie: %s" % e
        s.close()        


# Run the program
if __name__ == '__main__':
    app =  wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()
