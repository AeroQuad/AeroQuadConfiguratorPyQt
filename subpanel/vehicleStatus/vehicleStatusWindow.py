# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vehicleStatusWindow.ui'
#
# Created: Sun Dec 16 22:34:02 2012
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
        vehicleStatus.resize(800, 600)
        self.gridLayout = QtGui.QGridLayout(vehicleStatus)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.artificialHorizon = QtGui.QGraphicsView(vehicleStatus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.artificialHorizon.sizePolicy().hasHeightForWidth())
        self.artificialHorizon.setSizePolicy(sizePolicy)
        self.artificialHorizon.setMinimumSize(QtCore.QSize(300, 300))
        self.artificialHorizon.setMaximumSize(QtCore.QSize(300, 300))
        self.artificialHorizon.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.artificialHorizon.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.artificialHorizon.setObjectName(_fromUtf8("artificialHorizon"))
        self.gridLayout.addWidget(self.artificialHorizon, 0, 0, 1, 2)
        self.motorView = QtGui.QGraphicsView(vehicleStatus)
        self.motorView.setStyleSheet(_fromUtf8("background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.0397727, stop:0 rgba(12, 57, 106, 255), stop:1 rgba(25, 134, 193, 255))"))
        self.motorView.setObjectName(_fromUtf8("motorView"))
        self.gridLayout.addWidget(self.motorView, 0, 2, 3, 1)
        self.leftTransmitter = QtGui.QGraphicsView(vehicleStatus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftTransmitter.sizePolicy().hasHeightForWidth())
        self.leftTransmitter.setSizePolicy(sizePolicy)
        self.leftTransmitter.setMinimumSize(QtCore.QSize(147, 150))
        self.leftTransmitter.setMaximumSize(QtCore.QSize(147, 150))
        self.leftTransmitter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.leftTransmitter.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.leftTransmitter.setObjectName(_fromUtf8("leftTransmitter"))
        self.gridLayout.addWidget(self.leftTransmitter, 1, 0, 1, 1)
        self.rightTransmitter = QtGui.QGraphicsView(vehicleStatus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightTransmitter.sizePolicy().hasHeightForWidth())
        self.rightTransmitter.setSizePolicy(sizePolicy)
        self.rightTransmitter.setMinimumSize(QtCore.QSize(147, 150))
        self.rightTransmitter.setMaximumSize(QtCore.QSize(147, 150))
        self.rightTransmitter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rightTransmitter.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rightTransmitter.setObjectName(_fromUtf8("rightTransmitter"))
        self.gridLayout.addWidget(self.rightTransmitter, 1, 1, 1, 1)
        self.transmitterOutput = PlotWidget(vehicleStatus)
        self.transmitterOutput.setObjectName(_fromUtf8("transmitterOutput"))
        self.gridLayout.addWidget(self.transmitterOutput, 2, 0, 1, 2)

        self.retranslateUi(vehicleStatus)
        QtCore.QMetaObject.connectSlotsByName(vehicleStatus)

    def retranslateUi(self, vehicleStatus):
        vehicleStatus.setWindowTitle(QtGui.QApplication.translate("vehicleStatus", "AeroQuad Configurator", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
