# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CommMonitorPanel.ui'
#
# Created: Wed Apr 24 17:12:26 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CommMonitorPanel(object):
    def setupUi(self, CommMonitorPanel):
        CommMonitorPanel.setObjectName(_fromUtf8("CommMonitorPanel"))
        CommMonitorPanel.resize(818, 418)
        self.gridLayout = QtGui.QGridLayout(CommMonitorPanel)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = QtGui.QLineEdit(CommMonitorPanel)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.sendButton = QtGui.QPushButton(CommMonitorPanel)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.gridLayout.addWidget(self.sendButton, 1, 1, 1, 1)
        self.clearButton = QtGui.QPushButton(CommMonitorPanel)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.gridLayout.addWidget(self.clearButton, 1, 2, 1, 1)
        self.commLog = QtGui.QTextBrowser(CommMonitorPanel)
        self.commLog.setFrameShadow(QtGui.QFrame.Sunken)
        self.commLog.setObjectName(_fromUtf8("commLog"))
        self.gridLayout.addWidget(self.commLog, 0, 0, 1, 3)

        self.retranslateUi(CommMonitorPanel)
        QtCore.QMetaObject.connectSlotsByName(CommMonitorPanel)

    def retranslateUi(self, CommMonitorPanel):
        CommMonitorPanel.setWindowTitle(_translate("CommMonitorPanel", "Form", None))
        self.sendButton.setText(_translate("CommMonitorPanel", "Send Command", None))
        self.clearButton.setText(_translate("CommMonitorPanel", "Clear", None))

