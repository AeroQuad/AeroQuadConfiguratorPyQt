# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vehicleStatusWindow.ui'
#
# Created: Sun Mar 03 23:11:54 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class VehicleOverallStatusPanel(object):
    def setupUi(self, vehicleStatus):
        vehicleStatus.setObjectName(_fromUtf8("VehicleOverallStatusPanel"))
        vehicleStatus.resize(800, 600)
        self.gridLayout = QtGui.QGridLayout(vehicleStatus)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.motorView = QtGui.QGraphicsView(vehicleStatus)
        self.motorView.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.motorView.setFrameShape(QtGui.QFrame.NoFrame)
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
        self.leftTransmitter.setFrameShape(QtGui.QFrame.Box)
        self.leftTransmitter.setFrameShadow(QtGui.QFrame.Plain)
        self.leftTransmitter.setLineWidth(2)
        self.leftTransmitter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.leftTransmitter.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.leftTransmitter.setObjectName(_fromUtf8("leftTransmitter"))
        self.gridLayout.addWidget(self.leftTransmitter, 1, 0, 1, 1)
        self.artificialHorizon = QtGui.QGraphicsView(vehicleStatus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.artificialHorizon.sizePolicy().hasHeightForWidth())
        self.artificialHorizon.setSizePolicy(sizePolicy)
        self.artificialHorizon.setMinimumSize(QtCore.QSize(300, 300))
        self.artificialHorizon.setMaximumSize(QtCore.QSize(300, 300))
        self.artificialHorizon.setFrameShape(QtGui.QFrame.Box)
        self.artificialHorizon.setFrameShadow(QtGui.QFrame.Plain)
        self.artificialHorizon.setLineWidth(2)
        self.artificialHorizon.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.artificialHorizon.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.artificialHorizon.setObjectName(_fromUtf8("artificialHorizon"))
        self.gridLayout.addWidget(self.artificialHorizon, 0, 0, 1, 2)
        self.rightTransmitter = QtGui.QGraphicsView(vehicleStatus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightTransmitter.sizePolicy().hasHeightForWidth())
        self.rightTransmitter.setSizePolicy(sizePolicy)
        self.rightTransmitter.setMinimumSize(QtCore.QSize(147, 150))
        self.rightTransmitter.setMaximumSize(QtCore.QSize(147, 150))
        self.rightTransmitter.setFrameShape(QtGui.QFrame.Box)
        self.rightTransmitter.setFrameShadow(QtGui.QFrame.Plain)
        self.rightTransmitter.setLineWidth(2)
        self.rightTransmitter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rightTransmitter.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rightTransmitter.setObjectName(_fromUtf8("rightTransmitter"))
        self.gridLayout.addWidget(self.rightTransmitter, 1, 1, 1, 1)
        self.transmitterOutput = QtGui.QGraphicsView(vehicleStatus)
        self.transmitterOutput.setMaximumSize(QtCore.QSize(16777215, 300))
        self.transmitterOutput.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0.548, y1:0.0170455, x2:0.548, y2:1, stop:0 rgba(30, 30, 30, 255), stop:1 rgba(66, 66, 66, 255))"))
        self.transmitterOutput.setFrameShape(QtGui.QFrame.Box)
        self.transmitterOutput.setFrameShadow(QtGui.QFrame.Plain)
        self.transmitterOutput.setLineWidth(2)
        self.transmitterOutput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.transmitterOutput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.transmitterOutput.setObjectName(_fromUtf8("transmitterOutput"))
        self.gridLayout.addWidget(self.transmitterOutput, 2, 0, 1, 2)

        self.retranslateUi(vehicleStatus)
        QtCore.QMetaObject.connectSlotsByName(vehicleStatus)

    def retranslateUi(self, vehicleStatus):
        vehicleStatus.setWindowTitle(QtGui.QApplication.translate("vehicleStatus", "AeroQuad Configurator", None, QtGui.QApplication.UnicodeUTF8))

