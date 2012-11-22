# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataPlot.ui'
#
# Created: Mon Nov 19 01:23:30 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from subpanel.subPanelTemplate import subpanel

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_plotWindow(QtGui.QWidget, subpanel):
    def setupUi(self, plotWindow, commTransport):
        self.serialComm = commTransport
        plotWindow.setObjectName(_fromUtf8("plotWindow"))
        plotWindow.resize(579, 386)
        self.gridLayout = QtGui.QGridLayout(plotWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(plotWindow)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 3, 1, 1)
        self.checkBox = QtGui.QCheckBox(plotWindow)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 1, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.scrollArea = QtGui.QScrollArea(plotWindow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 134, 291))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.listView = QtGui.QListView(self.scrollAreaWidgetContents_2)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout_2.addWidget(self.listView, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea, 0, 3, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(plotWindow)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 2, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
        #self.widget = dataPlot(plotWindow)
        #self.widget.setObjectName(_fromUtf8("widget"))
        #self.gridLayout.addWidget(self.widget, 0, 0, 3, 3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)

        self.retranslateUi(plotWindow)
        QtCore.QMetaObject.connectSlotsByName(plotWindow)


    def retranslateUi(self, plotWindow):
        plotWindow.setWindowTitle(QtGui.QApplication.translate("plotWindow", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("plotWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("plotWindow", "Select All Plots", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("plotWindow", "Auto Scale", None, QtGui.QApplication.UnicodeUTF8))
