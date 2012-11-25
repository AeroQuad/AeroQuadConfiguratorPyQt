'''
Created on Nov 21, 2012

@author: Ted Carancho
'''

import pyqtgraph.examples
pyqtgraph.examples.run()
'''
from pyqtgraph.Qt import QtGui, QtCore
from collections import deque
import numpy as np
import pyqtgraph as pg

app = QtGui.QApplication([])

win = pg.GraphicsWindow(title="Plot Data")
win.resize(800,600)
dataPlot = win.addPlot(title="Sensor Data")
dataPlot.hideAxis('bottom')
dataPlot.showGrid(y=True)

plotSize = 256
plotCount = 6

output = []
for i in range(plotCount):
    output.append(deque([0.0]*plotSize))

axis = deque(range(plotSize))
value = plotSize

def update():
    global value
    value += 1
    axis.popleft()
    axis.append(value)
    
    dataPlot.clear()
    for i in range(plotCount):
        output[i].popleft()
        output[i].append(np.random.normal() + (i*3))
        dataPlot.plot(x=list(axis), y=list(output[i]), pen=(i,plotCount))


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

app.exec_()
'''