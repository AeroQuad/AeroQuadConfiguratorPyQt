'''
Created on Dec 5, 2012

@author: Ted Carancho
'''

from PyQt4 import QtCore, QtGui
from subpanel.subPanelTemplate import subpanel
from subpanel.vehicleConfiguration.vehicleConfigurationWindow import Ui_vehicleConfiguration

class vehicleConfiguration(QtGui.QWidget, subpanel):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        subpanel.__init__(self)
        self.ui = Ui_vehicleConfiguration()
        self.ui.setupUi(self)
        
        self.configView = QtGui.QLabel(self.ui.configView)
        self.image = QtGui.QPixmap("./resources/QuadX.png")
        w = min(self.image.width(),  self.ui.configView.width());
        h = min(self.image.height(), self.ui.configView.height());
        #scaledImage = self.image.scaled(QtCore.QSize(w, h), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        #self.configView.setPixmap(scaledImage)

    def resizeEvent(self, evt=None):
        #image = QtGui.QPixmap("./resources/QuadX.png")
        w = min(self.image.width(),  self.ui.configView.width());
        h = min(self.image.height(), self.ui.configView.height());
        scaledImage = self.image.scaled(QtCore.QSize(w, h), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.ui.configView.setPixmap(scaledImage)