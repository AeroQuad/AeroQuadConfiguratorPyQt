'''
Created on Nov 21, 2012

@author: Ted Carancho
'''

from PyQt4 import QtGui, QtCore
from pyqtgraph import PlotCurveItem

from subpanel.subPanel import SubPanel
from subpanel.dataPlot.dataPlotWindow import Ui_plotWindow


class dataPlot(QtGui.QWidget, SubPanel):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        SubPanel.__init__(self)

        self.ui = Ui_plotWindow()
        self.ui.setupUi(self)

    def start(self, xmlSubPanel, boardConfiguration):
        '''This method starts a timer used for any long running loops in a subpanel'''
        self.xmlSubPanel = xmlSubPanel
        self.boardConfiguration = boardConfiguration

        self.plotIndex = int(self.xml.find(self.xmlSubPanel + '/Index').text)
        plotSize = int(self.xml.find(self.xmlSubPanel + '/PlotSize').text)
        plotNames = self.xml.findall(self.xmlSubPanel + '/PlotName')
        self.plotCount = len(plotNames)

        self.ui.graphicsView.setRange(xRange=(0, plotSize), padding=0.0)
        self.ui.graphicsView.clear()
        self.ui.treeWidget.clear()

        self.data, self.curves, colors = [], [], [
            QtGui.QColor('blue'),
            QtGui.QColor('red'),
            QtGui.QColor('lime'),
            QtGui.QColor('cornflowerblue'),
            QtGui.QColor('greenyellow'),
            QtGui.QColor('violet'),
            QtGui.QColor('orange'),
            QtGui.QColor('deepskyblue'),
            QtGui.QColor('firebrick'),
            QtGui.QColor('aqua')
        ]
        
        for i in xrange(self.plotCount):
            self.data.append([0.0] * plotSize)
            self.curves.append(
                PlotCurveItem(self.data[i], pen={'color':colors[i], 'width': 2})
            )
            self.ui.graphicsView.addItem(self.curves[i])

            plotName = plotNames[i].text
            newLine = QtGui.QTreeWidgetItem(self.ui.treeWidget)
            newLine.setCheckState(0, 2)
            newLine.setBackgroundColor(0, colors[i])
            newLine.setText(1, plotName + '   ')
            newLine.setText(2, '0.000')
        
        self.ui.treeWidget.resizeColumnToContents(0)
        self.ui.treeWidget.resizeColumnToContents(1)
        self.legend = self.ui.treeWidget.invisibleRootItem()

        if self.comm.isConnected() == True:
            telemetry = self.xml.find(self.xmlSubPanel + '/Telemetry').text
            if telemetry != '':
                self.comm.write(telemetry)
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.readContinuousData)
            self.timer.start(50)
            self.startCommThread()

        self.plot_timer = QtCore.QTimer()
        self.plot_timer.timeout.connect(self.update_plot)
        self.plot_timer.start(100)

    def readContinuousData(self):
        '''This method continually reads telemetry from the AeroQuad'''
        if self.comm.isConnected() and not self.commData.empty():
            rawData = self.commData.get()
            data = rawData.split(',')

            for i in xrange(self.plotCount):
                legendRow = self.legend.child(i)
                if legendRow.checkState(0) == 2:
                    try:
                        dataValue = data[i + self.plotIndex]
                        self.data[i].insert(0, float(dataValue))
                        self.data[i].pop()
                        legendRow.setText(2, dataValue)
                    except:
                        pass # Do not update output data if invalid number detected from comm read

    def update_plot(self):
        for i in xrange(self.plotCount):
            legendRow = self.legend.child(i)
            if legendRow.checkState(0) == 2:
                self.curves[i].setData(self.data[i])
                if self.curves[i] not in self.ui.graphicsView.items():
                    self.ui.graphicsView.addItem(self.curves[i])
            else:
                if self.curves[i] in self.ui.graphicsView.items():
                    self.ui.graphicsView.removeItem(self.curves[i])
        self.ui.graphicsView.autoRange()
