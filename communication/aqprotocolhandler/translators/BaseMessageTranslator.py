'''
Created on Apr 28, 2013

@author: Kenny
'''

class BaseMessageTranslator(object):


    def __init__(self, vehicle_model):
        self._vehicle_model = vehicle_model
        
    def translate(self, message):
        #override this methos
        pass