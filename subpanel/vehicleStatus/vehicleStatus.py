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
        
        self.ui.horizontalScrollBar.setValue(0)
        self.ui.horizontalScrollBar.setMinimum(-180)
        self.ui.horizontalScrollBar.setMaximum(180)
        self.ui.horizontalScrollBar.valueChanged.connect(self.updatePitchRollTest)
        
        self.ui.verticalScrollBar.setValue(0)
        self.ui.verticalScrollBar.setMinimum(-90)
        self.ui.verticalScrollBar.setMaximum(90)
        self.ui.verticalScrollBar.valueChanged.connect(self.updatePitchRollTest)
        
        self.ui.horizontalScrollBarCompass.setValue(0)
        self.ui.horizontalScrollBarCompass.setMinimum(-180)
        self.ui.horizontalScrollBarCompass.setMaximum(180)
        self.ui.horizontalScrollBarCompass.valueChanged.connect(self.updateHeadingTest)
    
        horizon = QtGui.QPixmap("./resources/artificialHorizonBackGround.svg")
        self.horizonItem = QtGui.QGraphicsPixmapItem(horizon)
        
        horizonDial = QtGui.QPixmap("./resources/artificialHorizonDial.svg")
        self.horizonDialItem = QtGui.QGraphicsPixmapItem(horizonDial)
        p = QtCore.QPointF(100.0, 390.0)
        self.horizonDialItem.setPos(p)
                
        horizonCompass = QtGui.QPixmap("./resources/artificialHorizonCompass.svg")
        self.horizonCompassItem = QtGui.QGraphicsPixmapItem(horizonCompass)
        p = QtCore.QPointF(100.0, 390.0)
        self.horizonCompassItem.setPos(p) 
              
        horizonCompassBackground = QtGui.QPixmap("./resources/artificialHorizonCompassBackGround.svg")
        self.horizonCompassBackGroundItem = QtGui.QGraphicsPixmapItem(horizonCompassBackground)
        p = QtCore.QPointF(100.0, 390.0)
        self.horizonCompassBackGroundItem.setPos(p)
        
        self.scene = QtGui.QGraphicsScene()
        self.scene.addItem(self.horizonItem)
        self.scene.addItem(self.horizonDialItem)
        self.scene.addItem(self.horizonCompassBackGroundItem)
        self.scene.addItem(self.horizonCompassItem)

        #self.ui.artificialHorizon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ui.artificialHorizon.setScene(self.scene)
        
    def updatePitchRollTest(self):
        rollAngle = self.ui.horizontalScrollBar.value()
        pitchAngle = -self.ui.verticalScrollBar.value()
        self.updatePitchRoll(rollAngle, pitchAngle)
        
    def updateHeadingTest(self):
        heading = self.ui.horizontalScrollBarCompass.value()
        self.updateHeading(heading)

    def updatePitchRoll(self, rollAngle, pitchAngle):
        pitchPosition = self.scale(-pitchAngle, (-135.0, 135.0), (540.0, -540.0))
        rollCenter = self.scale(-pitchAngle, (-135.0, 135.0), (0, 1080.0))
        self.horizonItem.setPos(0, pitchPosition)
        self.horizonItem.setTransformOriginPoint(250.0, rollCenter)
        self.horizonItem.setRotation(-rollAngle)
        
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
                roll = math.degrees(float(data[1]))
                pitch = math.degrees(float(data[2]))
                heading = math.degrees(float(data[3]))
                #print(roll, pitch, heading)
                #print(data[1], data[2], data[3])
                self.updatePitchRoll(roll, pitch)
                self.updateHeading(heading)
