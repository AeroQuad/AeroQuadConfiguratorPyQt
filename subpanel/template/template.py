# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splashScreen.ui'
#
# Created: Thu Nov  8 12:08:29 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

# Read through the comments below to know how to update your GUI
# made in QT Designer as a subpanel in the Configurator

from PyQt4 import QtCore, QtGui

# Add this to your subpanel
from subpanel.subPanelTemplate import subpanel

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_template(QtGui.QWidget, subpanel):
    # Modify setupUi to add commTransport as an argument
    def setupUi(self, splashScreen, commTransport):
        # Add the line below to save a variable for communication to the AeroQuad
        self.serialComm = commTransport
        
        splashScreen.setObjectName(_fromUtf8("splashScreen"))
        splashScreen.resize(818, 418)
        self.gridLayout = QtGui.QGridLayout(splashScreen)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splash = QtGui.QLabel(splashScreen)
        self.splash.setMaximumSize(QtCore.QSize(800, 400))
        self.splash.setText(_fromUtf8(""))
        self.splash.setPixmap(QtGui.QPixmap(_fromUtf8(":/AQ/AeroQuad_1024x500.png")))
        self.splash.setScaledContents(True)
        self.splash.setObjectName(_fromUtf8("splash"))
        self.gridLayout.addWidget(self.splash, 0, 0, 1, 1)

        self.retranslateUi(splashScreen)
        QtCore.QMetaObject.connectSlotsByName(splashScreen)

    def retranslateUi(self, splashScreen):
        splashScreen.setWindowTitle(QtGui.QApplication.translate("splashScreen", "Form", None, QtGui.QApplication.UnicodeUTF8))

# Add any function calls you wish to redefine/customize in the subpanel class
# Or you can add any new function calls you need to make the subpanel operate

import AQresources_rc
