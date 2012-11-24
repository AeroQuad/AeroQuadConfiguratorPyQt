'''
Created on Nov 21, 2012

@author: Ted Carancho
'''

from PyQt4 import QtGui
from collections import deque
from subpanel.subPanelTemplate import subpanel

import pyqtgraph as pg
import numpy as np

class dataPlot(subpanel):
    def __init__(self):
        win = pg.GraphicsWindow(title="Plot Data")
        win.resize(800,600)
        dataPlot = win.addPlot(title="Sensor Data")
        dataPlot.hideAxis('bottom')
        dataPlot.showGrid(y=True)
        
        plotSize = 256
        self.plotCount = 6

        self.output = []
        for i in range(self.plotCount):
            self.output.append(deque([0.0]*plotSize))
            
        self.axis = deque(range(plotSize))
        self.value = plotSize
        
def readContinuousData(self, serialComm):
    while 1:
        if self.exitReadData == True:
            break
        self.value += 1
        self.axis.popleft()
        self.axis.append(self.value)
        
        dataPlot.clear()
        for i in range(self.plotCount):
            self.output[i].popleft()
            self.output[i].append(np.random.normal() + (i*3))
            dataPlot.plot(x=list(self.axis), y=list(self.output[i]), pen=(i,self.plotCount))
