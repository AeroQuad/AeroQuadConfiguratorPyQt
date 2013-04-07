#'''
#Created on Mar 27, 2013
#
#@author: Ted Carancho
#'''
#
#from PyQt4 import QtCore, QtGui
#from subpanel.subPanel import SubPanel
#from subpanel.dynamicConfig.dynamicConfigWindow import Ui_DynamicConfig
#
#class DynamicConfig(QtGui.QWidget, SubPanel):
#    '''Tutorial example for creating your first subpanel. 
#    This example will retrieve the AeroQuad flight software 
#    version number and write it into a label when a push button is pressed.
#    '''
#    
#    def __init__(self):
#        '''
#        This initializes the tutorial subpanel
#        '''
#        QtGui.QWidget.__init__(self)
#        SubPanel.__init__(self)
#        self.ui = Ui_DynamicConfig()
#        self.ui.setupUi(self)
#        self.ui.pushButton.clicked.connect(self.sendMiniConfig)
#        
#        palette = QtGui.QPalette()
#        palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.white)
#        self.ui.receiverTitle.setPalette(palette)
#        self.ui.motorTitle.setPalette(palette)
#        
#         
#    def sendMiniConfig(self):
#        pass
#=======
'''
Created on Mar 27, 2013

@author: Ted Carancho
'''

from PyQt4 import QtCore, QtGui
from subpanel.subPanel import SubPanel
from subpanel.dynamicConfig.dynamicConfigWindow import Ui_DynamicConfig

class DynamicConfig(QtGui.QWidget, SubPanel):
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
        self.ui = Ui_DynamicConfig()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.sendMiniConfig)
        
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.white)
        self.ui.receiverTitle.setPalette(palette)
        self.ui.motorTitle.setPalette(palette)
        
         
    def sendMiniConfig(self):
        pass
