'''
Created on Nov 21, 2012

@author: Ted Carancho
'''

from PyQt4 import QtGui, QtCore
from collections import deque
from subpanel.subPanelTemplate import subpanel
from subpanel.dataPlot.dataPlotWindow import Ui_plotWindow
import pyqtgraph as pg

class dataPlot(QtGui.QWidget, subpanel):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_plotWindow()
        self.ui.setupUi(self)
        self.ui.graphicsView.hideAxis('bottom')
        self.ui.graphicsView.showGrid(y=True)
        self.ui.graphicsView.getAxis('top').setHeight(10)
        self.ui.graphicsView.getAxis('bottom').setHeight(10)
                
        plotSize = 128
        self.plotCount = 6

        self.output = []
        for i in range(self.plotCount):
            self.output.append(deque([0.0]*plotSize))
            
        self.axis = deque(range(plotSize))
        self.value = plotSize
        
        legend = pg.LegendItem((100,100), (60,10))
        legend.setParentItem(self.ui.graphicsView.graphicsItem())
        channel = 0
        for i in range(self.plotCount):
            plotRef = self.ui.graphicsView.plot(x=[0.0], y=[0.0], pen=(i,self.plotCount))
            channel += 1
            plotName = "Channel " + str(channel)
            legend.addItem(plotRef, plotName)

    def initialize(self, commTransport):
        self.serialComm = commTransport
        
    def start(self):
        '''This method starts a new thread dedicated to reading serial communication'''
        self.isConnected()
        if self.connected == True:
            self.exitReadData = False
            self.serialComm.write("i")
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.readContinuousData)
            self.timer.start(50)
            
    def readContinuousData(self):
        if self.exitReadData == False:            
            rawData = self.serialComm.read()
            data = rawData.split(",")
            self.ui.graphicsView.clear()
            for i in range(self.plotCount):
                self.output[i].popleft()
                self.output[i].append(float(data[i]))
                self.ui.graphicsView.plot(y=list(self.output[i]), pen=(i,self.plotCount))
                
    def stop(self):
        '''This method enables a flag which closes the continuous serial read thread'''
        self.exitReadData = True
        self.timer.stop()
        self.timer.timeout.disconnect(self.readContinuousData)