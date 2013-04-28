'''
Created on Apr 10, 2013

@author: Kenny
'''
from model.FlightConfigType import FlightConfigType
from model.ReceiverConfigType import ReceiverConfigType
from utilities.observers.Observable import Observable


#
# Not a fan of singleton pattern, but, that will fit my need for now
# 
class VehicleModel(Observable):
    
    CONNECTION_STATE_CHANGED_EVENT = "CONNECTION_STATE_CHANGED_EVENT"
    
    SOFTWARE_VERSION_EVENT = "Software Version"
    BOAR_TYPE_EVENT = "Board Type"
    FLIGHT_CONFIG_EVENT = "Flight Config"
    YAW_DIRECTION_CONFIG_EVENT = "Yaw Config"
    RECEIVER_TYPE_EVENT = "Receiver Type"
    RECEIVER_NB_CHANNEL_EVENT = "Receiver Nb Channels"
    RECEIVER_CHANNELS_MAPS_EVENT = "Receiver Channels map"
    NUMBER_MOTORS_EVENT = "Motors"
    GYROSCOPE_DETECTED_EVENT = "Gyroscope"
    ACCELEROMETER_DETECTED_EVENT = "Accelerometer"
    BAROMETER_DETECTED_EVENT = "Barometer"
    MAGNETOMETER_DETECTED_EVENT = "Magnetometer"
    HEADING_HOLD_ENABLED_EVENT = "Heading Hold"
    ALTITUDE_HOLD_ENABLED_EVENT = "Altitude Hold"
    BATTERY_MONITOR_ENABLED_EVENT = "Battery Monitor"
    
    def __init__(self):
        Observable.__init__(self)
        
        self._is_connected = False
        self._flight_config_type = FlightConfigType.QUAD_X
        self._receiver_type = ReceiverConfigType.RECEIVER_PWM
        self._reversed_yaw = '1'
        
        self._board_onfiguration_properties = {}
        

    def get_reversed_yaw(self):
        return self._reversed_yaw

    def get_receiver_type(self):
        return self._receiver_type
    
    def get_flight_config_type(self):
        return self._flight_config_type
        
    def set_boad_configuration_property(self, key, value):
        self._board_onfiguration_properties[key] = value;
        self.dispatch( key, value)
        
    def set_is_connected(self, is_connected):
        self._is_connected = is_connected
        self.dispatch( VehicleModel.CONNECTION_STATE_CHANGED_EVENT, self._is_connected)
        
        