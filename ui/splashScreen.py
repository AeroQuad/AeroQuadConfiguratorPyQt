# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splashScreen.ui'
#
# Created: Sat Dec 15 02:33:08 2012
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
        splashScreen.resize(818, 600)
        splashScreen.setStyleSheet(_fromUtf8("background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.0397727, stop:0 rgba(12, 57, 106, 255), stop:1 rgba(25, 134, 193, 255))"))
        self.gridLayout = QtGui.QGridLayout(splashScreen)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splash = QtGui.QLabel(splashScreen)
        self.splash.setMaximumSize(QtCore.QSize(800, 400))
        self.splash.setStyleSheet(_fromUtf8("background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.0397727, stop:0 rgba(12, 57, 106, 255), stop:1 rgba(25, 134, 193, 255))"))
        self.splash.setText(_fromUtf8(""))
        self.splash.setPixmap(QtGui.QPixmap(_fromUtf8(":/AQ/AeroQuad_1024x500.png")))
        self.splash.setScaledContents(True)
        self.splash.setObjectName(_fromUtf8("splash"))
        self.gridLayout.addWidget(self.splash, 0, 0, 1, 1)

        self.retranslateUi(splashScreen)
        QtCore.QMetaObject.connectSlotsByName(splashScreen)

    def retranslateUi(self, splashScreen):
        splashScreen.setWindowTitle(QtGui.QApplication.translate("splashScreen", "Form", None, QtGui.QApplication.UnicodeUTF8))

import AQresources_rc
