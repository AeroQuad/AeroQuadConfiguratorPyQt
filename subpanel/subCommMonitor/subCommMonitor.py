# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subCommMonitor.ui'
#
# Created: Sat Nov 10 12:22:32 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

import time
from PyQt4 import QtCore, QtGui
from subpanel.subPanelTemplate import subpanel

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_commMonitor(QtGui.QWidget, subpanel):
    def setupUi(self, commMonitor, commTransport):
        self.serialComm = commTransport
        commMonitor.setObjectName(_fromUtf8("commMonitor"))
        commMonitor.resize(818, 418)
        self.gridLayout = QtGui.QGridLayout(commMonitor)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.clearButton = QtGui.QPushButton(commMonitor)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.gridLayout.addWidget(self.clearButton, 1, 2, 1, 1)
        self.sendButton = QtGui.QPushButton(commMonitor)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.gridLayout.addWidget(self.sendButton, 1, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(commMonitor)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.commLog = QtGui.QTextBrowser(commMonitor)
        self.commLog.setFrameShadow(QtGui.QFrame.Sunken)
        self.commLog.setObjectName(_fromUtf8("commLog"))
        self.gridLayout.addWidget(self.commLog, 0, 0, 1, 3)
        self.retranslateUi(commMonitor)
        QtCore.QMetaObject.connectSlotsByName(commMonitor)
                
        # Connect GUI slots and signals
        self.sendButton.clicked.connect(self.sendCommand)
        self.clearButton.clicked.connect(self.clearComm)
        
    def retranslateUi(self, commMonitor):
        commMonitor.setWindowTitle(QtGui.QApplication.translate("commMonitor", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setText(QtGui.QApplication.translate("commMonitor", "Send Command", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("commMonitor", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setAutoDefault(True)

    def sendCommand(self):
        command = self.lineEdit.text()
        self.serialComm.write(command)
        self.commLog.append(self.timeStamp() + " -> " + command)
        self.lineEdit.clear()
        time.sleep(0.150)
        
    def readContinuousData(self, serialComm):
        self.comm = serialComm
        while 1:
            if self.exitReadData == True:
                break
            # TODO: Need to figure out how to clear out text when too large
            #if self.commLog.toPlainText().__len__() > 1024:
            #    time.sleep(0.250)
            #    self.commLog.clear()
            response = self.comm.read()
            if response != "":
                self.commLog.append(self.timeStamp() + " <- " + response)
                self.commLog.ensureCursorVisible()
                time.sleep(0.050)
            else:
                time.sleep(0.250)
                self.commLog.ensureCursorVisible()
       
    def isConnected(self):
        state = self.serialComm.isConnected()
        self.sendButton.setEnabled(state)
        self.clearButton.setEnabled(state)
        self.connected = state
        
    def clearComm(self):
        self.lineEdit.clear()
        self.commLog.clear()

