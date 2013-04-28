'''
Created on Apr 24, 2013

@author: Kenny
'''

import time
import threading
import Queue
from PyQt4 import QtCore
import logging

class AQV4ProtocolHandler(object):


    def __init__(self,communicator,vehicle_model):
        
        self._communicator = communicator
        self._vehicle_model = vehicle_model
        
        self._is_connected = False
        
        self._reader_thread = threading.Thread(target=self._reading_thread_call_back, args=[])
        self._reader_thread.start()
        self._raw_data = Queue.Queue()
        
#        self._reading_timer = QtCore.QTimer()
#        self._reading_timer.timeout.connect(self._read_continuous_data)
#        self._reading_timer.start(50)
        
    def _process_new_connection(self):
        self._is_connected = True
        self._vehicle_model.set_is_connected(True)
        
        self._communicator.write('X')
        self._communicator.flushResponse()
        # Request version number to identify AeroQuad board
        
        self._communicator.write('#')
#        size = int(self._communicator.waitForRead())
#        for index in range(size):
#            response = self._communicator.waitForRead()
#            configuration = response.split(':')
#            self._vehicle_model.setBoadConfigurationProperty(configuration[0],configuration[1].strip())
        
    def _process_deconnection(self):
        self._vehicle_model.set_is_connected(False)
        
    def _reading_thread_call_back(self):

        while(True):
            try:
                if self._communicator.isConnected() :
                    if not self._is_connected :
                        self._process_new_connection()
                    elif self._communicator.dataAvailable():
                        self._raw_data.put(self._communicator.read())
                        if not self._raw_data.empty() :
                            print(str(self._raw_data.get()))
                    else:
                        time.sleep(0.100)
                else :
                    if self._is_connected :
                        self._process_deconnection()
            except:
                print("oups")
#                logging.error("Communication asserted")
                
#    def _read_continuous_data(self):
#        if self._communicator.isConnected() and not self._raw_data.empty:           
#            raw_data = self._raw_data.get() # self.data is updated in commThread()
#            print(raw_data)
            
#            # Replace lines below with desired functionality
#            data = rawData.split(",")
#            for i in data:
#                print(i)

                
        
        
        
    
        