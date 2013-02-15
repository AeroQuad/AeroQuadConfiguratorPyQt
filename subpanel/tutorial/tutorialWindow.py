# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tutorialWindow.ui'
#
# Created: Fri Feb 15 08:11:10 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_tutorial(object):
    def setupUi(self, tutorial):
        tutorial.setObjectName(_fromUtf8("tutorial"))
        tutorial.resize(400, 300)
        self.label = QtGui.QLabel(tutorial)
        self.label.setGeometry(QtCore.QRect(180, 120, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(tutorial)
        self.pushButton.setGeometry(QtCore.QRect(170, 160, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(tutorial)
        QtCore.QMetaObject.connectSlotsByName(tutorial)

    def retranslateUi(self, tutorial):
        tutorial.setWindowTitle(QtGui.QApplication.translate("tutorial", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("tutorial", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("tutorial", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

