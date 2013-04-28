'''
Created on Apr 28, 2013

@author: Kenny
'''
from communication.aqprotocolhandler.translators.BaseMessageTranslator import BaseMessageTranslator
import logging

class LoggingTraslator(BaseMessageTranslator):


    def __init__(self,vehicle_model):
        BaseMessageTranslator.__init__(self,vehicle_model)
        
    def translate(self, message):
        print(message)
        logging.error("Unprocessed message = " + message)
        