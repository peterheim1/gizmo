#!/usr/bin/python
#ping_test.p is quicker when systems off line
import wx
import subprocess
import os
import socket
import thread
class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title='Gizmo GUI')
        txt1 = '    '
        txt2 = 'On'
        txt_off = 'Off'
        # Add a panel so it looks correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY)

        #bmp = wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_OTHER, (16, 16))
        titleIco = wx.StaticBitmap(self.panel, wx.ID_ANY)
        title = wx.StaticText(self.panel, wx.ID_ANY, 'Gizmo GUI')

        #define buttons
        gizmo_shutdown_Btn = wx.Button(self.panel, wx.ID_ANY, 'Gizmo Shutdown')
        exit_Btn = wx.Button(self.panel, wx.ID_ANY, 'Exit')
        sysBtn = wx.Button(self.panel, wx.ID_ANY, 'System Check')
        B1_Launch_Btn = wx.Button(self.panel, wx.ID_ANY, 'Gizmo launch')
        PowerOffBtn = wx.Button(self.panel, wx.ID_ANY, 'Power Off')

        self.B1_status_lable = wx.StaticText(self.panel, wx.ID_ANY, label='  ')
        self.B1_status_lable.SetBackgroundColour((255,255,255))
        self.B2_status_lable = wx.StaticText(self.panel, wx.ID_ANY, label='  ')
        self.B2_status_lable.SetBackgroundColour((255,255,255))
        self.B3_status_lable = wx.StaticText(self.panel, wx.ID_ANY, label='  ')
        self.B3_status_lable.SetBackgroundColour((255,255,255))
        B1_status = wx.StaticText(self.panel, wx.ID_ANY, 'B1 Status ')
        B2_status = wx.StaticText(self.panel, wx.ID_ANY, 'B2 Status ')
        B3_status = wx.StaticText(self.panel, wx.ID_ANY, 'B3 Status ')
        #bind event to button
        self.Bind(wx.EVT_BUTTON, self.on_gizmo_shutdown, gizmo_shutdown_Btn)
        self.Bind(wx.EVT_BUTTON, self.onCancel, exit_Btn)
        self.Bind(wx.EVT_BUTTON, self.OnCheck, sysBtn)
        self.Bind(wx.EVT_BUTTON, self.gizmo_launch, B1_Launch_Btn)
        self.Bind(wx.EVT_BUTTON, self.PowerOff, PowerOffBtn)
        
        topSizer        = wx.BoxSizer(wx.VERTICAL)
        titleSizer      = wx.BoxSizer(wx.HORIZONTAL)
        gizmo_launchlBtnSizer   = wx.BoxSizer(wx.HORIZONTAL)
        PowerOfflBtnSizer   = wx.BoxSizer(wx.HORIZONTAL)
        TxtLableSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputFourSizer  = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer        = wx.BoxSizer(wx.HORIZONTAL)

        titleSizer.Add(titleIco, 0, wx.ALL, 5)
        titleSizer.Add(title, 0, wx.ALL, 5)
        TxtLableSizer.Add(B1_status, 0, wx.ALL, 5)
        TxtLableSizer.Add(self.B1_status_lable, 0, wx.ALL, 5)
        TxtLableSizer.Add(B2_status, 0, wx.ALL, 5)
        TxtLableSizer.Add(self.B2_status_lable, 0, wx.ALL, 5)
        TxtLableSizer.Add(B3_status, 0, wx.ALL, 5)
        TxtLableSizer.Add(self.B3_status_lable, 0, wx.ALL, 5)
        
        btnSizer.Add(gizmo_shutdown_Btn, 0, wx.ALL, 5) 
        btnSizer.Add(sysBtn, 0, wx.ALL, 5)  
        btnSizer.Add(B1_Launch_Btn, 0, wx.ALL, 5)
        btnSizer.Add(PowerOffBtn, 0, wx.ALL, 5)    
        btnSizer.Add(exit_Btn, 0, wx.ALL, 5)

        topSizer.Add(titleSizer, 0, wx.CENTER)
        topSizer.Add(wx.StaticLine(self.panel,), 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(TxtLableSizer, 0, wx.ALL|wx.LEFT, 5)
        topSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(btnSizer, 0, wx.ALL|wx.CENTER, 5)

        self.panel.SetSizer(topSizer)
        topSizer.Fit(self)


    def on_gizmo_shutdown(self, event):
        print "Shutdown B1"
        os.system('ssh -t pi@10.0.0.9 sudo poweroff')#service call
        print "Shutdown B2"
        os.system('ssh -t pi@10.0.0.8 sudo poweroff')#service call ssh -t max@r2 ./shut_down.sh
        print "Shutdown B3"
        os.system('ssh -t pi@b3 sudo poweroff')#service call ssh -t max@r2 ./shut_down.sh

    def onCancel(self, event):
        self.Close()

    def gizmo_launch(self,event):
        print "start file on r2"
        self.B1_status_lable.SetLabel("1234.45")
        thread.start_new_thread(os.system('ssh -t max@r2 ./r2_start.sh'))

    def PowerOff(self,event):
        print "turn off Robbies power"

    def OnCheck(self, event):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(('b1', 22))
            print "B1 is on line"
            self.B1_status_lable.SetBackgroundColour((0,255,0))
        except socket.error:# as e:
            print "B1 offline"##print "Error on connect to R1: %s" % e
            self.B1_status_lable.SetBackgroundColour((255,0,0))
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(('b2', 22))
            print "B2 is on line"
            self.B2_status_lable.SetBackgroundColour((0,255,0))
        except socket.error:# as e:
            print "B2 off line"#print "Error on connect to Robbie: %s" % e
            self.B2_status_lable.SetBackgroundColour((255,0,0))
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(('b3', 22))
            print "B3 is on line"
            self.B3_status_lable.SetBackgroundColour((0,255,0))
        except socket.error:# as e:
            print "B3 off line"#print "Error on connect to Robbie: %s" % e
            self.B3_status_lable.SetBackgroundColour((255,0,0))
        s.close()      


# Run the program
if __name__ == '__main__':
    app =  wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()
