'''
Created on Apr 10, 2013

@author: Kenny
'''
from model.FlightConfigType import FlightConfigType
from model.ReceiverConfigType import ReceiverConfigType


#
# Not a fan of singleton pattern, but, that will fit my need for now
# 
class VehicleModel():
    INSTANCE = None
    
    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
         
        self._flight_config_type = FlightConfigType.QUAD_X
        self._receiver_type = ReceiverConfigType.RECEIVER_PWM
        self._reversed_yaw = '1'
     
    @classmethod     
    def getInstance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = VehicleModel()
        return cls.INSTANCE