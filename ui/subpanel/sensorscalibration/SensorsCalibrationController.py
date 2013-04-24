'''
Created on 22 apr. 2013

@author: Erik
'''

from PyQt4 import QtCore, QtGui
from ui.subpanel.BasePanelController import BasePanelController
from ui.subpanel.sensorscalibration.SensorsCalibrationPanel import Ui_SensorsCalibrationPanel

class SensorsCalibrationController(QtGui.QWidget, BasePanelController):


    def __init__(self):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        self.ui = Ui_SensorsCalibrationPanel()
        self.ui.setupUi(self)
        self.ui.start.clicked.connect(self.StartCalibration)
        self.ui.cancel.clicked.connect(self.CancelCalibration)
        self.ui.cancel.setEnabled(False)
        
        self.state = 0
        self.AmountReadings = 100
        self.ReadingNumber = 0
        self.AmountStates = 6
        
        self.CalLevel = '0'
        self.CalUpsidedown = '1'
        self.CalLeft = '2'
        self.CalRight = '3'
        self.CalFront = '4'
        self.CalRear = '5'
        
        self.ChangeUIPicture(self.state)
    
    def readContinuousData(self):
        isConnected = self.comm.isConnected()
        if isConnected and not self.commData.empty():
            if not self.AmountReadings == self.ReadingNumber:
                self.ReadingNumber += 1
                self.ui.progressBar.setValue(self.ReadingNumber)
                #We need to count something here
            elif self.AmountReadings == self.ReadingNumber:
                self.StopData()

    
    def StartCalibration(self):        
        if (self.comm.isConnected()):
            self.ui.start.setEnabled(False)
            self.ui.next.setEnabled(False)
            self.ui.cancel.setEnabled(True)
            self.comm.write("l")
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.readContinuousData)
            self.timer.start(50)
            self.startCommThread()
    
    def CancelCalibration(self):
        self.StopData()
        self.ui.start.setEnabled(True)
        self.ui.next.setEnabled(True)
        self.state = 0
        self.ChangeUIPicture(self.state)
        self.ui.progressBar.setValue(0)            
    
    def StopData(self):
        self.comm.write("x")
        self.timer.stop()
        self.comm.flushResponse()
        self.state += 1
        self.ReadingNumber = 0
        self.ui.start.setEnabled(True)
        
        if self.state == self.AmountStates:
            self.state = 0
            self.SendCalibration()
        
        self.ChangeUIPicture(self.state)      
    
    def ChangeUIPicture (self, state):
        pictureScene = QtGui.QGraphicsScene()
        
        if state == int(self.CalLevel):
            pictureBackground = QtGui.QPixmap("./resources/callevel.png")
            self.ui.commLog.setText("Place the AeroQuad on a flat and motionless surface and press the start to begin the calibration procedure")
        elif state == int(self.CalUpsidedown):
            pictureBackground = QtGui.QPixmap("./resources/callevel.png")
            self.ui.commLog.setText("Place the AeroQuad upside down and press start")
        elif state == int(self.CalLeft):
            pictureBackground = QtGui.QPixmap("./resources/calleft.png")
            self.ui.commLog.setText("Place the AeroQuad left edge down and press start")
        elif state == int(self.CalRight):
            pictureBackground = QtGui.QPixmap("./resources/calright.png")
            self.ui.commLog.setText("Place the AeroQuad right edge down and press start")
        elif state == int(self.CalFront):
            pictureBackground = QtGui.QPixmap("./resources/calfront.png")
            self.ui.commLog.setText("Place the AeroQuad front edge down and press start. The arrow indicates the front of the AeroQuad")
        elif state == int(self.CalRear):
            pictureBackground = QtGui.QPixmap("./resources/calrear.png")
            self.ui.commLog.setText("Place the AeroQuad rear edge down and press start. The arrow indicates the front of the AeroQuad")
            
        pictureItem = QtGui.QGraphicsPixmapItem(pictureBackground)
        pictureScene.addItem(pictureItem)
        self.ui.picture.setScene(pictureScene)
    
    def SendCalibration(self):
        #calculate the values and send them to the quad
        self.CancelCalibration()
        