#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Mon Dec 13 15:52:22 2010

import wx

# begin wxGlade: extracode
# end wxGlade



class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, -1, style=0)
        self.MainSizer = wx.Panel(self.notebook_1, -1)
        self.LabelHive = wx.StaticText(self.MainSizer, -1, "Hive:")
        self.TextHive = wx.TextCtrl(self.MainSizer, -1, "irc.hiddenaces.net")
        self.LabelPort = wx.StaticText(self.MainSizer, -1, "Port:")
        self.TextPort = wx.TextCtrl(self.MainSizer, -1, "6667")
        self.LabelChan = wx.StaticText(self.MainSizer, -1, "Chan:")
        self.TextChan = wx.TextCtrl(self.MainSizer, -1, "#loic")
        self.LabelHiveTarget = wx.StaticText(self.MainSizer, -1, "Hive Target")
        self.TextTarget = wx.TextCtrl(self.MainSizer, -1, "Target: null", style=wx.TE_READONLY)
        self.LabelPower = wx.StaticText(self.MainSizer, -1, "Power:")
        self.SliderPower = wx.Slider(self.MainSizer, -1, 9001, 0, 9001, style=wx.SL_HORIZONTAL|wx.SL_LABELS)
        self.ButtonConenctToHive = wx.Button(self.MainSizer, -1, "Conenct To Hive")
        self.TextOut = wx.TextCtrl(self.MainSizer, -1, "Loaded", style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL|wx.TE_RICH)
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, -1)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.EvtConnectToHive, self.ButtonConenctToHive)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("PyHiveMind")
        self.SetSize((217, 504))
        self.TextTarget.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.TextTarget.SetForegroundColour(wx.Colour(0, 255, 255))
        self.TextOut.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.TextOut.SetForegroundColour(wx.Colour(0, 255, 255))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_3 = wx.FlexGridSizer(1, 1, 0, 0)
        grid_sizer_2 = wx.GridSizer(5, 1, 0, 0)
        grid_sizer_4 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_3 = wx.FlexGridSizer(3, 2, 0, 0)
        grid_sizer_3.Add(self.LabelHive, 0, 0, 0)
        grid_sizer_3.Add(self.TextHive, 0, wx.EXPAND, 0)
        grid_sizer_3.Add(self.LabelPort, 0, 0, 0)
        grid_sizer_3.Add(self.TextPort, 0, wx.EXPAND, 0)
        grid_sizer_3.Add(self.LabelChan, 0, 0, 0)
        grid_sizer_3.Add(self.TextChan, 0, wx.EXPAND, 0)
        grid_sizer_3.AddGrowableCol(1)
        grid_sizer_2.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.LabelHiveTarget, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.TextTarget, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 0)
        grid_sizer_4.Add(self.LabelPower, 0, 0, 0)
        grid_sizer_4.Add(self.SliderPower, 0, wx.ALL|wx.EXPAND, 0)
        grid_sizer_4.AddGrowableRow(0)
        grid_sizer_4.AddGrowableCol(1)
        grid_sizer_2.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.ButtonConenctToHive, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.TextOut, 0, wx.EXPAND, 0)
        self.MainSizer.SetSizer(grid_sizer_2)
        self.notebook_1.AddPage(self.MainSizer, "HIVEMIND")
        self.notebook_1.AddPage(self.notebook_1_pane_2, "ADVANCED")
        sizer_3.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_3)
        sizer_3.AddGrowableRow(0)
        sizer_3.AddGrowableCol(0)
        self.Layout()
        # end wxGlade

    def EvtConnectToHive(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `EvtConnectToHive' not implemented"
        event.Skip()

# end of class MyFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    PyHiveMind = MyFrame(None, -1, "")
    app.SetTopWindow(PyHiveMind)
    PyHiveMind.Show()
    app.MainLoop()
