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
        
        self.ui.triBox.clicked.connect(self.triCheckBoxPressed)
        self.ui.quadBox.clicked.connect(self.quadCheckBoxPressed)
        self.ui.quadPlusBox.clicked.connect(self.quadPlusCheckBoxPressed)
        self.ui.quadY4Box.clicked.connect(self.y4CheckBoxPressed)
        self.ui.Y6Box.clicked.connect(self.y6CheckBoxPressed)
        self.ui.hexaPlusBox.clicked.connect(self.hexPlusCheckBoxPressed)
        self.ui.hexaXBox.clicked.connect(self.hexXCheckBoxPressed)

    def start(self, xmlSubPanel, boardConfiguration):
        self.boardConfiguration = boardConfiguration
        vehicleConfig = '0'
        try:
            vehicleConfig = self.boardConfiguration["Flight Config"]
        except:
            print("can't read vehicle config")
        
        if vehicleConfig == "0" :
            self.ui.quadBox.setChecked(True)
        elif vehicleConfig == '1' :
            self.ui.quadPlusBox.setChecked(True)
        elif vehicleConfig == '2' :
            self.ui.hexaPlusBox.setChecked(True)
        elif vehicleConfig == '3' :
            self.ui.hexaXBox.setChecked(True)
        elif vehicleConfig == '4' :
            self.ui.triBox.setChecked(True)
        elif vehicleConfig == '5' :
            self.ui.quadY4Box.setChecked(True)
        elif vehicleConfig == '6' :
            self.ui.Y6Box.setChecked(True)

    def sendMiniConfig(self):
        print("send config to mmi not implemented yet")

    def triCheckBoxPressed(self):
        print("tri check box press")

    def quadCheckBoxPressed(self):
        print("quad check box press")
        
    def quadPlusCheckBoxPressed(self):
        print("quad Plus check box press")
        
    def y4CheckBoxPressed(self):
        print("Y4 check box press")

    def y6CheckBoxPressed(self):
        print("y6 check box press")

    def hexPlusCheckBoxPressed(self):
        print("hex plus check box press")

    def hexXCheckBoxPressed(self):
        print("hex X check box press")


















