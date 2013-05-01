'''
Created on Apr 10, 2013

@author: Kenny
'''
from model.FlightConfigType import FlightConfigType
from model.ReceiverConfigType import ReceiverConfigType
from utilities.observers.Observable import Observable
from model.Vector3D import Vector3D


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
    
    MAGNETOMETER_RAW_DATA_EVENT = "MAGNETOMETER_RAW_DATA_EVENT"
    
    def __init__(self):
        Observable.__init__(self)
        
    def update_property_from_the_board(self, property_name, value):
        self.dispatch(property_name, value)
        
        