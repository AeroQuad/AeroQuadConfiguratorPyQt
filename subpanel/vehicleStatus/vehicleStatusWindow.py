# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vehicleStatusWindow.ui'
#
# Created: Wed Dec 12 02:05:17 2012
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
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 4, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 3, 1, 1)
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
        self.gridLayout.addWidget(self.artificialHorizon, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 2, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 3, 0, 1, 1)
        self.horizontalScrollBar = QtGui.QScrollBar(vehicleStatus)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName(_fromUtf8("horizontalScrollBar"))
        self.gridLayout.addWidget(self.horizontalScrollBar, 1, 0, 1, 1)
        self.verticalScrollBar = QtGui.QScrollBar(vehicleStatus)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.gridLayout.addWidget(self.verticalScrollBar, 0, 1, 1, 1)
        self.horizontalScrollBarCompass = QtGui.QScrollBar(vehicleStatus)
        self.horizontalScrollBarCompass.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBarCompass.setObjectName(_fromUtf8("horizontalScrollBarCompass"))
        self.gridLayout.addWidget(self.horizontalScrollBarCompass, 2, 0, 1, 1)

        self.retranslateUi(vehicleStatus)
        QtCore.QMetaObject.connectSlotsByName(vehicleStatus)

    def retranslateUi(self, vehicleStatus):
        vehicleStatus.setWindowTitle(QtGui.QApplication.translate("vehicleStatus", "Form", None, QtGui.QApplication.UnicodeUTF8))

