'''
Created on Dec 27, 2012

@author: Ted Carancho
'''

from PyQt4 import QtCore, QtGui

class BarGauge(QtGui.QGraphicsRectItem):
    ''' Generic bar gauge to graphically display numeric values
    '''

    def __init__(self, parent=None):
        QtGui.QGraphicsRectItem.__init__(self, parent)
        self.min = 1000.0
        self.max = 2000.0
        self.location = 0
        self.labelHeight = 25
        self.windowHeight = 100
        self.barGaugeWidth = 25
        self.label = "Test"
        self.brush = QtGui.QBrush(QtCore.Qt.black, QtCore.Qt.SolidPattern)

        #self.setBrush(QtGui.QBrush(QtCore.Qt.blue, QtCore.Qt.SolidPattern))
        #self.setPos(self.location, self.windowHeight - self.labelHeight)
        #self.update(1000)
            
        # Center transmitter output window
        #self.centerOn(0.0, 0.0)
    
    def boundingRect(self):
        return QtCore.QRectF(0.0, 0.0, 100.0, 100.0)
    
    def paint(self, painter, option, widget):
        #self.paint(painter, option, widget)
        self.localPainter = painter
        painter.fillRect(self.location, 5, self.barGaugeWidth, self.windowHeight, self.brush)
        painter.setPen(QtCore.Qt.white)
        painter.drawText(0, 0, self.label)
        
    def updateSize(self, windowHeight):
        self.windowHeight = windowHeight
        
    def update(self, value):
        output = self.scale(value, (self.min, self.max), (0, self.windowHeight))
        #self.setRect(self.location, self.windowHeight-(output + self.labelHeight), self.barGaugeWidth, output)
        print(output)
        self.localPainter
        #.drawRect(self.location, self.windowHeight-(output + self.labelHeight), self.barGaugeWidth, output)

    def setLocation(self, location):
        self.location = location
    
    def setWidth(self, width):
        self.barGaugeWidth = width
        
    def setMinMax(self, minimum, maximum):
        self.min = minimum
        self.max = maximum
    
    @staticmethod
    def scale(val, src, dst):
        '''Scale the given value from the scale of src to the scale of dst.'''
        return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]
