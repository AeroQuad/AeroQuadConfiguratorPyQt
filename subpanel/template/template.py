# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splashScreen.ui'
#
# Created: Thu Nov  8 12:08:29 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

import time
from PyQt4 import QtCore, QtGui
from threading import Thread

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_template(QtGui.QWidget):
    def setupUi(self, splashScreen, commTransport):
        self.serialComm = commTransport
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
    
    def start(self):
        # Start thread to read incoming messages
        self.exitReadData = False
        #thread = Thread(target=self.readData, args=[self.serialComm])
        #thread.start()
        print("subpanel started")
        
    def stop(self):
        self.exitReadData = True
        print("subpanel stopped")
        
    def readData(self, serialComm):
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
                
import AQresources_rc
