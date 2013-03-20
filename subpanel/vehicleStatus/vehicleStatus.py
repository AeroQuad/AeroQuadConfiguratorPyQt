'''
Created on Dec 6, 2012

@author: Ted Carancho
'''

from PyQt4 import QtCore, QtGui
from subpanel.subPanel import SubPanel
from subpanel.vehicleStatus.vehicleStatusWindow import Ui_vehicleStatus
from utilities.barGauge import BarGauge
import math
import ast
import time

class vehicleStatus(QtGui.QWidget, SubPanel):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        SubPanel.__init__(self)
        self.ui = Ui_vehicleStatus()
        self.ui.setupUi(self)
        self.channelCount = 0
        self.rawData = ""
        
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

        # Setup text info in artificial horizon
        rollLabel = horizonScene.addText("Roll:")
        rollLabel.setDefaultTextColor(QtCore.Qt.white)
        rollLabel.setPos(102, 420)
        self.roll = horizonScene.addText("0.0")
        self.roll.setDefaultTextColor(QtCore.Qt.white)
        self.roll.setPos(125, 420)
        pitchLabel = horizonScene.addText("Pitch:")
        pitchLabel.setDefaultTextColor(QtCore.Qt.white)
        pitchLabel.setPos(102, 405)
        self.pitch = horizonScene.addText("0.0")
        self.pitch.setDefaultTextColor(QtCore.Qt.white)
        self.pitch.setPos(132, 405)
        headingLabel = horizonScene.addText("Heading:")
        headingLabel.setDefaultTextColor(QtCore.Qt.white)
        headingLabel.setPos(102, 390)
        self.heading = horizonScene.addText("0.0")
        self.heading.setDefaultTextColor(QtCore.Qt.white)
        self.heading.setPos(147, 390)
        altitudeLabel = horizonScene.addText("Altitude:")
        altitudeLabel.setDefaultTextColor(QtCore.Qt.white)
        altitudeLabel.setPos(320, 390)
        self.altitude = horizonScene.addText("000.0")
        self.altitude.setDefaultTextColor(QtCore.Qt.white)
        self.altitude.setPos(363, 390)
        altHoldLabel = horizonScene.addText("Alt Hold:")
        altHoldLabel.setDefaultTextColor(QtCore.Qt.white)
        altHoldLabel.setPos(331, 405)
        self.altitudeHold = horizonScene.addText("Off")
        self.altitudeHold.setDefaultTextColor(QtCore.Qt.red)
        self.altitudeHold.setPos(374, 405)
        armLabel = horizonScene.addText("Motors:")
        armLabel.setDefaultTextColor(QtCore.Qt.white)
        armLabel.setPos(102, 653)
        self.motorArm = horizonScene.addText("Not Armed")
        self.motorArm.setDefaultTextColor(QtCore.Qt.red)
        self.motorArm.setPos(102, 668)
        battLabel = horizonScene.addText("Batt:")
        battLabel.setDefaultTextColor(QtCore.Qt.white)
        battLabel.setPos(330, 653)
        self.batteryPower = horizonScene.addText("0.000")
        self.batteryPower.setDefaultTextColor(QtCore.Qt.white)
        self.batteryPower.setPos(357, 653)
        modeLabel = horizonScene.addText("Mode:")
        modeLabel.setDefaultTextColor(QtCore.Qt.white)
        modeLabel.setPos(330, 668)
        self.flightMode = horizonScene.addText("Acro")
        self.flightMode.setDefaultTextColor(QtCore.Qt.yellow)
        self.flightMode.setPos(362, 668)
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

    def start(self, xmlSubPanel, boardConfiguration):
        '''This method starts a timer used for any long running loops in a subpanel'''
        self.xmlSubPanel = xmlSubPanel
        self.boardConfiguration = boardConfiguration
        if self.comm.isConnected():
            telemetry = self.xml.find(xmlSubPanel + "/Telemetry").text
            if telemetry != None:
                self.comm.write(telemetry)
                self.startCommThread()
                # This timer keeps telemetry queue empty
                self.timer = QtCore.QTimer()
                self.timer.timeout.connect(self.readContinuousData)
                self.timer.start(50)
                # Wait a little to give time for self.timer to start
                time.sleep(0.200)
                # This timer updates front screen a eye pleasing rate
                self.updateStatus = QtCore.QTimer()
                self.updateStatus.timeout.connect(self.updateVehicleStatus)
                self.updateStatus.start(100)
             
        try:
            self.receiverChannels = int(self.boardConfiguration["Receiver Channels"])
        except:
            self.receiverChannels = 10
        # Do we need these?
        #self.altitudeDetect = self.boardConfiguration["Barometer"] == "Detected"
        #self.batteryMonitorDetect = self.boardConfiguration["Battery Monitor"] == "Enabled"
        
        # Setup plots to display rest of transmitter channels
        transmitterScene = QtGui.QGraphicsScene()
        self.channelCount = self.receiverChannels - 4
        self.barGaugeWidth = 25.0
        self.xmitChannel = []
        self.xmitLabel = []
        self.xmitLabels = ["Mode", "Aux1", "Aux2", "Aux3", "Aux4", "Aux5"]
        self.labelHeight = 25

        for channel in range(self.channelCount):
            barGauge = QtGui.QGraphicsRectItem()
            barGauge.setBrush(QtGui.QBrush(QtCore.Qt.blue, QtCore.Qt.SolidPattern))
            self.xmitChannel.append(barGauge)
            transmitterScene.addItem(self.xmitChannel[channel])
            label = transmitterScene.addText(self.xmitLabels[channel])
            label.setDefaultTextColor(QtCore.Qt.white)
            label.setPos(self.xmitChannelLocation(channel), self.ui.transmitterOutput.height())
            self.xmitLabel.append(label)
        self.ui.transmitterOutput.setScene(transmitterScene)
        
        for channel in range(self.channelCount):
            self.updateBarGauge(channel, 1000)
            self.xmitLabel[channel].setPos(self.xmitChannelLocation(channel) - 3, self.ui.transmitterOutput.height() - self.labelHeight)
            
        # Center transmitter output window
        self.ui.transmitterOutput.centerOn(0.0, 0.0)
        
        # Setup background for motor view
        motorScene = QtGui.QGraphicsScene()
        try:
            vehicle = self.boardConfiguration["Flight Config"]
        except:
            vehicle = "Quad +"
        vehicleFile = self.xml.find(xmlSubPanel + "/VehicleGraphics/Vehicle/[@Name='" + vehicle + "']")
        vehicleImage = QtGui.QPixmap(vehicleFile.text)
        vehicleHeight = int(vehicleFile.attrib["Height"])
        vehicleWidth = int(vehicleFile.attrib["Width"])
        scaledImage = vehicleImage.scaled(vehicleWidth, vehicleHeight, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        motorScene.addPixmap(scaledImage)
        
        # Setup motor view
        try:
            self.motorCount = int(self.boardConfiguration["Motors"])
        except:
            self.motorCount = 4
        self.motor = []
        motorLocation = ast.literal_eval(vehicleFile.attrib["Motors"]) # read in motor locations from XML
        for motorIndex in range(self.motorCount):
            self.motor.append(BarGauge("Motor " + str(motorIndex+1)))
            self.motor[motorIndex].setPos(motorLocation[motorIndex][0], motorLocation[motorIndex][1])
            motorScene.addItem(self.motor[motorIndex])
        self.ui.motorView.setScene(motorScene)
    
    def updateBarGauge(self, channel, value):
        #output = self.scale(value, (1000.0, 2000.0), (25.0, self.windowHeight - 25.0)) - self.labelHeight
        output = self.scale(value, (1000.0, 2000.0), (25.0, self.windowHeight - 10)) - self.labelHeight
        self.xmitChannel[channel].setRect(self.xmitChannelLocation(channel), self.windowHeight-(output + self.labelHeight), self.barGaugeWidth, output)

    def xmitChannelLocation(self, channel):
        barPosition = (self.ui.transmitterOutput.width() - (self.barGaugeWidth * self.channelCount)) / (self.channelCount + 1)
        location = ((channel + 1) * barPosition) + (channel * self.barGaugeWidth)
        return location

    def resizeEvent(self, event):
        #size = event.size()
        self.windowHeight = self.ui.transmitterOutput.height()
        self.windowWidth = self.ui.transmitterOutput.width()
        self.ui.transmitterOutput.setSceneRect(0, 0, self.windowWidth*2, self.windowHeight*2)
        self.ui.transmitterOutput.centerOn(0,0)
        for channel in range(self.channelCount):
            self.updateBarGauge(channel, 1000)
            self.xmitLabel[channel].setPos(self.xmitChannelLocation(channel) - 3, self.ui.transmitterOutput.height() - self.labelHeight)

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
        '''This method continually emptys the telemetry queue from the AeroQuad'''
        if self.comm.isConnected() and not self.commData.empty():           
            self.rawData = self.commData.get()
                
    def updateVehicleStatus(self):
        '''This method continually reads the last telemetry value from the AeroQuad'''
        if self.comm.isConnected():        
            data = self.rawData.split(",")
            motorArmed = int(data[0])
            if motorArmed:
                self.motorArm.setPlainText("Armed")
                self.motorArm.setDefaultTextColor(QtCore.Qt.green)
            else:
                self.motorArm.setPlainText("Not Armed")
                self.motorArm.setDefaultTextColor(QtCore.Qt.red)
            roll = math.degrees(float(data[1]))
            self.roll.setPlainText("{:.1f}".format(roll))
            pitch = math.degrees(float(data[2]))
            self.pitch.setPlainText("{:.1f}".format(pitch))
            heading = math.degrees(float(data[3]))
            self.heading.setPlainText("{:.1f}".format(heading).zfill(5))
            self.updatePitchRoll(roll, pitch)
            self.updateHeading(heading)
            altitude = float(data[4])
            self.altitude.setPlainText("{:.1f}".format(altitude).zfill(5))
            altitudeHold = int(data[5])
            if altitudeHold:
                self.altitudeHold.setPlainText("On")
                self.altitudeHold.setDefaultTextColor(QtCore.Qt.green)
            else:
                self.altitudeHold.setPlainText("Off")
                self.altitudeHold.setDefaultTextColor(QtCore.Qt.red)
            self.updateRightStick(int(data[6]), int(data[7]))
            self.updateLeftStick(int(data[9]), int(data[8]))
            for receiverIndex in range(self.channelCount):
                self.updateBarGauge(receiverIndex, int(data[receiverIndex+10]))
            for motorIndex in range(self.motorCount):
                self.motor[motorIndex].setValue(int(data[motorIndex+14]))
            batteryPower = float(data[22])
            self.batteryPower.setPlainText("{:.3f}".format(batteryPower))
            flightMode = int(data[23])
            if flightMode:
                self.flightMode.setPlainText("Stable")
                self.flightMode.setDefaultTextColor(QtCore.Qt.green)
            else:
                self.flightMode.setPlainText("Acro")
                self.flightMode.setDefaultTextColor(QtCore.Qt.yellow)
