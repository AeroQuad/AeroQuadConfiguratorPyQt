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
        subpanel.__init__(self)
        self.ui = Ui_plotWindow()
        self.ui.setupUi(self)
        self.ui.graphicsView.hideAxis('bottom')
        self.ui.graphicsView.showGrid(y=True)
        self.ui.graphicsView.getAxis('top').setHeight(10)
        self.ui.graphicsView.getAxis('bottom').setHeight(10)
        
    def start(self, xml, xmlSubPanel):
        '''This method starts a timer used for any long running loops in a subpanel'''
        self.xml = xml
        self.xmlSubPanel = xmlSubPanel
    
        self.plotIndex = int(self.xml.find(self.xmlSubPanel + "/Index").text)            
        plotSize = int(self.xml.find(self.xmlSubPanel + "/PlotSize").text)
        plotNames = self.xml.findall(self.xmlSubPanel + "/PlotName")
        self.plotCount = len(plotNames)

        self.output = []
        for i in range(self.plotCount):
            self.output.append(deque([0.0]*plotSize))
            
        self.axis = deque(range(plotSize))
        self.value = plotSize
        legend = pg.LegendItem((100, 10 + 30 * self.plotCount), (60,10))
        legend.setParentItem(self.ui.graphicsView.graphicsItem())
        for i in range(self.plotCount):
            plotRef = self.ui.graphicsView.plot(x=[0.0], y=[0.0], pen=(i,self.plotCount))
            plotName = plotNames[i].text
            legend.addItem(plotRef, plotName)
            
        if self.comm.isConnected() == True:
            telemetry = self.xml.find(self.xmlSubPanel + "/Telemetry").text
            if telemetry != "":
                self.comm.write(telemetry)
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.readContinuousData)
            self.timer.start(50)

    def readContinuousData(self):
        '''This method continually reads telemetry from the AeroQuad'''
        if self.comm.isConnected() == True: 
            if self.comm.dataAvailable():           
                rawData = self.comm.read()
                data = rawData.split(",")
                self.ui.graphicsView.clear()
                for i in range(self.plotCount):
                    self.output[i].popleft()
                    self.output[i].append(float(data[i + self.plotIndex]))
                    self.ui.graphicsView.plot(y=list(self.output[i]), pen=(i,self.plotCount))
