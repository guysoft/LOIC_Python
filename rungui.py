# -*- coding: iso-8859-1 -*-
import wx
import gui
import main
#from compiler.ast import Return

#Here you overload all the functons you want
class framelogic(gui.MyFrame):
    def init(self):
        print "burr"
        return
    def EvtConnectToHive(self,event):
        print "burr"
        host = self.TextHive.GetValue();
        port = int(self.TextPort.GetValue())
        channel = self.TextChan.GetValue()
        main.main([None,host,port,channel])
        return
        

app = wx.PySimpleApp()
wx.InitAllImageHandlers()
frame = framelogic(None, -1, "")
frame.init() #things to do at startup

app.SetTopWindow(frame)

frame.Show()
app.MainLoop()
