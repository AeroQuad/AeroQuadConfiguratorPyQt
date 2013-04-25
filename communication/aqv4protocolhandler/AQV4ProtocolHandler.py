'''
Created on Apr 24, 2013

@author: Kenny
'''

import time
import threading
import Queue
from PyQt4 import QtCore

class AQV4ProtocolHandler(object):


    def __init__(self,communicator,model):
        
        self.communicator = communicator
        self.model = model
        
        self.is_connected = False
        
        self.updateStatus = QtCore.QTimer()
        self.updateStatus.timeout.connect(self.reading_thread_call_back)
        self.updateStatus.start(20)
        
    def process_new_connection(self):
        self.model.set_is_connected(True)
        
        self.communicator.write('X')
        self.communicator.flushResponse()
        # Request version number to identify AeroQuad board
        
        self.communicator.write('#')
        size = int(self.communicator.waitForRead())
        for index in range(size):
            response = self.communicator.waitForRead()
            configuration = response.split(':')
            self.model.setBoadConfigurationProperty(configuration[0],configuration[1].strip())
            
            
            
        
    def process_deconnection(self):
        self.model.set_is_connected(False)
        
    def reading_thread_call_back(self):

        if self.communicator.isConnected() :
            if not self.is_connected :
                self.process_new_connection()
                self.is_connected = True
            # read data
        else :
            if self.is_connected :
                self.process_deconnection()
        
        
    
        