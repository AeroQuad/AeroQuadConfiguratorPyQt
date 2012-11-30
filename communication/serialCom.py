'''
Created on Nov 7, 2012

@author: Ted Carancho
'''
import os
import serial
import time
from serial.tools import list_ports

class AQSerial(object):
    '''
    This handles all serial communication
    '''
    
    def __init__(self):
        self.comm = None
        self.availablePorts = []
        self.connected = False

    def connect(self, port, baud, delay, commTimeout):
        self.comm = serial.Serial(port, baud, timeout=commTimeout)
        self.comm.setDTR(False)
        time.sleep(0.100)
        self.comm.setDTR(True)
        time.sleep(delay)
        self.connected = True
        
    def disconnect(self):
        self.comm.close()
        self.connected = False
        
    def write(self, data):
        self.comm.write(bytes(data.encode('utf-8')))
        
    def read(self):
        response = self.comm.readline().decode('utf-8')
        return response.rstrip('\r\n')
    
    def dataAvailable(self):
        return self.comm.inWaiting()
        
    def detectPorts(self):
        if os.name == 'nt':
            self.availablePorts = []
            for i in range(256):
                try:
                    s = serial.Serial(i)
                    self.availablePorts.append(s.portstr)
                    s.close()
                except serial.SerialException:
                    pass
        else:
            self.availablePorts = [port[0] for port in list_ports.comports()]
        
        return self.availablePorts

    def isConnected(self):
        return self.connected