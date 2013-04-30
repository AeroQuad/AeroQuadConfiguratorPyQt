'''
Created on Apr 21, 2013

@author: David Lobato <dav.lobato [at] gmail.com>
'''

import sys
import time
import threading

from abc import abstractmethod
from abc import ABCMeta

class AlreadySubscribedException(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return "AlreadySubscribedException: %s" % self.msg

class ProtocolHandler(object):
    
    __metaclass__ = ABCMeta

    BASE_COMMANDS = { 'GetSoftwareVersion'    : '!',
                      'UnsubscribeAll'        : 'X', }
    
    def __init__(self, communicator, vehicle_model):
        self._communicator = communicator
        self._is_subscribed = False
        self._vehicle_model = vehicle_model

    def send_command(self, command):
        if self._is_subscribed:
            raise AlreadySubscribedException("already subscribed. stop subscriptions before sending another command")
        self._communicator.write(bytes(command.encode('utf-8')))
        self._communicator.flush() 

    def receive_command_data(self):
        data = self._communicator.read_line().rstrip('\r\n')
        print(data)
        return data

    def flush_command_data(self):
        data = self._communicator.read(self._communicator.data_available())
        return len(data)

    def subscribe_command(self, command, callback):
        self.send_command(command)
        self.start_subscription_thread(callback)

    def unsubscribe_command(self, command = None):
        self.stop_subscription_thread()
        self.send_command(command or self.BASE_COMMANDS['UnsubscribeAll'])
        self.flush_command_data()

    def start_subscription_thread(self, callback):
        self._is_subscribed = True
        self.subscription_thread_object = threading.Thread(target=self.subscription_thread, args=(callback,))
        self.subscription_thread_object.start()

    def join_subscription_thread(self):
        if self._is_subscribed:
            self.subscription_thread_object.join()
        
    def stop_subscription_thread(self):
        self._is_subscribed = False
        self.join_subscription_thread()

    def subscription_thread(self, callback):
        while(self._is_subscribed):
            data = self.receive_command_data()
            if callback(data):  
                break

    def get_flight_software_version(self):
        self.send_command(self.BASE_COMMANDS['GetSoftwareVersion'])
        return self.receive_command_data()

    @abstractmethod
    def request_board_configuration(self):
        pass
        
            

