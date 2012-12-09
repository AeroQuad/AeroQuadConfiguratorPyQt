# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vehicleStatusWindow.ui'
#
# Created: Fri Dec 07 01:08:48 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_vehicleStatus(object):
    def setupUi(self, vehicleStatus):
        vehicleStatus.setObjectName(_fromUtf8("vehicleStatus"))
        vehicleStatus.resize(600, 300)
        self.gridLayout = QtGui.QGridLayout(vehicleStatus)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalScrollBar = QtGui.QScrollBar(vehicleStatus)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.gridLayout.addWidget(self.verticalScrollBar, 0, 3, 1, 1)
        self.plotView = PlotWidget(vehicleStatus)
        self.plotView.setFrameShape(QtGui.QFrame.StyledPanel)
        self.plotView.setFrameShadow(QtGui.QFrame.Plain)
        self.plotView.setObjectName(_fromUtf8("plotView"))
        self.gridLayout.addWidget(self.plotView, 0, 0, 1, 1)
        self.horizontalSlider = QtGui.QSlider(vehicleStatus)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.gridLayout.addWidget(self.horizontalSlider, 1, 0, 1, 1)
        self.horizontalScrollBar = QtGui.QScrollBar(vehicleStatus)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName(_fromUtf8("horizontalScrollBar"))
        self.gridLayout.addWidget(self.horizontalScrollBar, 1, 2, 1, 1)
        self.graphicsView = QtGui.QGraphicsView(vehicleStatus)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setResizeAnchor(QtGui.QGraphicsView.AnchorViewCenter)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 2, 1, 1)
        self.verticalSlider = QtGui.QSlider(vehicleStatus)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.gridLayout.addWidget(self.verticalSlider, 0, 1, 1, 1)

        self.retranslateUi(vehicleStatus)
        QtCore.QMetaObject.connectSlotsByName(vehicleStatus)

    def retranslateUi(self, vehicleStatus):
        vehicleStatus.setWindowTitle(QtGui.QApplication.translate("vehicleStatus", "Form", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
