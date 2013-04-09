'''
Created on 27 mrt. 2013

@author: Lithium
'''

import time
from PyQt4 import QtCore, QtGui
from subpanel.subPanel import SubPanel
from subpanel.RCcalibration.RCcalibrationWindow import Ui_Form

class RCcalibration(QtGui.QWidget, SubPanel):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        SubPanel.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.start.setEnabled(True)
        self.ui.cancel.setEnabled(False)
        
        # Setup left transmitter stick
        leftStickScene = QtGui.QGraphicsScene()
        leftStickBackground = QtGui.QPixmap("./resources/TxDial.png")
        leftStickItem = QtGui.QGraphicsPixmapItem(leftStickBackground)
        leftStickScene.addItem(leftStickItem)
        self.leftStick = QtGui.QGraphicsEllipseItem(QtCore.QRectF(75, 75, 30, 30))
        self.leftStick.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black, QtCore.Qt.SolidPattern), 2))
        self.leftStick.setBrush(QtGui.QBrush(QtCore.Qt.blue, QtCore.Qt.SolidPattern))
        leftStickScene.addItem(self.leftStick)
        self.ui.leftTransmitter.setScene(leftStickScene)
        
        # Setup right transmitter stick
        rightStickScene = QtGui.QGraphicsScene()
        rightStickBackground = QtGui.QPixmap("./resources/TxDial.png")
        rightStickItem = QtGui.QGraphicsPixmapItem(rightStickBackground)
        rightStickScene.addItem(rightStickItem)
        self.rightStick = QtGui.QGraphicsEllipseItem(QtCore.QRectF(75, 75, 30, 30))
        self.rightStick.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black, QtCore.Qt.SolidPattern), 2))
        self.rightStick.setBrush(QtGui.QBrush(QtCore.Qt.blue, QtCore.Qt.SolidPattern))
        rightStickScene.addItem(self.rightStick)
        self.ui.rightTransmitter.setScene(rightStickScene)   
        
        self.running = False
        
        self.amount_channels = 100
        
        self.RCmin = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]
        self.RCmax = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]
        self.RCOffset = [0,0,0,0,0,0,0,0]
        self.RCSlope = [0,0,0,0,0,0,0,0]
        
        self.ui.start.clicked.connect(self.start_RCcalibration)
        self.ui.cancel.clicked.connect(self.cancel_RCcalibration)

    def start(self, xmlSubPanel, boardConfiguration):
        self.xmlSubPanel = xmlSubPanel
        self.boardConfiguration = boardConfiguration
        
        try:
            self.amount_channels = int(self.boardConfiguration["Receiver Channels"])
        except:
            self.amount_channels = 10
            print("Can't read amount of channels from boardconfiguration!")
        

    def start_RCcalibration(self):
        if self.running:    #we are already running and the user want to finish the calibration
                print("Finish")
                
                for i in range(0, self.amount_channels):
                    self.RCOffset[i] = ((2000*self.RCmin[i]) - (1000*self.RCmax[i]))/(self.RCmin[i]-self.RCmax[i])
                    self.RCSlope[i] = ((1000-self.RCOffset[i])/self.RCmin[i])
                
                print("Offset: " + str(self.RCOffset))
                print("Slope: " + str(self.RCSlope))
                
                self.ui.start.setText("Start")
                #do some math to calculate the offset and slope
                self.cancel_RCcalibration() #we can stop the calibration it's done
        
        elif not self.running:
            if self.comm.isConnected() == True:
                self.comm.write("t")
                self.timer = QtCore.QTimer()
                self.timer.timeout.connect(self.readContinuousData)
                self.timer.start(50)
                self.startCommThread()
                self.running = True
                
                #self.ui.start.setEnabled(False)
                self.ui.cancel.setEnabled(True)
                self.ui.next.setEnabled(False)
                
                self.ui.start.setText("Finish")
                
                #    pitch, roll, yaw, throttle, mode, aux1, aux2, aux3
                self.RCmin = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]
                self.RCmax = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]
            
                
                
    def cancel_RCcalibration(self):
        self.comm.write("x")
        self.comm.flushResponse()
        self.running = False
        #self.ui.start.setEnabled(True)
        self.ui.cancel.setEnabled(False)
        self.ui.next.setEnabled(True)
                
        
    def readContinuousData(self):
        '''This method continually reads telemetry from the AeroQuad'''
        isConnected = self.comm.isConnected()
        if isConnected and not self.commData.empty():
            
            string = self.commData.get()
            string_out = string.split(',')
            
            if self.running:
                for i in range(0, self.amount_channels):
                    if int(string_out[i]) < self.RCmin[i]:  #lets look if the channel is lower then we have saved and if save it
                        self.RCmin[i] = int(string_out[i])
                        print('Channel id lower: ' + str(i))
                        
                    if int(string_out[i]) > self.RCmax[i]:  #lets look if the channel is higher then we have saved and if save it
                        self.RCmax[i] = int(string_out[i])
                        print('Channel id higher: ' + str(i))
                    
                    self.update_gui(i, string_out[i])                      #we want the gui to update send the channel number we are working on
            self.updateLeftStick(int(string_out[3]), int(string_out[2]))
            self.updateRightStick(int(string_out[0]), int(string_out[1]))
                                       
            self.ui.commLog.append(self.timeStamp() + " <- " + self.commData.get())
            self.ui.commLog.ensureCursorVisible()
            
    def update_gui(self, channel_number, value):
        if channel_number == 0:
            self.ui.progressBar_RCmode.setValue(int(value))
        if channel_number == 1:
            self.ui.progressBar_RCAux1.setValue(int(value))
        if channel_number == 2:
            self.ui.progressBar_RCAux2.setValue(int(value))
        if channel_number == 3:
            self.ui.progressBar_RCAux3.setValue(int(value))
    
    def updateLeftStick(self, throttle, yaw):
        throttlePosition = self.scale(throttle, (1000.0, 2000.0), (58.0, -57.0))
        yawPosition = self.scale(yaw, (1000.0, 2000.0), (-57.0, 55.0))
        self.leftStick.setPos(yawPosition, throttlePosition)
        
    def updateRightStick(self, roll, pitch):
        rollPosition = self.scale(roll, (1000.0, 2000.0), (-57.0, 55.0))
        pitchPosition = self.scale(pitch, (1000.0, 2000.0), (58.0, -57.0))
        self.rightStick.setPos(rollPosition, pitchPosition)
        
    def scale(self, val, src, dst):
        '''Scale the given value from the scale of src to the scale of dst.'''
        return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]
        
        