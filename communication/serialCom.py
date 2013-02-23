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
    This handles all serial communication to the AeroQuad board
    '''
    
    def __init__(self):
        self.comm = None
        self.availablePorts = []
        self.connected = False
        self.timeout = 0.0
        
        self.bufferData = ""
        self.lineDataReceived = ""

    def connect(self, port, baud, delay, commTimeout):
        ''' Open a comm port enable the "conencted" flag and toggle the DTR line for Arduino boards
        '''
        self.comm = serial.Serial(port, baud, timeout=commTimeout)
        self.timeout = commTimeout
        self.comm.setDTR(False)
        time.sleep(0.100)
        self.comm.setDTR(True)
        time.sleep(delay)
        self.connected = True
        
    def flushResponse(self):
        ''' Keep reading the serial port until no data is detected
        '''
        while self.dataAvailable():
            time.sleep(0.100)
            self.read()
        
    def disconnect(self):
        ''' Close the serial port and disable the "connected" flag
        '''
        self.comm.close()
        self.connected = False
        
    def write(self, data):
        ''' Write a text string to the serial port
        '''
        self.comm.write(bytes(data.encode('utf-8')))
        
    def read(self):
        ''' Read a text string from the serial port and remove the newline character if it exists
        '''
        response = self.comm.readline().decode('utf-8')
        return response.rstrip('\r\n')
    
    def waitForRead(self):
        ''' Wait for data to be available at the port and return the resulting string.  If the timeout value is reached, stop waiting.
        '''
        timeout = 0.0
        while not self.dataAvailable():
            time.sleep(0.100)
            timeout += 0.100
            if (timeout >= self.timeout):
                break
        response = self.comm.readline().decode('utf-8')
        return response.rstrip('\r\n')
    
    def waitForLine(self):
        while(self.comm.inWaiting()):
            self.bufferData += self.comm.read(self.comm.inWaiting())
            if '\n' in buffer:
                lineData = self.bufferData.split('\n')
                self.lineDataReceived = lineData[-2]
                self.bufferData = lineData[-1]
        return self.lineDataReceived
                 
    def dataAvailable(self):
        ''' Wait for data to be available at the serial port
        '''
        return self.comm.inWaiting()
        
    def detectPorts(self):
        ''' Detect available serial ports
        '''
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
        ''' Returns if "connected" flag is enabled or disabled
        '''
        return self.connected