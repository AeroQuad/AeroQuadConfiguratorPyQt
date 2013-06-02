
import logging
from communication.ProtocolHandler import ProtocolHandler
from model.Vector3D import Vector3D
from model.VehicleEventDispatcher import VehicleEventDispatcher
from communication.v32protocolhandler.V32VehicleStatusTranslator import V32VehicleStatusTranslator
from communication.v32protocolhandler.V32VehicleSensorsDataTranslator import V32VehicleSensorsDataTranslator
from communication.v32protocolhandler.V32ReceiverDataTranslator import V32ReceiverDataTranslator

class AQV32ProtocolHandler(ProtocolHandler):

    COMMANDS = {'GetBoardConfiguration' : '#',
                'GetRatePID'         : 'a', 
                'SetRatePID'         : 'A',
                'GetAttitudePID'     : 'b',
                'SetAttitudePID'     : 'B',
                'GetYawHeadingHoldPID':'c',
                'SetYawHeadingHoldPID':'C',
                'GetAltitudeHoldPID' : 'd',
                'SetAltitudeHoldPID' : 'D',
                'GetMiscConfig': 'e',
                'SetMiscConfig': 'E',
                'GetTransmitterSmoothing' : 'f',
                'SetTransmitterSmoothing' : 'F',
                'GetTransmitterCalibration' : 'g',
                'SetTransmitterCalibration' : 'G',
                'GetTransmitterOffset' : 'h',
                'SetTransmitterOffset' : 'H',                 
                'SubscribeSensor'  : 'i',
                'SubscribeRawMagnetometer' : 'j',
                'GetAccelCalibration' : 'k',
                'SetAccelCalibration' : 'K',
                'SubscribeRawAccel' : 'l',
                'GetMagnetometerCalibration' : 'm',
                'SetMagnetometerCalibration' : 'M',
                'GetBatteryMonitor' : 'n',
                'SetBatteryMonitor' : 'N',
                'GetWaypoints' : 'o',
                'SetWaypoints' : 'O',
                'GetCameraStabilization' : 'p',
                'SetCameraStabilization' : 'P',
                'GetVehicleStateVariables' : 'q',
                'SubscribeVehicleAttitude' : 'r',
                'SubscribeAllFlight' : 's',
                'SubscribeProcessedTransmitter' : 't',
                'GetRangeFinder' : 'u',
                'SetRangeFinder' : 'U',
                'GetGPSPID' : 'v',
                'SetGPSPID' : 'V',
                'GetGPSStatus' : 'y',
                'SubscribeAltitude' : 'z',
                'SubscribeVoltageCurrent' : '$',
                'SubscribeRSSI' : '%',
                'InitializeEEPROM' : 'I',
                'WriteUserValuesEEPROM' : 'W',
                'CalibrateGyro': 'J',
                'GenerateAccelBias' : 'L',
                'CalibrateESCHigh' : '1',
                'CalibrateESCLow' : '2',
                'ESCCalibrationOn' : '3',
                'ESCCalibrationOff' : '4',
                'SetMotorCommands' : '5',
                'GetMotorCommands' : '6' }
    
    def __init__(self, communicator, vehicle_event_dispatcher):
        ProtocolHandler.__init__(self, communicator, vehicle_event_dispatcher)

    def subscribe_sensors_data(self):
        def unpack_data():
            try :
                serial_data = self._date_output_queue.get()
                V32VehicleSensorsDataTranslator(serial_data, self._vehicle_event_dispatcher)
            except:
                logging.error("Protocol Handler: Failed to notify update vehicle raw sensors data")
                print "Protocol Handler: Failed to notify update vehicle raw sensors data"
            
        self.subscribe_command(self.COMMANDS['SubscribeSensor'], unpack_data)

    def subscribe_vehicle_status(self):
        def unpack_data():
            if not self._date_output_queue.empty():
                try :
                    serial_data = self._date_output_queue.get()
                    V32VehicleStatusTranslator(serial_data, self._vehicle_event_dispatcher)
                except:
                    logging.error("Protocol Handler: Failed to notify update vehicle status data")
                    print "Protocol Handler: Failed to notify update vehicle raw data"
                    
        self.subscribe_command(self.COMMANDS['SubscribeAllFlight'], unpack_data)

    def subscribe_raw_magnetometer(self):
        def unpack_data():
            if not self._date_output_queue.empty():
                try :
                    serial_data = self._date_output_queue.get()
                    values = serial_data.split(',')
                    magnetometer_raw_vector = Vector3D(values[0], values[1], values[2])
                    self._vehicle_event_dispatcher.dispatch_event(VehicleEventDispatcher.MAGNETOMETER_RAW_DATA_EVENT,magnetometer_raw_vector)
                except:
                    logging.error("Protocol Handler: Failed to notify update magnetometer raw data")
                    print "Protocol Handler: Failed to notify update magnetometer raw data"

        self.subscribe_command(self.COMMANDS['SubscribeRawMagnetometer'], unpack_data)

    def subscribe_raw_accelerometer(self):
        def unpack_data():
            try :
                serial_data = self._date_output_queue.get()
                splitted_data = serial_data.split(',')
                accel_raw_data_vector = Vector3D(float(splitted_data[0]),float(splitted_data[1]),float(splitted_data[2]))
                self._vehicle_event_dispatcher.dispatch_event(VehicleEventDispatcher.ACCEL_RAW_DATA_EVENT, accel_raw_data_vector)
            except:
                logging.error("Protocol Handler: Failed to notify update accel raw data")
                print "Protocol Handler: Failed to notify update accel raw data"

        self.subscribe_command(self.COMMANDS['SubscribeRawAccel'], unpack_data)
        
    def set_accel_calibration_scale_factor(self, x_scale_factor, y_scale_factor, z_scale_factor) :
        command = self.COMMANDS['SetAccelCalibration'] + ' '
        command = command + str(x_scale_factor)[0:8] + ';' + '0' + ';'
        command = command + str(y_scale_factor)[0:8] + ';' + '0' + ';'
        command = command + str(z_scale_factor)[0:8] + ';' + '0'
        self.send_command(command)
        

    def request_board_configuration(self):
        self.send_command(self.COMMANDS['GetBoardConfiguration'])
        number_of_lines = int(self.receive_command_data())
        for i in range(number_of_lines):
            board_properties = self.receive_command_data().split(':')
            self._vehicle_event_dispatcher.dispatch_event(board_properties[0],board_properties[1].strip())
            
    def subscribe_receiver_data(self):
        def unpack_data():
            if not self._date_output_queue.empty():
                try :
                    serial_data = self._date_output_queue.get()
                    V32ReceiverDataTranslator(serial_data, self._vehicle_event_dispatcher)
                except:
                    logging.error("Protocol Handler: Failed to notify update receiver data")
                    print "Protocol Handler: Failed to notify update receiver data"

        self.subscribe_command(self.COMMANDS['SubscribeProcessedTransmitter'], unpack_data)

