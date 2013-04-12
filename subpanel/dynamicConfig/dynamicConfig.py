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
from model.ReceiverConfigType import ReceiverConfigType

class DynamicConfig(QtGui.QWidget, SubPanel):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        SubPanel.__init__(self)
        self.ui = Ui_DynamicConfig()
        self.ui.setupUi(self)
        self.ui._updateAQButton.clicked.connect(self.sendMiniConfig)
        
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.white)
        self.ui.receiverTitle.setPalette(palette)
        self.ui.motorTitle.setPalette(palette)
        
        self.ui._triBox.clicked.connect(self.triCheckBoxPressed)
        self.ui._quadBox.clicked.connect(self.quadCheckBoxPressed)
        self.ui._quadPlusBox.clicked.connect(self.quadPlusCheckBoxPressed)
        self.ui._quadY4Box.clicked.connect(self.y4CheckBoxPressed)
        self.ui._y6Box.clicked.connect(self.y6CheckBoxPressed)
        self.ui._hexaPlusBox.clicked.connect(self.hexPlusCheckBoxPressed)
        self.ui._hexaXBox.clicked.connect(self.hexXCheckBoxPressed)
        self.ui._reverseRotation.clicked.connect(self.reverseRotationCheckBoxPressed)
        
        self.ui._ppmRecv.clicked.connect(self.ppmReceiverCheckBoxPressed)
        self.ui._normalRecv.clicked.connect(self.normalReceiverCheckBoxPressed)
        
        self._selectedVehicleConfig = FlightConfigType.quadXConfig
        self._selectedReceiverConfig = ReceiverConfigType.receiver_PWM
        self._selectedInvertedYawRotation = '1'
        self.updatePanelComponent()
            
    def start(self, xmlSubPanel, boardConfiguration):
        self.boardConfiguration = boardConfiguration
        
        try:
            VehicleModel.getInstance()._flightConfigType = self.boardConfiguration["Flight Config"]
            VehicleModel.getInstance()._receiverType = self.boardConfiguration["Receiver Type"]
            VehicleModel.getInstance()._reversedYaw = self.boardConfiguration["Yaw Config"]
        except:
            logging.error("Can't read vehicle config, probably not connected to current Aeroquad")
        
        
        if (VehicleModel.getInstance()._flightConfigType == '0') :
            self.ui._quadBox.setChecked(True)
        elif (VehicleModel.getInstance()._flightConfigType == '1') :
            self.ui._quadPlusBox.setChecked(True)
        elif (VehicleModel.getInstance()._flightConfigType == '2') :
            self.ui._hexaPlusBox.setChecked(True)
        elif (VehicleModel.getInstance()._flightConfigType == '3') :
            self.ui._hexaXBox.setChecked(True)
        elif (VehicleModel.getInstance()._flightConfigType == '4') :
            self.ui._triBox.setChecked(True)
        elif (VehicleModel.getInstance()._flightConfigType == '5') :
            self.ui._quadY4Box.setChecked(True)
        elif (VehicleModel.getInstance()._flightConfigType == '6') :
            self.ui._Y6Box.setChecked(True)
            
        if (VehicleModel.getInstance()._reversedYaw == '-1') :
            self.ui._reverseRotation.setChecked(True)

        if (VehicleModel.getInstance()._receiverType == '0') :
            self.ui._ppmRecv.setChecked(True)
        elif (VehicleModel.getInstance()._receiverType == '1') :
            self.ui._normalRecv.setChecked(True)
            
        self._selectedInvertedYawRotation = VehicleModel.getInstance()._reversedYaw
        self._selectedReceiverConfig = VehicleModel.getInstance()._receiverType
        self._selectedVehicleConfig = VehicleModel.getInstance()._flightConfigType
            
    def triCheckBoxPressed(self):
        self._selectedVehicleConfig = FlightConfigType.triConfig
        self.updatePanelComponent()

    def quadCheckBoxPressed(self):
        self._selectedVehicleConfig = FlightConfigType.quadXConfig
        self.updatePanelComponent()
        
    def quadPlusCheckBoxPressed(self):
        self._selectedVehicleConfig = FlightConfigType.quadPlusConfig
        self.updatePanelComponent()
        
    def y4CheckBoxPressed(self):
        self._selectedVehicleConfig = FlightConfigType.quadY4Config
        self.updatePanelComponent()

    def y6CheckBoxPressed(self):
        self._selectedVehicleConfig = FlightConfigType.hexY6Config
        self.updatePanelComponent()

    def hexPlusCheckBoxPressed(self):
        self._selectedVehicleConfig = FlightConfigType.hexPlusConfig
        self.updatePanelComponent()

    def hexXCheckBoxPressed(self):
        self._selectedVehicleConfig = FlightConfigType.hexXConfig
        self.updatePanelComponent()
        
    def reverseRotationCheckBoxPressed(self):
        if (self.ui._reverseRotation.isChecked()) :
            self._selectedInvertedYawRotation = '-1'
        else :
            self._selectedInvertedYawRotation = '1'
        self.updatePanelComponent()

    def ppmReceiverCheckBoxPressed(self):
        self._selectedReceiverConfig = ReceiverConfigType.receiver_PPM
        self.updatePanelComponent()
        
    def normalReceiverCheckBoxPressed(self):
        self._selectedReceiverConfig = ReceiverConfigType.receiver_PWM
        self.updatePanelComponent()

    def updatePanelComponent(self):
        
        if (self._selectedInvertedYawRotation != VehicleModel.getInstance()._reversedYaw) :
            self.ui._updateAQButton.setEnabled(True)
            return
        
        if (self._selectedReceiverConfig != VehicleModel.getInstance()._receiverType) :
            self.ui._updateAQButton.setEnabled(True)
            return
        
        if (self._selectedVehicleConfig != VehicleModel.getInstance()._flightConfigType) :
            self.ui._updateAQButton.setEnabled(True)
            return
        
        self.ui._updateAQButton.setEnabled(False)
        
    def sendMiniConfig(self):
        command = "Q "
        command += self._selectedVehicleConfig
        command += ";"
        command += self._selectedReceiverConfig
        command += ";"
        command += self._selectedInvertedYawRotation
        command += ";"
        command += "5"
        self.comm.write(command)
        
        # In fact here, we should request back the vehicle config to make sure the 
        # vehicle have been updated with the selection from the user
        VehicleModel.getInstance()._reversedYaw = self._selectedInvertedYawRotation 
        VehicleModel.getInstance()._receiverType = self._selectedReceiverConfig
        VehicleModel.getInstance()._flightConfigType = self._selectedVehicleConfig

        self.updatePanelComponent()













