'''
Created on Nov 19, 2012

@author: Ted Carancho
'''
import time
from threading import Thread

class subpanel(object):
    '''This is a class that contains the methods required to add new subpanels to the Configurator
    You can override any of these functions by making new ones in the subpanel they will be used.
    Look at subCommMonitor.py for an example of how to add this subclass to your subpanel.
    '''

    def __init__(self):
        self.connected = False
               
    def initialize(self, commTransport):
        '''This initializes your class with required external arguments'''
        self.serialComm = commTransport
                
    def sendCommand(self, command):
        '''Send a serial command'''
        #command = self.lineEdit.text()
        self.serialComm.write(command)
        time.sleep(0.150)
        
    def readData(self):
        '''This method reads a single response from the AeroQuad'''
        response = self.comm.read()
        return response
            
    def readContinuousData(self, serialComm):
        '''This method gets called in a thread to continuously detected incoming serial messages'''
        self.comm = serialComm
        while 1:
            if self.exitReadData == True:
                break
            response = self.comm.read()
            if response != "":
                # Replace this with subpanel's own communication needs when a response is detected
                #self.commLog.append(self.timeStamp() + " <- " + response)
                #self.commLog.ensureCursorVisible()
                time.sleep(0.050)
            else:
                time.sleep(0.250)
                # Replace this with subpanel's own communication needs when a response is not detected
                #self.commLog.ensureCursorVisible()
        
    def timeStamp(self):
        '''Records a timestamp for serial communication'''
        now = time.time()
        localtime = time.localtime(now)
        milliseconds = '%03d' % int((now - int(now)) * 1000)
        return time.strftime('%H:%M:%S.', localtime) + milliseconds

    def start(self):
        '''This method starts a new thread dedicated to reading serial communication'''
        self.isConnected()
        if self.connected == True:
            self.exitReadData = False
            thread = Thread(target=self.readContinuousData, args=[self.serialComm])
            thread.start()
        
    def stop(self):
        '''This method enables a flag which closes the continuous serial read thread'''
        self.exitReadData = True
        
    def isConnected(self):
        '''Reads flag to know if we are connected to an AeroQuad'''
        state = self.serialComm.isConnected()
        self.connected = state
