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
         
        self._flightConfigType = FlightConfigType.quadXConfig
        self._receiverType = ReceiverConfigType.receiver_PWM
     
    @classmethod     
    def getInstance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = VehicleModel()
        return cls.INSTANCE