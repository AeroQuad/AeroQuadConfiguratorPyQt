'''
Created on Dec 27, 2012

@author: Ted Carancho
'''

class BarGauge(object):
    '''
    classdocs
    '''


    def __init__(cls, channelName, ui):
        '''
        Constructor
        '''
        cls.ui = ui
        cls.channelName = channelName
        # Setup plots to display rest of transmitter channels
        transmitterScene = QtGui.QGraphicsScene()
        cls.channelCount = 4
        cls.labelWidth = 20

        cls.barGauge = QtGui.QGraphicsRectItem()
        cls.barGauge.setBrush(QtGui.QBrush(QtCore.Qt.blue, QtCore.Qt.SolidPattern))
        xmitLabel = transmitterScene.addText(cls.xmitLabels[channel])
        xmitLabel.setPos(cls.xmitChannelLocation(channel), cls.ui.transmitterOutput.height())
        print(cls.xmitChannelLocation(channel), cls.ui.transmitterOutput.height())