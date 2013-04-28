'''
Created on Apr 27, 2013

@author: Kenny
'''

class AQV4MessageSender(object):


    def __init__(self,communicator):
        self._communicator = communicator
        
    def send_request(self, request):
#        self._communicator.write('X')
        self._communicator.write(request)
        print("send request = " + request)
        
    def send_mini_config(self, selected_flight_config, selected_receiver_config, selected_reversed_yaw_rotation):
        command = "Q "
        command += selected_flight_config
        command += ";"
        command += selected_receiver_config
        command += ";"
        command += selected_reversed_yaw_rotation
        command += ";"
        command += "5"
        self._communicator.write(command)

    
        