
import time
import threading
import Queue

from PyQt4 import QtCore
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
    
    def __init__(self, communicator, event_dispatcher):
        self._communicator = communicator
        self._is_subscribed = False
        self._event_dispatcher = event_dispatcher
        
        self._date_output_queue = Queue.Queue()
        self._timer = QtCore.QTimer()

    def send_command(self, command):
        if self._is_subscribed:
            raise AlreadySubscribedException("already subscribed. stop subscriptions before sending another command")
        self._communicator.write(bytes(command.encode('utf-8')))
        self._communicator.flush() 

    def receive_command_data(self):
        data = self._communicator.read_line().rstrip('\r\n')
        return data

    def flush_command_data(self):
        data = self._communicator.read(self._communicator.data_available())
        return len(data)

    def subscribe_command(self, command, callback):
        self.send_command(command)
        self.start_subscription_thread()
        self.start_context_switch_timer(callback)

    def unsubscribe_command(self, command = None):
        self.stop_subscription_thread()
        self.send_command(command or self.BASE_COMMANDS['UnsubscribeAll'])
        self.flush_command_data()

    def start_subscription_thread(self):
        self._is_subscribed = True
        self.reading_thread = threading.Thread(target=self.reading_thread_function, args=[])
        self.reading_thread.setDaemon(True)
        self.reading_thread.start()

    def join_subscription_thread(self):
        if self._is_subscribed:
            self.reading_thread.join()
        
    def stop_subscription_thread(self):
        self._is_subscribed = False
        self.join_subscription_thread()
        self._timer.stop()
        
    def start_context_switch_timer(self, callback):
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(callback)
        self._timer.start(50)


    def reading_thread_function(self):
        while(self._is_subscribed):
#            callback(self.receive_command_data())
            self._date_output_queue.put(self.receive_command_data())
            time.sleep(0.002)  

    def get_flight_software_version(self):
        self.send_command(self.BASE_COMMANDS['GetSoftwareVersion'])
        return self.receive_command_data()

    @abstractmethod
    def request_board_configuration(self):
        pass
        
            

