# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuWindow.ui'
#
# Created: Sun Mar 17 16:36:33 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName(_fromUtf8("Menu"))
        Menu.resize(800, 600)
        self.gridLayout = QtGui.QGridLayout(Menu)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splash = QtGui.QLabel(Menu)
        self.splash.setMaximumSize(QtCore.QSize(800, 250))
        self.splash.setText(_fromUtf8(""))
        self.splash.setPixmap(QtGui.QPixmap(_fromUtf8(":/AQ/AeroQuadLogo3.png")))
        self.splash.setScaledContents(True)
        self.splash.setObjectName(_fromUtf8("splash"))
        self.gridLayout.addWidget(self.splash, 0, 0, 1, 1)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QtGui.QApplication.translate("Menu", "Form", None, QtGui.QApplication.UnicodeUTF8))

