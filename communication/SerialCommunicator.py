'''
Created on Nov 7, 2012

@author: Ted Carancho
'''
import os
import serial
import time
from serial.tools import list_ports

class SerialCommunicator(object):
    '''
    This handles all serial communication to the AeroQuad board
    '''
    
    def __init__(self):
        self._communicator = None
        self.availablePorts = []
        self.connected = False
        self.timeout = 0.0
        
        self.bufferData = ""
        self.lineDataReceived = ""

    def connect(self, port, baud, delay, commTimeout):
        ''' Open a _communicator port enable the "conencted" flag and toggle the DTR line for Arduino boards
        '''
        self._communicator = serial.Serial(port, baud, timeout=commTimeout)
        self.timeout = commTimeout
        self._communicator.setDTR(False)
        time.sleep(0.100)
        self._communicator.setDTR(True)
        time.sleep(delay)
        self.connected = True
        
#    def flushResponse(self):
#        ''' Keep reading the serial port until no data is detected
#        '''
#        while self.dataAvailable():
#            time.sleep(0.100)
#            self.read()
            
    def flush(self):
        self._communicator.flush();
        
    def read_line(self, size=None):
        return self._communicator.readline(size)        
        
    def disconnect(self):
        self._communicator.close()
        self.connected = False
        
    def write(self, data):
        self._communicator.write(bytes(data.encode('utf-8')))
        
    def read(self, size=1):
#        return self._communicator.read(size)
        response = self._communicator.readline().decode('utf-8')
        return response.rstrip('\r\n')
    
#    def waitForRead(self):
#        ''' Wait for data to be available at the port and return the resulting string.  If the timeout value is reached, stop waiting.
#        '''
#        timeout = 0.0
#        while not self.dataAvailable():
#            time.sleep(0.100)
#            timeout += 0.100
#            if (timeout >= self.timeout):
#                break
#        response = self._communicator.readline().decode('utf-8')
#        return response.rstrip('\r\n')
#    
#    def waitForLine(self):
#        while(self._communicator.inWaiting()):
#            self.bufferData += self._communicator.read(self._communicator.inWaiting())
#            if '\n' in buffer:
#                lineData = self.bufferData.split('\n')
#                self.lineDataReceived = lineData[-2]
#                self.bufferData = lineData[-1]
#        return self.lineDataReceived
                 
    def data_available(self):
        return self._communicator.inWaiting()
        
    def detect_ports(self):
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

    def is_connected(self):
        ''' Returns if "connected" flag is enabled or disabled
        '''
        return self.connected