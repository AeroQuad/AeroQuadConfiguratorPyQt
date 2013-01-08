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

        pg.setConfigOption('antialias', True)
        #pg.setConfigOption('background', (255,255,255))
        pg.setConfigOption('foreground', (128,128,128))
        self.ui = Ui_plotWindow()
        self.ui.setupUi(self)
        self.ui.graphicsView.hideAxis('bottom')
        self.ui.graphicsView.getAxis('top').setHeight(10)
        self.ui.graphicsView.getAxis('bottom').setHeight(10)
        self.ui.graphicsView.getAxis('left').setWidth(50)
        self.ui.graphicsView.setBackground((255,255,255))
        self.ui.graphicsView.setRange(xRange=(0,128))
        self.plotCount = 0
        self.legend = None
        self.colors = [QtGui.QColor('blue'),
                       QtGui.QColor('red'),
                       QtGui.QColor('lime'),
                       QtGui.QColor('cornflowerblue'),
                       QtGui.QColor('greenyellow'),
                       QtGui.QColor('violet'),
                       QtGui.QColor('orange'),
                       QtGui.QColor('deepskyblue'),
                       QtGui.QColor('firebrick'),
                       QtGui.QColor('aqua')]
        
    def start(self, xmlSubPanel, boardConfiguration):
        '''This method starts a timer used for any long running loops in a subpanel'''
        self.xmlSubPanel = xmlSubPanel
        self.boardConfiguration = boardConfiguration
    
        self.plotIndex = int(self.xml.find(self.xmlSubPanel + "/Index").text)            
        plotSize = int(self.xml.find(self.xmlSubPanel + "/PlotSize").text)
        plotNames = self.xml.findall(self.xmlSubPanel + "/PlotName")
        self.plotCount = len(plotNames)

        self.output = []
        self.curves = []
        for i in range(self.plotCount):
            self.output.append(deque([0.0] * plotSize))
            self.curves.append(self.ui.graphicsView.plot(self.output[i], pen=pg.mkPen(self.colors[i], width=2)))
            
        self.axis = deque(range(plotSize))
        self.value = plotSize
        
        self.ui.treeWidget.clear()
        for i in range(self.plotCount):
            plotName = plotNames[i].text
            newLine = QtGui.QTreeWidgetItem(self.ui.treeWidget)
            newLine.setCheckState(0, 2)
            newLine.setBackgroundColor(0, self.colors[i])
            newLine.setText(1, plotName + "   ")
            newLine.setText(2, "0.000")
        self.ui.treeWidget.resizeColumnToContents(0)
        self.ui.treeWidget.resizeColumnToContents(1)
        self.legend = self.ui.treeWidget.invisibleRootItem()

        if self.comm.isConnected() == True:
            telemetry = self.xml.find(self.xmlSubPanel + "/Telemetry").text
            if telemetry != "":
                self.comm.write(telemetry)
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.readContinuousData)
            self.timer.start(100)

        self.plot_timer = QtCore.QTimer()
        self.plot_timer.timeout.connect(self.update_plot)
        self.plot_timer.start(20)

    def readContinuousData(self):
        '''This method continually reads telemetry from the AeroQuad'''
        if self.comm.isConnected() == True: 
            if self.comm.dataAvailable():           
                rawData = self.comm.read()
                data = rawData.split(",")  
                                 
                for i in range(self.plotCount):
                    legendRow = self.legend.child(i)
                    if legendRow.checkState(0) == 2:
                        try:
                            dataValue = data[i + self.plotIndex]
                            self.output[i].appendleft(float(dataValue))
                            self.output[i].pop()
                        except:
                            pass # Do not update output data if invalid number detected from comm read
                        legendRow.setText(2, dataValue)
    
    def update_plot(self):
        for i in range(self.plotCount):
            legendRow = self.legend.child(i)
            if legendRow.checkState(0) == 2:
                self.curves[i].setData(self.output[i])
            else:
                self.curves[i].clear()

