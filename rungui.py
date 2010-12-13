# -*- coding: utf8 -*-
import wx
import os
import gui
import main
from multiprocessing import Process, Queue

#Here you overload all the functons you want
class framelogic(gui.MyFrame):
    def init(self):
        self.running = False;#is the flooder backend running
        return
    def EvtConnectToHive(self,event):
        if not self.running:
            self.running= True;
            host = self.TextHive.GetValue();
            port = int(self.TextPort.GetValue())
            channel = self.TextChan.GetValue()
            p = Process(target=backend, args=(None,host,port,channel))
            p.start();
            
        return

def backend(nothing,host,port,channel):
    parentProcess =os.getppid()
    processId=os.getpid();
    main.main([nothing,host,port,channel])
            

app = wx.PySimpleApp()
wx.InitAllImageHandlers()
frame = framelogic(None, -1, "")
frame.init() #things to do at startup

app.SetTopWindow(frame)

frame.Show()
app.MainLoop()
