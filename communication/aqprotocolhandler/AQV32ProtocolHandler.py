
from communication.aqprotocolhandler.ProtocolHandler import ProtocolHandler
from model.Vector3D import Vector3D
from model.EventDispatcher import EventDispatcher
import logging


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
                'UnsubscribeSensor'  : 'X',
                'SubscribeRawMagnetometer' : 'j',
                'UnsubscribeRawMagnetometer' : 'X',
                'GetAccelCalibration' : 'k',
                'SetAccelCalibration' : 'K',
                'SubscribeRawAccel' : 'l',
                'UnsubscribeRawAccel' : 'X',
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
                'UnsubscribeVehicleAttitude' : 'X',
                'SubscribeAllFlight' : 's',
                'UnsubscribeAllFlight' : 'X',
                'SubscribeProcessedTransmitter' : 't',
                'UnsubscribeProcessedTransmitter' : 'X',
                'GetRangeFinder' : 'u',
                'SetRangeFinder' : 'U',
                'GetGPSPID' : 'v',
                'SetGPSPID' : 'V',
                'GetGPSStatus' : 'y',
                'SubscribeAltitude' : 'z',
                'UnsubscribeAltitude' : 'X',
                'SubscribeVoltageCurrent' : '$',
                'UnsubscribeVoltageCurrent' : 'X',
                'SubscribeRSSI' : '%',
                'UnsubscribeRSSI' : 'X',
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
    
    def __init__(self, communicator, event_dispatcher):
        ProtocolHandler.__init__(self, communicator, event_dispatcher)
        
#    def get_rate_PID(self):
#        self.send_command(self.COMMANDS['GetRatePID'])
#        return [float(i) for i in self.receiveCommandData().rstrip(',').split(',')]
#
#    def set_rate_PID(self, rollP, rollI, rollD, pitchP, pitchI, pitchD, rotSpeedFactor):
#        command_data = ('{:.4f};'*7).format(rollP, rollI, rollD,pitchP, pitchI, pitchD,rotSpeedFactor)
#        self.send_command(self.COMMANDS['SetRatePID'] + command_data)
#        self.flush_command_data()
#
#    def get_attitude_PID(self):
#        self.send_command(self.COMMANDS['GetAttitudePID'])
#        return [float(i) for i in self.receive_command_data().rstrip(',').split(',')]
#
#    def set_attitude_PID(self, rollAccelP, rollAccelI, rollAccelD, pitchAccelP, pitchAccelI, pitchAccelD, rollP, rollI, rollD, pitchP, pitchI, pitchD, windupGuard):
#        command_data = ('{:.4f};'*13).format(rollAccelP, rollAccelI, rollAccelD, pitchAccelP, pitchAccelI, pitchAccelD, rollP, rollI, rollD, pitchP, pitchI, pitchD, windupGuard)
#        self.send_command(self.COMMANDS['SetAttitudePID']+command_data)
#        self.flush_command_data()
#
#    def get_accel_calibration(self):
#        self.send_command(self.COMMANDS['GetAccelCalibration'])
#        return [float(i) for i in self.receiveCommandData().rstrip(',').split(',')]
#
#    def set_accel_calibration(self, scaleX, biasX, scaleY, biasY, scaleZ, biasZ):
#        command_data = ('{:.4f};'*6).format(scaleX, biasX, scaleY, biasY, scaleZ, biasZ)
#        self.send_command(self.COMMANDS['SetAccelCalibration']+command_data)
#        self.flush_command_data()
#
#    def initialize_EEPROM(self):
#        self.send_command(self.COMMANDS['InitializeEEPROM'])
#        self.flush_command_data()
#
#    def generate_accel_bias(self):
#        self.send_command(self.COMMANDS['GenerateAccelBias'])
#        self.flush_command_data()
#
#    def subscribe_sensors(self, callback):
#        def unpack_data(data):
#            args = [t(s) for t,s in zip((float,)*7+(int,)*2,data.split(','))]
#            return callback(*args)
#        self.subscribe_command(self.COMMANDS['SubscribeSensor'], unpack_data)
#
#    def unsubscribe_sensors(self):
#        self.unsubscribe_command(self.COMMANDS['UnsubscribeSensor'])


    def subscribe_raw_magnetometer(self):
        def unpack_data():
            if not self._date_output_queue.empty():
                try :
                    serial_data = self._date_output_queue.get()
                    values = serial_data.split(',')
                    magnetometer_raw_vector = Vector3D(values[0], values[1], values[2])
                    self._event_dispatcher.dispatch_event(EventDispatcher.MAGNETOMETER_RAW_DATA_EVENT,magnetometer_raw_vector)
                except:
                    logging.error("Protocol Handler: Failed to notify update magnetometer raw data")

        self.subscribe_command(self.COMMANDS['SubscribeRawMagnetometer'], unpack_data)

#    def unsubscribe_raw_magnetometer(self):
#        self.unsubscribe_command(self.COMMANDS['UnsubscribeRawMagnetometer'])
#
#    def subscribe_raw_accelerometer(self, callback):
#        def unpack_data(data):
#            args = [t(s) for t,s in zip((int,)*3,data.split(','))]
#            return callback(*args)
#        self.subscribe_command(self.COMMANDS['SubscribeRawAccel'], unpack_data)
#
#    def unsubscribe_raw_accelerometer(self):
#        self.unsubscribe_command(self.COMMANDS['UnsubscribeRawAccel'])

    def request_board_configuration(self):
        self.send_command(self.COMMANDS['GetBoardConfiguration'])
        number_of_lines = int(self.receive_command_data())
        for i in range(number_of_lines):
            board_properties = self.receive_command_data().split(':')
            self._event_dispatcher.dispatch_event(board_properties[0],board_properties[1].strip())
            
