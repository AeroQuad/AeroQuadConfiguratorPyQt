# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataPlotWindow.ui'
#
# Created: Tue Nov 27 14:21:15 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_plotWindow(object):
    def setupUi(self, plotWindow):
        plotWindow.setObjectName(_fromUtf8("plotWindow"))
        plotWindow.resize(579, 386)
        self.gridLayout = QtGui.QGridLayout(plotWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = PlotWidget(plotWindow)
        self.graphicsView.setFrameShape(QtGui.QFrame.StyledPanel)
        self.graphicsView.setFrameShadow(QtGui.QFrame.Plain)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.retranslateUi(plotWindow)
        QtCore.QMetaObject.connectSlotsByName(plotWindow)

    def retranslateUi(self, plotWindow):
        plotWindow.setWindowTitle(QtGui.QApplication.translate("plotWindow", "Form", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
