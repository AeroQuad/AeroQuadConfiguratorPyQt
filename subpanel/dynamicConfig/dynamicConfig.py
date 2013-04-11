'''
Created on Mar 27, 2013

@author: Ted Carancho
'''

import logging
from PyQt4 import QtCore, QtGui
from subpanel.subPanel import SubPanel
from subpanel.dynamicConfig.dynamicConfigWindow import Ui_DynamicConfig
from model.VehicleModel import VehicleModel
from model.FlightConfigType import FlightConfigType

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
        self.ui.updateAQButton.clicked.connect(self.sendMiniConfig)
        
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
        self.ui.reverseRotation.clicked.connect(self.reverseRotationCheckBoxPressed)
        
        self.selectedVehicleConfig = FlightConfigType.quadXConfig
        self.selectedInvertedYawRotation = False
        self.updatePanelComponent()
            
    def start(self, xmlSubPanel, boardConfiguration):
        self.boardConfiguration = boardConfiguration
        
        try:
            VehicleModel.getInstance()._flightConfigType = self.boardConfiguration["Flight Config"]
        except:
            logging.error("Can't read vehicle config, probably not connected to current Aeroquad")
        
        if VehicleModel.getInstance()._flightConfigType == '0' :
            self.ui.quadBox.setChecked(True)
        elif VehicleModel.getInstance()._flightConfigType == '1' :
            self.ui.quadPlusBox.setChecked(True)
        elif VehicleModel.getInstance()._flightConfigType == '2' :
            self.ui.hexaPlusBox.setChecked(True)
        elif VehicleModel.getInstance()._flightConfigType == '3' :
            self.ui.hexaXBox.setChecked(True)
        elif VehicleModel.getInstance()._flightConfigType == '4' :
            self.ui.triBox.setChecked(True)
        elif VehicleModel.getInstance()._flightConfigType == '5' :
            self.ui.quadY4Box.setChecked(True)
        elif VehicleModel.getInstance()._flightConfigType == '6' :
            self.ui.Y6Box.setChecked(True)

        print (self.boardConfiguration["Yaw Config"])
        print (self.boardConfiguration["Receiver Type"])

    def sendMiniConfig(self):
        print("Send")

    def triCheckBoxPressed(self):
        self.selectedVehicleConfig = FlightConfigType.triConfig
        self.updatePanelComponent()

    def quadCheckBoxPressed(self):
        self.selectedVehicleConfig = FlightConfigType.quadXConfig
        self.updatePanelComponent()
        
    def quadPlusCheckBoxPressed(self):
        self.selectedVehicleConfig = FlightConfigType.quadPlusConfig
        self.updatePanelComponent()
        
    def y4CheckBoxPressed(self):
        self.selectedVehicleConfig = FlightConfigType.quadY4Config
        self.updatePanelComponent()

    def y6CheckBoxPressed(self):
        self.selectedVehicleConfig = FlightConfigType.hexY6Config
        self.updatePanelComponent()

    def hexPlusCheckBoxPressed(self):
        self.selectedVehicleConfig = FlightConfigType.hexPlusConfig
        self.updatePanelComponent()

    def hexXCheckBoxPressed(self):
        self.selectedVehicleConfig = FlightConfigType.hexXConfig
        self.updatePanelComponent()
        
    def reverseRotationCheckBoxPressed(self):
        self.selectedInvertedYawRotation = self.ui.reverseRotation.isChecked()
        self.updatePanelComponent()

    def updatePanelComponent(self):
        self.ui.updateAQButton.setEnabled(False)
        print("update panel compement")

    

















