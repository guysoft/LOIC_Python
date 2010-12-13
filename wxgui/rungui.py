# -*- coding: iso-8859-1 -*-
import wx
import gui

#Here you overload all the functons you want
class framelogic(gui.MyFrame):
    def init(self):
        return

app = wx.PySimpleApp()
wx.InitAllImageHandlers()
frame = framelogic(None, -1, "")
frame.init() #things to do at startup

app.SetTopWindow(frame)

frame.Show()
app.MainLoop()