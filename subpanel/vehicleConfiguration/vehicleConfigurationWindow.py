# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vehicleConfigurationWindow.ui'
#
# Created: Wed Dec 05 02:28:40 2012
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
        vehicleConfiguration.resize(400, 300)
        vehicleConfiguration.setStyleSheet(_fromUtf8("background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.0397727, stop:0 rgba(12, 57, 106, 255), stop:1 rgba(25, 134, 193, 255))"))
        self.gridLayout = QtGui.QGridLayout(vehicleConfiguration)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.configView = QtGui.QLabel(vehicleConfiguration)
        self.configView.setMinimumSize(QtCore.QSize(0, 0))
        self.configView.setObjectName(_fromUtf8("configView"))
        self.gridLayout.addWidget(self.configView, 0, 0, 1, 1)
        self.configSpecs = QtGui.QTreeWidget(vehicleConfiguration)
        self.configSpecs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.configSpecs.setObjectName(_fromUtf8("configSpecs"))
        self.configSpecs.headerItem().setText(0, _fromUtf8("1"))
        self.configSpecs.header().setVisible(False)
        self.gridLayout.addWidget(self.configSpecs, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)

        self.retranslateUi(vehicleConfiguration)
        QtCore.QMetaObject.connectSlotsByName(vehicleConfiguration)

    def retranslateUi(self, vehicleConfiguration):
        vehicleConfiguration.setWindowTitle(QtGui.QApplication.translate("vehicleConfiguration", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.configView.setText(QtGui.QApplication.translate("vehicleConfiguration", "Configuration View", None, QtGui.QApplication.UnicodeUTF8))

