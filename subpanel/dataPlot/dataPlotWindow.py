# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataPlotWindow.ui'
#
# Created: Fri Nov 23 10:24:31 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from pyqtgraph import PlotWidget
from collections import deque
from subpanel.subPanelTemplate import subpanel

import pyqtgraph as pg
import numpy as np

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_plotWindow(QtGui.QWidget, subpanel):
    def setupUi(self, plotWindow, commTransport):
        plotWindow.setObjectName(_fromUtf8("plotWindow"))
        plotWindow.resize(818, 418)
        self.gridLayout = QtGui.QGridLayout(plotWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = PlotWidget(plotWindow)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.retranslateUi(plotWindow)
        QtCore.QMetaObject.connectSlotsByName(plotWindow)
        
        self.serialComm = commTransport
        self.graphicsView.hideAxis('bottom')
        self.graphicsView.getAxis('left').setWidth(100)
        
        # custom code added
        '''
        self.dataPlot.hideAxis('bottom')
        self.dataPlot.showGrid(y=True)
        self.dataPlot.getAxis('left').setWidth(100)
        
        plotSize = 256
        self.plotCount = 6

        self.output = []
        for i in range(self.plotCount):
            self.output.append(deque([0.0]*plotSize))
            
        self.axis = deque(range(plotSize))
        self.value = plotSize
        '''

    def retranslateUi(self, plotWindow):
        plotWindow.setWindowTitle(QtGui.QApplication.translate("plotWindow", "Form", None, QtGui.QApplication.UnicodeUTF8))

    def readContinuousData(self, serialComm):
        '''
        while 1:
            if self.exitReadData == True:
                break
            self.value += 1
            self.axis.popleft()
            self.axis.append(self.value)
            outputAxis = list(self.axis)
            
            self.dataPlot.clear()
            for i in range(self.plotCount):
                self.output[i].popleft()
                self.output[i].append(np.random.normal() + (i*3))
                self.dataPlot.plot(x=outputAxis, y=list(self.output[i]), pen=(i,self.plotCount))
        '''
