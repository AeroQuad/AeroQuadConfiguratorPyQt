'''
Created on Apr 28, 2013

@author: Kenny
'''
from communication.aqprotocolhandler.translators.BaseMessageTranslator import BaseMessageTranslator

class AQV4VehicleInfoTranslator(BaseMessageTranslator):


    def __init__(self,vehicle_model):
        BaseMessageTranslator.__init__(self,vehicle_model)
        
    def translate(self, message):
        try :
            configuration = message.split(':')
            self._vehicle_model.set_boad_configuration_property(configuration[0],configuration[1].strip())
        except :
            print("Can't decode message = " + message)
       
        