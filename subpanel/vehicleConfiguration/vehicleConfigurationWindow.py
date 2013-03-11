# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vehicleConfigurationWindow.ui'
#
# Created: Sun Mar 03 23:27:20 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_vehicleConfiguration(object):
    def setupUi(self, vehicleConfiguration):
        vehicleConfiguration.setObjectName(_fromUtf8("vehicleConfiguration"))
        vehicleConfiguration.resize(589, 304)
        vehicleConfiguration.setStyleSheet(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(vehicleConfiguration)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.configView = QtGui.QLabel(vehicleConfiguration)
        self.configView.setMinimumSize(QtCore.QSize(0, 0))
        self.configView.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 0);"))
        self.configView.setText(_fromUtf8(""))
        self.configView.setObjectName(_fromUtf8("configView"))
        self.gridLayout.addWidget(self.configView, 0, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.updateButton = QtGui.QPushButton(vehicleConfiguration)
        self.updateButton.setObjectName(_fromUtf8("updateButton"))
        self.gridLayout.addWidget(self.updateButton, 1, 4, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        self.configSpecs = QtGui.QTableWidget(vehicleConfiguration)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.configSpecs.setFont(font)
        self.configSpecs.setStyleSheet(_fromUtf8("background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.0397727, stop:0 rgba(100, 100, 100, 255), stop:1 rgba(36, 36, 36, 255))\n"
""))
        self.configSpecs.setFrameShape(QtGui.QFrame.Box)
        self.configSpecs.setFrameShadow(QtGui.QFrame.Plain)
        self.configSpecs.setLineWidth(1)
        self.configSpecs.setAlternatingRowColors(False)
        self.configSpecs.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.configSpecs.setShowGrid(False)
        self.configSpecs.setGridStyle(QtCore.Qt.NoPen)
        self.configSpecs.setWordWrap(False)
        self.configSpecs.setCornerButtonEnabled(False)
        self.configSpecs.setObjectName(_fromUtf8("configSpecs"))
        self.configSpecs.setColumnCount(0)
        self.configSpecs.setRowCount(0)
        self.configSpecs.horizontalHeader().setVisible(False)
        self.configSpecs.horizontalHeader().setCascadingSectionResizes(True)
        self.configSpecs.horizontalHeader().setStretchLastSection(True)
        self.configSpecs.verticalHeader().setVisible(False)
        self.configSpecs.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.configSpecs, 0, 3, 1, 2)

        self.retranslateUi(vehicleConfiguration)
        QtCore.QMetaObject.connectSlotsByName(vehicleConfiguration)

    def retranslateUi(self, vehicleConfiguration):
        vehicleConfiguration.setWindowTitle(QtGui.QApplication.translate("vehicleConfiguration", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.updateButton.setText(QtGui.QApplication.translate("vehicleConfiguration", "Update", None, QtGui.QApplication.UnicodeUTF8))

