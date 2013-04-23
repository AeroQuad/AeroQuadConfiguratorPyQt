'''
Created on Mar 27, 2013

@author: Ted Carancho
'''

import logging
from PyQt4 import QtCore, QtGui
from ui.subpanel.BasePanelController import BasePanelController
from model.VehicleModel import VehicleModel
from model.FlightConfigType import FlightConfigType
from model.ReceiverConfigType import ReceiverConfigType
from ui.subpanel.vehicledynamicconfig.VehicleDynamicConfigPanel import VehicleDynamicConfigPanel

class VehicleDynamicConfigController(QtGui.QWidget, BasePanelController):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        self.ui = VehicleDynamicConfigPanel()
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
        
        self._selectedVehicleConfig = FlightConfigType.QUAD_X
        self._selectedReceiverConfig = ReceiverConfigType.RECEIVER_PWM
        self._selectedInvertedYawRotation = '1'
        self.updatePanelComponent()
            
    def start(self, xmlSubPanel, boardConfiguration):
        self.boardConfiguration = boardConfiguration
        
        try:
            VehicleModel.getInstance()._flight_config_type = self.boardConfiguration["Flight Config"]
            VehicleModel.getInstance()._receiver_type = self.boardConfiguration["Receiver Type"]
            VehicleModel.getInstance()._reversed_yaw = self.boardConfiguration["Yaw Config"]
        except:
            logging.error("Can't read vehicle config, probably not connected to current Aeroquad")
        
        
        if (VehicleModel.getInstance()._flight_config_type == '0') :
            self.ui._quadBox.setChecked(True)
        elif (VehicleModel.getInstance()._flight_config_type == '1') :
            self.ui._quadPlusBox.setChecked(True)
        elif (VehicleModel.getInstance()._flight_config_type == '2') :
            self.ui._hexaPlusBox.setChecked(True)
        elif (VehicleModel.getInstance()._flight_config_type == '3') :
            self.ui._hexaXBox.setChecked(True)
        elif (VehicleModel.getInstance()._flight_config_type == '4') :
            self.ui._triBox.setChecked(True)
        elif (VehicleModel.getInstance()._flight_config_type == '5') :
            self.ui._quadY4Box.setChecked(True)
        elif (VehicleModel.getInstance()._flight_config_type == '6') :
            self.ui._Y6Box.setChecked(True)
            
        if (VehicleModel.getInstance()._reversed_yaw == '-1') :
            self.ui._reverseRotation.setChecked(True)

        if (VehicleModel.getInstance()._receiver_type == '0') :
            self.ui._ppmRecv.setChecked(True)
        elif (VehicleModel.getInstance()._receiver_type == '1') :
            self.ui._normalRecv.setChecked(True)
            
        self._selectedInvertedYawRotation = VehicleModel.getInstance()._reversed_yaw
        self._selectedReceiverConfig = VehicleModel.getInstance()._receiver_type
        self._selectedVehicleConfig = VehicleModel.getInstance()._flight_config_type
            
    def triCheckBoxPressed(self):
        self._selectedVehicleConfig = FlightConfigType.TRI
        self.updatePanelComponent()

    def quadCheckBoxPressed(self):
        self._selectedVehicleConfig = FlightConfigType.QUAD_X
        self.updatePanelComponent()
        
    def quadPlusCheckBoxPressed(self):
        self._selectedVehicleConfig = FlightConfigType.QUAD_PLUS
        self.updatePanelComponent()
        
    def y4CheckBoxPressed(self):
        self._selectedVehicleConfig = FlightConfigType.QUAD_Y4
        self.updatePanelComponent()

    def y6CheckBoxPressed(self):
        self._selectedVehicleConfig = FlightConfigType.HEX_Y6
        self.updatePanelComponent()

    def hexPlusCheckBoxPressed(self):
        self._selectedVehicleConfig = FlightConfigType.HEX_PLUS
        self.updatePanelComponent()

    def hexXCheckBoxPressed(self):
        self._selectedVehicleConfig = FlightConfigType.HEX_X
        self.updatePanelComponent()
        
    def reverseRotationCheckBoxPressed(self):
        if (self.ui._reverseRotation.isChecked()) :
            self._selectedInvertedYawRotation = '-1'
        else :
            self._selectedInvertedYawRotation = '1'
        self.updatePanelComponent()

    def ppmReceiverCheckBoxPressed(self):
        self._selectedReceiverConfig = ReceiverConfigType.RECEIBER_PPM
        self.updatePanelComponent()
        
    def normalReceiverCheckBoxPressed(self):
        self._selectedReceiverConfig = ReceiverConfigType.RECEIVER_PWM
        self.updatePanelComponent()

    def updatePanelComponent(self):
        
        if (self._selectedInvertedYawRotation != VehicleModel.getInstance()._reversed_yaw) :
            self.ui._updateAQButton.setEnabled(True)
            return
        
        if (self._selectedReceiverConfig != VehicleModel.getInstance()._receiver_type) :
            self.ui._updateAQButton.setEnabled(True)
            return
        
        if (self._selectedVehicleConfig != VehicleModel.getInstance()._flight_config_type) :
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
        VehicleModel.getInstance()._reversed_yaw = self._selectedInvertedYawRotation 
        VehicleModel.getInstance()._receiver_type = self._selectedReceiverConfig
        VehicleModel.getInstance()._flight_config_type = self._selectedVehicleConfig

        self.updatePanelComponent()













