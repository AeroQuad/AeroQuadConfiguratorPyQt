'''
Created on Feb 15, 2013

@author: Ted Carancho
'''

from PyQt4 import QtCore, QtGui
from subpanel.subPanel import SubPanel
from subpanel.tutorial.tutorialWindow import Ui_tutorial

class tutorial(QtGui.QWidget, SubPanel):
    '''Tutorial example for creating your first subpanel. 
    This example will retrieve the AeroQuad flight software 
    version number and write it into a label when a push button is pressed.
    '''
    
    def __init__(self):
        '''
        This initializes the tutorial subpanel
        '''
        QtGui.QWidget.__init__(self)
        SubPanel.__init__(self)
        self.ui = Ui_tutorial()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.getSoftwareVersion)
        
    def getSoftwareVersion(self):
        if (self.comm.isConnected()):
            self.comm.write("!")
            self.ui.label.setText(self.comm.read())
            