'''
Created on Dec 6, 2012

@author: Ted Carancho
'''

from PyQt4 import QtCore, QtGui
from subpanel.subPanelTemplate import subpanel
from subpanel.vehicleStatus.vehicleStatusWindow import Ui_vehicleStatus

class vehicleStatus(QtGui.QWidget, subpanel):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        subpanel.__init__(self)
        self.ui = Ui_vehicleStatus()
        self.ui.setupUi(self)
        
        self.ui.horizontalScrollBar.setValue(50)
        self.ui.verticalScrollBar.setValue(50)
        self.ui.horizontalSlider.setValue(50)
        self.ui.verticalSlider.setValue(50)
        self.ui.horizontalScrollBar.valueChanged.connect(self.yaw)

        self.scene = QtGui.QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        self.image = QtGui.QPixmap("./resources/Dial.png")
    
    #def resizeEvent(self, event):
    #    self.displayVehicle()
        
    def displayVehicle(self):
        width = self.ui.graphicsView.width()
        height = self.ui.graphicsView.height()
        scaledImage = self.image.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        
    def start(self, subPanelName):
        width = self.ui.graphicsView.width()
        height = self.ui.graphicsView.height()
        scaledImage = self.image.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.scene.addPixmap(scaledImage)
        self.ui.graphicsView.show()
        
    def yaw(self, value):
        self.ui.graphicsView.rotate(value)