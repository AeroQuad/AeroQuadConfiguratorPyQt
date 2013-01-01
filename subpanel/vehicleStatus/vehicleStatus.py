'''
Created on Dec 6, 2012

@author: Ted Carancho
'''

from PyQt4 import QtCore, QtGui
from subpanel.subPanelTemplate import subpanel
from subpanel.vehicleStatus.vehicleStatusWindow import Ui_vehicleStatus
#from scipy.misc import imread
#from scipy.ndimage.interpolation import rotate
import math

class vehicleStatus(QtGui.QWidget, subpanel):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        subpanel.__init__(self)
        self.ui = Ui_vehicleStatus()
        self.ui.setupUi(self)
        
        # Setup artificial horizon    
        horizon = QtGui.QPixmap("./resources/artificialHorizonBackGround.svg")
        self.horizonItem = QtGui.QGraphicsPixmapItem(horizon)
        
        horizonDial = QtGui.QPixmap("./resources/artificialHorizonDial.svg")
        horizonDialItem = QtGui.QGraphicsPixmapItem(horizonDial)
        horizonDialItem.setPos(QtCore.QPointF(100.0, 390.0))
             
        horizonCompassBackground = QtGui.QPixmap("./resources/artificialHorizonCompassBackGround.svg")
        horizonCompassBackGroundItem = QtGui.QGraphicsPixmapItem(horizonCompassBackground)
        horizonCompassBackGroundItem.setPos(QtCore.QPointF(100.0, 390.0))
                       
        horizonCompass = QtGui.QPixmap("./resources/artificialHorizonCompass.svg")
        self.horizonCompassItem = QtGui.QGraphicsPixmapItem(horizonCompass)
        self.horizonCompassItem.setPos(QtCore.QPointF(100.0, 390.0)) 
        
        horizonScene = QtGui.QGraphicsScene()
        horizonScene.addItem(self.horizonItem)
        horizonScene.addItem(horizonDialItem)
        horizonScene.addItem(horizonCompassBackGroundItem)
        horizonScene.addItem(self.horizonCompassItem)
        self.ui.artificialHorizon.setScene(horizonScene)
        
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
        
        # Setup histogram to display rest of transmitter channels
        self.ui.transmitterOutput.hideAxis('left')
        self.ui.transmitterOutput.hideAxis('bottom')
        self.ui.transmitterOutput.hideButtons()
        
        configCount = len(self.boardConfiguration)
        for config in self.boardConfiguration:
            if "Receiver Channels" in config:
                receiverConfig = config.split(": ")
                self.receiverChannls = int(receiverConfig[1])
                break
        if "Barometer: Detected" in self.boardConfiguration:
            self.altitude = True
        if "Battery Monitor: Enabled" in self.boardConfiguration:
            self.batteryMonitor = True

    def updatePitchRoll(self, rollAngle, pitchAngle):
        pitchPosition = self.scale(-pitchAngle, (-135.0, 135.0), (540.0, -540.0))
        rollCenter = self.scale(-pitchAngle, (-135.0, 135.0), (0, 1080.0))
        self.horizonItem.setPos(0, pitchPosition)
        self.horizonItem.setTransformOriginPoint(250.0, rollCenter)
        self.horizonItem.setRotation(-rollAngle)
        
    def updateLeftStick(self, throttle, yaw):
        throttlePosition = self.scale(throttle, (1000.0, 2000.0), (58.0, -57.0))
        yawPosition = self.scale(yaw, (1000.0, 2000.0), (-57.0, 55.0))
        self.leftStick.setPos(yawPosition, throttlePosition)
        
    def updateRightStick(self, roll, pitch):
        rollPosition = self.scale(roll, (1000.0, 2000.0), (-57.0, 55.0))
        pitchPosition = self.scale(pitch, (1000.0, 2000.0), (58.0, -57.0))
        self.rightStick.setPos(rollPosition, pitchPosition)
        
    def updateHeading(self, heading):
        self.horizonCompassItem.setTransformOriginPoint(150.0, 150.0)
        self.horizonCompassItem.setRotation(-heading)
        
    def scale(self, val, src, dst):
        '''Scale the given value from the scale of src to the scale of dst.'''
        return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

    def readContinuousData(self):
        '''This method continually reads telemetry from the AeroQuad'''
        if self.comm.isConnected() == True: 
            if self.comm.dataAvailable():           
                rawData = self.comm.read()
                data = rawData.split(",")
                motorArmed = int(data[0])
                roll = math.degrees(float(data[1]))
                pitch = math.degrees(float(data[2]))
                heading = math.degrees(float(data[3]))
                self.updatePitchRoll(roll, pitch)
                self.updateHeading(heading)
                altitude = float(data[4])
                altitudeHold = int(data[5])
                # Do some checking based on number of transmitter channels
                receiverData = []
                for receiverIndex in range(8):
                    receiverData.append(int(data[receiverIndex+6]))
                self.updateLeftStick(receiverData[3], receiverData[2])
                self.updateRightStick(receiverData[0], receiverData[1])
                motorPower = []
                for motorIndex in range(8):
                    motorPower.append(int(data[motorIndex+14]))
                batteryPower = float(data[22])
                flightMode = int(data[23])
