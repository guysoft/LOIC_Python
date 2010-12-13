# -*- coding: utf8 -*-
import wx
import os
import gui
#import main
from multiprocessing import Process, Queue

from Core.Events import *
from Core.IRC import * 
from Core.Flooder import *


#from main import *

#Here you overload all the functons you want
class framelogic(gui.MyFrame):
    def init(self):
        self.running = False;#is the flooder backend running
        
        self.listener = Listener(LAZER_RECV, lazerParseHook)
        getEventManager().addListener(self.listener)
        self.listener = Listener(START_LAZER, lazerStartHook)
        getEventManager().addListener(self.listener)
        self.listener = Listener(IRC_RESTART, restartIRCHook)
        getEventManager().addListener(self.listener)
        getEventManager().start()#opens a new thread
        
        self.irc=None;
        return
    def EvtConnectToHive(self,event):

        
        if not self.running:
            host = self.TextHive.GetValue();
            port = int(self.TextPort.GetValue())
            channel = self.TextChan.GetValue()
            self.irc = IRC(host, port, channel)
            if True:
                    newhost = host
                    newport = port
                    newchannel = channel.replace("\\", "")
                    if newhost == host and newport == port and self.irc.connected:
                        self.echo("changing channel to " +  newchannel)
                        self.irc.changeChannel(newchannel)
                        channel = newchannel
                    else:
                        host = newhost
                        port = newport
                        channel = newchannel
                        self.echo("changing host to "+ host + port + channel)
                        self.ircirc.disconnect()
                        self.ircirc.host = host
                        self.ircirc.port = port
                        self.ircirc.channel = channel
                        self.ircirc.connect()
            

            
            #sanity check channel
            if channel[0] != '#':
                channel = '#' + channel
            self.irc = IRC(host, port, channel)

            
            self.running= True;
            '''
            p = Process(target=backend, args=(None,host,port,channel))
            p.start();
            '''
        return
    
    def echo(self,message):
        '''
        This lets you print to the gui info screen
        '''
        self.TextOut.SetValue(self.TextOut.GetValue() +"\n" + message );


def backend(nothing,host,port,channel):
    #get process info
    parentProcess =os.getppid()
    processId=os.getpid();
    #main.main([nothing,host,port,channel])
    #do cool things here if we need
            

app = wx.PySimpleApp()
wx.InitAllImageHandlers()
frame = framelogic(None, -1, "")
frame.init() #things to do at startup

app.SetTopWindow(frame)

frame.Show()
app.MainLoop()
