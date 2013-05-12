
from PyQt4 import QtCore, QtGui
from ui.subpanel.BasePanelController import BasePanelController
from model.EventDispatcher import EventDispatcher
from model.FlightConfigType import FlightConfigType
from model.ReceiverConfigType import ReceiverConfigType
from ui.subpanel.vehicledynamicconfig.VehicleDynamicConfigPanel import Ui_VehicleDynamicConfigPanel

class VehicleDynamicConfigController(QtGui.QWidget, BasePanelController):
    
    def __init__(self, event_dispatcher, protocol_handler):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        self.ui = Ui_VehicleDynamicConfigPanel()
        self.ui.setupUi(self)
        self.ui.updateButton.clicked.connect(self._send_mini_config)
        
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.white)
        self.ui.receiverTitle.setPalette(palette)
        self.ui.motorTitle.setPalette(palette)
        
        self.ui.triBox.clicked.connect(self.triCheckBoxPressed)
        self.ui.quadBox.clicked.connect(self.quadCheckBoxPressed)
        self.ui.quadPlusBox.clicked.connect(self.quadPlusCheckBoxPressed)
        self.ui.quadY4Box.clicked.connect(self.y4CheckBoxPressed)
        self.ui.y6Box.clicked.connect(self.y6CheckBoxPressed)
        self.ui.hexaPlusBox.clicked.connect(self.hexPlusCheckBoxPressed)
        self.ui.hexaXBox.clicked.connect(self.hexXCheckBoxPressed)
        self.ui.reverseRotation.clicked.connect(self.reverseRotationCheckBoxPressed)
        
        self.ui.ppmRecv.clicked.connect(self.ppmReceiverCheckBoxPressed)
        self.ui.normalRecv.clicked.connect(self.normalReceiverCheckBoxPressed)
        
        
        self._flight_config_type = FlightConfigType.QUAD_X
        self._receiver_type = ReceiverConfigType.RECEIVER_PWM
        self._reversed_yaw = '1'

        self._selected_flight_config = FlightConfigType.QUAD_X
        self._selected_receiver_config = ReceiverConfigType.RECEIVER_PWM
        self._selected_reversed_yaw_rotation = '1'
        self._update_panel_component()
        
        event_dispatcher.register(self._flight_config_updated, EventDispatcher.FLIGHT_CONFIG_EVENT)
        event_dispatcher.register(self._yaw_direction_updated, EventDispatcher.YAW_DIRECTION_CONFIG_EVENT)
        event_dispatcher.register(self._receiver_type_updated, EventDispatcher.RECEIVER_TYPE_EVENT)
        
        
    def _flight_config_updated(self, sender, event, msg = None):
        self._flight_config_type = msg
        
        if (self._flight_config_type == '0') :
            self.ui.quadBox.setChecked(True)
        elif (self._flight_config_type == '1') :
            self.ui.quadPlusBox.setChecked(True)
        elif (self._flight_config_type == '2') :
            self.ui.hexaPlusBox.setChecked(True)
        elif (self._flight_config_type == '3') :
            self.ui.hexaXBox.setChecked(True)
        elif (self._flight_config_type == '4') :
            self.ui.triBox.setChecked(True)
        elif (self._flight_config_type == '5') :
            self.ui.quadY4Box.setChecked(True)
        elif (self._flight_config_type == '6') :
            self.ui.y6Box.setChecked(True)
            
        self._update_panel_component()
                
    def _yaw_direction_updated(self, sender, event, msg = None):
        self._reversed_yaw = msg
        
        if (self._reversed_yaw == '-1') :
            self.ui.reverseRotation.setChecked(True)
        else :
            self.ui.reverseRotation.setChecked(False)
            
        self._update_panel_component()

    def _receiver_type_updated(self, sender, event, msg = None):

        self._receiver_type = msg
                
        if (self._receiver_type == '0') :
            self.ui.ppmRecv.setChecked(True)
        elif (self._receiver_type == '1') :
            self.ui.normalRecv.setChecked(True)
            
        self._update_panel_component()          
        print("receiver type updated!")  
            
    def start(self):
        pass

    def triCheckBoxPressed(self):
        self._selected_flight_config = FlightConfigType.TRI
        self._update_panel_component()

    def quadCheckBoxPressed(self):
        self._selected_flight_config = FlightConfigType.QUAD_X
        self._update_panel_component()
        
    def quadPlusCheckBoxPressed(self):
        self._selected_flight_config = FlightConfigType.QUAD_PLUS
        self._update_panel_component()
        
    def y4CheckBoxPressed(self):
        self._selected_flight_config = FlightConfigType.QUAD_Y4
        self._update_panel_component()

    def y6CheckBoxPressed(self):
        self._selected_flight_config = FlightConfigType.HEX_Y6
        self._update_panel_component()

    def hexPlusCheckBoxPressed(self):
        self._selected_flight_config = FlightConfigType.HEX_PLUS
        self._update_panel_component()

    def hexXCheckBoxPressed(self):
        self._selected_flight_config = FlightConfigType.HEX_X
        self._update_panel_component()
        
    def reverseRotationCheckBoxPressed(self):
        if (self.ui.reverseRotation.isChecked()) :
            self._selected_reversed_yaw_rotation = '-1'
        else :
            self._selected_reversed_yaw_rotation = '1'
        self._update_panel_component()

    def ppmReceiverCheckBoxPressed(self):
        self._selected_receiver_config = ReceiverConfigType.RECEIVER_PPM
        self._update_panel_component()
        
    def normalReceiverCheckBoxPressed(self):
        self._selected_receiver_config = ReceiverConfigType.RECEIVER_PWM
        self._update_panel_component()

    def _update_panel_component(self):
        
        if (self._selected_reversed_yaw_rotation != self._reversed_yaw) :
            self.ui.updateButton.setEnabled(True)
            return
        
        if (self._selected_receiver_config != self._receiver_type) :
            self.ui.updateButton.setEnabled(True)
            return
        
        if (self._selected_flight_config != self._flight_config_type) :
            self.ui.updateButton.setEnabled(True)
            return
        
        self.ui.updateButton.setEnabled(False)
        
    def _send_mini_config(self):
        self._message_sender.send_mini_config(self._selected_flight_config,
                                              self._selected_receiver_config,
                                              self._selected_reversed_yaw_rotation)

        self._message_sender.send_request('#')













