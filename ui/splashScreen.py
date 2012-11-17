# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splashScreen.ui'
#
# Created: Thu Nov  8 12:08:29 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_splashScreen(QtGui.QWidget):
    def setupUi(self, splashScreen):
        splashScreen.setObjectName(_fromUtf8("splashScreen"))
        splashScreen.resize(818, 418)
        self.gridLayout = QtGui.QGridLayout(splashScreen)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splash = QtGui.QLabel(splashScreen)
        self.splash.setMaximumSize(QtCore.QSize(800, 400))
        self.splash.setText(_fromUtf8(""))
        self.splash.setPixmap(QtGui.QPixmap(_fromUtf8("resources/AeroQuad_1024x500.png")))
        self.splash.setScaledContents(True)
        self.splash.setObjectName(_fromUtf8("splash"))
        self.gridLayout.addWidget(self.splash, 0, 0, 1, 1)

        self.retranslateUi(splashScreen)
        QtCore.QMetaObject.connectSlotsByName(splashScreen)

    def retranslateUi(self, splashScreen):
        splashScreen.setWindowTitle(QtGui.QApplication.translate("splashScreen", "Form", None, QtGui.QApplication.UnicodeUTF8))

import AQresources_rc
