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
        self.barGaugeGap = 5 # Add a little line at the bottom to show a zero value, and space at the top to separate text
        self.labelHeight = 15
        self.labelWidth = 0.0

        gradient = QtGui.QLinearGradient(0, 100, 100, 0)
        gradient.setColorAt(0.0, QtCore.Qt.black);
        gradient.setColorAt(0.8, QtCore.Qt.gray);
        gradient.setColorAt(1.0, QtCore.Qt.white);
        self.setBrush(gradient)

        self.setValue(1000)
        
        # Setup gauge label
        self.labelItem = QtGui.QGraphicsTextItem(name)
        self.labelItem.setParentItem(self)
        self.labelItem.setDefaultTextColor(QtCore.Qt.white)
        # Center label
        self.labelWidth = self.labelItem.boundingRect().width()
        self.labelItem.setPos((self.barGaugeWidth-self.labelWidth)/2.0, 0)


    def setHeight(self, height):
        self.barGaugeHeight = height
    
    def setWidth(self, width):
        self.barGaugeWidth = width
        self.labelItem.setPos((self.barGaugeWidth-self.labelWidth)/2.0, 0)
        
    def setValue(self, value):
        if value > self.max:
            value = self.max
        if value < self.min:
            value = self.min
            
        if value > 1850:
            self.brush().gradient().setColorAt(0.0, QtCore.Qt.red)
        elif value > 1600:
            self.brush().gradient().setColorAt(0.0, QtCore.Qt.yellow)
        else:
            self.brush().gradient().setColorAt(0.0, QtCore.Qt.black)

        self.output = self.scale(value, (self.min, self.max), (self.barGaugeGap, self.barGaugeHeight-self.barGaugeGap))
        self.updateRect()
    
    def setValueMinMax(self, min, max):
        self.min, self.max = min, max
        self.updateRect()
    
    def updateRect(self):
        self.setRect(self.location, (self.barGaugeHeight-self.output)+self.labelHeight, self.barGaugeWidth, self.output)
    
    @staticmethod
    def scale(val, src, dst):
        '''Scale the given value from the scale of src to the scale of dst.'''
        return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]
