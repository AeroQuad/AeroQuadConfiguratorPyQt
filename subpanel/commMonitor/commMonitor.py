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
from subpanel.commMonitor.commMonitorWindow import Ui_commMonitor

class commMonitor(QtGui.QWidget, subpanel):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        subpanel.__init__(self)
        self.ui = Ui_commMonitor()
        self.ui.setupUi(self)
        self.ui.sendButton.setEnabled(False)
        self.ui.clearButton.setEnabled(False)
                
        # Connect GUI slots and signals
        self.ui.sendButton.clicked.connect(self.sendCommand)
        self.ui.clearButton.clicked.connect(self.clearComm)
        
    def start(self, xmlSubPanel):
        '''This method starts a timer used for any long running loops in a subpanel'''
        if self.comm.isConnected() == True:
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.readContinuousData)
            self.timer.start(50)
            
    def sendCommand(self):
        command = str(self.ui.lineEdit.text())
        self.comm.write(command)
        self.ui.commLog.append(self.timeStamp() + " -> " + command)
        self.ui.lineEdit.clear()
        time.sleep(0.150)
        
    #def readContinuousData(self, serialComm):
    #    self.comm = serialComm
    #    while 1:
    #        if self.exitReadData == True:
    #            break
            # TODO: Need to figure out how to clear out text when too large
            #if self.commLog.toPlainText().__len__() > 1024:
            #    time.sleep(0.250)
            #    self.commLog.clear()
    #        response = self.comm.read()
    #        if response != "":
    #            self.commLog.append(self.timeStamp() + " <- " + response)
    #            self.commLog.ensureCursorVisible()
    #            time.sleep(0.050)
    #        else:
    #            time.sleep(0.250)
    #            self.commLog.ensureCursorVisible()
    
    def readContinuousData(self):
        '''This method continually reads telemetry from the AeroQuad'''
        isConnected = self.comm.isConnected()
        self.ui.sendButton.setEnabled(isConnected)
        self.ui.clearButton.setEnabled(isConnected)
        if isConnected == True: 
            if self.comm.dataAvailable():           
                response = self.comm.read()
                self.ui.commLog.append(self.timeStamp() + " <- " + response)
                self.ui.commLog.ensureCursorVisible()
        
    def clearComm(self):
        self.ui.lineEdit.clear()
        self.ui.commLog.clear()

