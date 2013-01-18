'''
Created on Dec 27, 2012

@author: Ted Carancho
'''

from PyQt4 import QtCore, QtGui

class BarGauge(QtGui.QGraphicsRectItem):
    ''' Generic bar gauge to graphically display numeric values
    '''

    def __init__(self, name ="", parent=None):
        QtGui.QGraphicsRectItem.__init__(self, parent)
        self.min = 1000.0
        self.max = 2000.0
        self.location = 0
        self.barGaugeHeight = 100
        self.barGaugeWidth = 35
        self.label = name
        self.brush = QtGui.QBrush(QtCore.Qt.black, QtCore.Qt.SolidPattern)
        self.barGaugeGap = 5
        self.output = self.barGaugeGap

        #self.setBrush(QtGui.QBrush(QtCore.Qt.blue, QtCore.Qt.SolidPattern))
        #self.setPos(self.location, self.windowHeight - self.labelHeight)
        #self.update(1000)
            
        # Center transmitter output window
        #self.centerOn(0.0, 0.0)
    
    def boundingRect(self):
        return QtCore.QRectF(0.0, 0.0, self.barGaugeHeight, self.barGaugeHeight)
    
    def paint(self, painter, option, widget):
        painter.fillRect(self.location, self.barGaugeHeight-self.output, self.barGaugeWidth, self.output, self.brush)
        painter.setPen(QtCore.Qt.white)
        painter.drawText(self.location, 0, self.label)
        
    def updateSize(self, windowHeight):
        self.windowHeight = windowHeight

        
    def update(self, value):
        self.output = self.scale(value, (self.min, self.max), (self.barGaugeGap, self.barGaugeHeight-self.barGaugeGap))

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
