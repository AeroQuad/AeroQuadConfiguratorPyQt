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
    
    INSTANCE = None    # instance have to be remove later on, when messaging will work
    
    CONNECTION_STATE_CHANGED_EVENT = "CONNECTION_STATE_CHANGED_EVENT"
    
    def __init__(self):
        Observable.__init__(self)
        
        
        
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
         
        self._flight_config_type = FlightConfigType.QUAD_X
        self._receiver_type = ReceiverConfigType.RECEIVER_PWM
        self._reversed_yaw = '1'
        
        self._board_onfiguration_properties = {}
        
        self.register(self.listener)
        
        
    def listener(self,sender,event,msg=None):
        print("listener " + sender + " " + event + " = " + msg)
        
     
    @classmethod     
    def getInstance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = VehicleModel()
        return cls.INSTANCE
    
    def setBoadConfigurationProperty(self,key,value):
        self._board_onfiguration_properties[key] = value;
        self.dispatch( key, value)
#        print("dispatch " + key + " = " + value)
        
    def set_is_connected(self,is_connected):
        self.is_connected = is_connected
        self.dispatch( VehicleModel.CONNECTION_STATE_CHANGED_EVENT, is_connected)
#        print("dispatch " + VehicleModel.CONNECTION_STATE_CHANGED_EVENT + " = " + str(is_connected))
        
        