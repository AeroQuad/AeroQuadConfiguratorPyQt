
import logging
from communication.ProtocolHandler import ProtocolHandler
from model.Vector3D import Vector3D
from model.VehicleEventDispatcher import VehicleEventDispatcher
from communication.v32protocolhandler.V32VehicleStatusTranslator import V32VehicleStatusTranslator
from communication.v32protocolhandler.V32VehicleSensorsDataTranslator import V32VehicleSensorsDataTranslator
from communication.v32protocolhandler.V32ReceiverDataTranslator import V32ReceiverDataTranslator
from model.PIDData import PIDData

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
        
        self._motor_command = ''

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

    def send_motos_command(self,
                        nb_motors,
                        motor1_command,
                        motor2_command,
                        motor3_command,
                        motor4_command,
                        motor5_command,
                        motor6_command,
                        motor7_command,
                        motor8_command):
        
        command = self.COMMANDS['SetMotorCommands'] + ' '
        command = command + '123.45' + ';'
        command = command + str(motor1_command) + ';'
        command = command + str(motor2_command) + ';'
        command = command + str(motor3_command) + ';'
        command = command + str(motor4_command) 
        if int(nb_motors) > 4 :
            command = command + ';'
            command = command + str(motor5_command) + ';'
            command = command + str(motor6_command)
        if int(nb_motors) > 6 :
            command = command + ';'
            command = command + str(motor7_command) + ';'
            command = command + str(motor8_command)

        if self._motor_command != command:
            self.send_command(command)
            self._motor_command = command
        
    def reset_receiver_calibration_values(self, nb_channels):
        for channel in range(nb_channels):
            command = self.COMMANDS['SetTransmitterCalibration'] + ' '
            command = command + str(channel) + ';'
            command = command + '1.0'
        for channel in range(nb_channels):
            command = self.COMMANDS['SetTransmitterOffset'] + ' '
            command = command + str(channel) + ';'
            command = command + '0.0'
            
    
    def get_accro_pid(self):
        def unpack_data():
            if not self._date_output_queue.empty():
                try :
                    serial_data = self._date_output_queue.get().split(',')
                    accroRollPidData = PIDData(serial_data[0],serial_data[1],serial_data[2])
                    self._vehicle_event_dispatcher.dispatch_event(VehicleEventDispatcher.PID_ACCRO_ROLL,accroRollPidData)
                    accroPitchPidData = PIDData(serial_data[3],serial_data[4],serial_data[5])
                    self._vehicle_event_dispatcher.dispatch_event(VehicleEventDispatcher.PID_ACCRO_PITCH,accroPitchPidData)
                    self._vehicle_event_dispatcher.dispatch_event(VehicleEventDispatcher.PID_ACCRO_STICK_SCALING,serial_data[6])
                except:
                    logging.error("Protocol Handler: Failed to notify update rate PID data")
                    print "Protocol Handler: Failed to notify update rate PID data"
                    
                self.unsubscribe_command()

        self.subscribe_command(self.COMMANDS['GetRatePID'], unpack_data)
        
    def send_receiver_calibation_values(self, nb_channels, min_values, max_values):
        # @todo do the math and send the command here
        pass
        
    def send_mag_calibration_values(self, min_values, max_values):
        # @todo do the math and send the command here
        pass
    
    
        
        