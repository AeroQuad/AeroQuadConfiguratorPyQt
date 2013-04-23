'''
Created on 22 apr. 2013

@author: Erik
'''

from PyQt4 import QtGui
from ui.subpanel.BasePanelController import BasePanelController
from ui.subpanel.sensorscalibration.SensorsCalibrationPanel import ReceiverChannelDetectionPanel

class SensorsCalibrationController(QtGui.QWidget, BasePanelController):


    def __init__(self):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        self.ui = ReceiverChannelDetectionPanel()
        self.ui.setupUi(self)

        pictureScene = QtGui.QGraphicsScene()
        pictureBackground = QtGui.QPixmap("./resources/calfront.png")
        pictureItem = QtGui.QGraphicsPixmapItem(pictureBackground)
        pictureScene.addItem(pictureItem)
        self.ui.picture.setScene(pictureScene)
        