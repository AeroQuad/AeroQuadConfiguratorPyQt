
import time
import threading
import Queue
#from PyQt4 import QtCore

class AQV4ProtocolHandler(object):


    def __init__(self,communicator,vehicle_event_dispatcher):
        
        self._communicator = communicator
        self._vehicle_event_dispatcher = vehicle_event_dispatcher
        
        self._is_connected = False
        self._is_locked = False
        
        self._reader_thread = threading.Thread(target=self._reading_thread_call_back, args=[])
        self._reader_thread.start()
        self._raw_data = Queue.Queue()
        
#        self._reading_timer = QtCore.QTimer()
#        self._reading_timer.timeout.connect(self._read_continuous_data)
#        self._reading_timer.start(50)

        self._translators = {}
#        self._translators['logging'] = LoggingTraslator(event_dispatcher)
#        self._translators['#'] = AQV4VehicleInfoTranslator(event_dispatcher)
        
        self._current_translator = self._translators['logging'] 

        
        
        
    def _process_new_connection(self):
        self._is_locked = True
        self._is_connected = True
        self._vehicle_model.set_is_connected(True)
        
        self._communicator.write('X')
        self._communicator.flushResponse()
        # Request version number to identify AeroQuad board
        
        self._communicator.write('#')
        self._current_translator = self._translators['#']
#        size = int(self._communicator.waitForRead())
#        for index in range(size):
#            response = self._communicator.waitForRead()
#            self._translators['#'].translate(response)
        
        self._is_locked = False
        
    def _process_deconnection(self):
        self._vehicle_model.set_is_connected(False)
        
    def _reading_thread_call_back(self):

        while(True):
            try:
                if not self._is_locked :
                    if self._communicator.isConnected() :
                        if not self._is_connected :
                            self._process_new_connection()
                        elif self._communicator.dataAvailable():
                            self._raw_data.put(self._communicator.read())
                            if not self._raw_data.empty() :
                                self._current_translator.translate(self._raw_data.get())
                        else:
                            time.sleep(0.100)
                    else :
                        if self._is_connected :
                            self._process_deconnection()
            except IOError as e:
                print(e)
#                logging.error(e)
                
#    def _read_continuous_data(self):
#        if self._communicator.isConnected() and not self._raw_data.empty():           
#            raw_data = self._raw_data.get() # self.data is updated in commThread()
#            print(raw_data)
            
#            # Replace lines below with desired functionality
#            data = rawData.split(",")
#            for i in data:
#                print(i)

                
        
        
        
    
        