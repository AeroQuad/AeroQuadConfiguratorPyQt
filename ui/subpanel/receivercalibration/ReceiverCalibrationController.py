
from PyQt4 import QtCore, QtGui
from ui.subpanel.BasePanelController import BasePanelController
from ui.subpanel.receivercalibration.ReceiverCalibrationPanel import Ui_ReceiverCalibrationPanel
from ui.UIEventDispatcher import UIEventDispatcher
from model.VehicleEventDispatcher import VehicleEventDispatcher

class ReceiverCalibrationController(QtGui.QWidget, BasePanelController):

    def __init__(self, vehicle_event_dispatcher, ui_event_dispatcher):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        self.ui = Ui_ReceiverCalibrationPanel()
        self.ui.setupUi(self)
        self.ui.start.setEnabled(True)
        self.ui.cancel.setEnabled(False)
        
        leftStickScene = QtGui.QGraphicsScene()
        leftStickBackground = QtGui.QPixmap("./resources/TxDial.png")
        leftStickItem = QtGui.QGraphicsPixmapItem(leftStickBackground)
        leftStickScene.addItem(leftStickItem)
        self.leftStick = QtGui.QGraphicsEllipseItem(QtCore.QRectF(75, 75, 30, 30))
        self.leftStick.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black, QtCore.Qt.SolidPattern), 2))
        self.leftStick.setBrush(QtGui.QBrush(QtCore.Qt.blue, QtCore.Qt.SolidPattern))
        leftStickScene.addItem(self.leftStick)
        self.ui.leftTransmitter.setScene(leftStickScene)
        
        rightStickScene = QtGui.QGraphicsScene()
        rightStickBackground = QtGui.QPixmap("./resources/TxDial.png")
        rightStickItem = QtGui.QGraphicsPixmapItem(rightStickBackground)
        rightStickScene.addItem(rightStickItem)
        self.rightStick = QtGui.QGraphicsEllipseItem(QtCore.QRectF(75, 75, 30, 30))
        self.rightStick.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black, QtCore.Qt.SolidPattern), 2))
        self.rightStick.setBrush(QtGui.QBrush(QtCore.Qt.blue, QtCore.Qt.SolidPattern))
        rightStickScene.addItem(self.rightStick)
        self.ui.rightTransmitter.setScene(rightStickScene)   
        
        self._nb_channels = 12
        self._raw_receiver_min_values = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]
        self._raw_receiver_max_values = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]
        self.max_amount_channels = 12
        
        self._raw_roll = 1500
        self._raw_pitch = 1500
        self._raw_yaw = 1500
        self._raw_throttle = 1500
        
        self.ui.start.clicked.connect(self.start_RCcalibration)
        self.ui.cancel.clicked.connect(self._cancel_calibration)
        
        ui_event_dispatcher.register(self._protocol_handler_changed_event, UIEventDispatcher.PROTOCOL_HANDLER_EVENT)
        vehicle_event_dispatcher.register(self._receiver_channel_count_received, VehicleEventDispatcher.RECEIVER_NB_CHANNEL_EVENT)
        
        vehicle_event_dispatcher.register(self._receiver_raw_roll_received, VehicleEventDispatcher.RECEIVER_ROLL_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_raw_pitch_received, VehicleEventDispatcher.RECEIVER_PITCH_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_raw_yaw_received, VehicleEventDispatcher.RECEIVER_YAW_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_raw_throttle_received, VehicleEventDispatcher.RECEIVER_THROTTLE_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_raw_mode_received, VehicleEventDispatcher.RECEIVER_MODE_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_raw_aux1_received, VehicleEventDispatcher.RECEIVER_AUX1_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_raw_aux2_received, VehicleEventDispatcher.RECEIVER_AUX2_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_raw_aux3_received, VehicleEventDispatcher.RECEIVER_AUX3_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_raw_aux4_received, VehicleEventDispatcher.RECEIVER_AUX4_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_raw_aux5_received, VehicleEventDispatcher.RECEIVER_AUX5_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_raw_aux6_received, VehicleEventDispatcher.RECEIVER_AUX6_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_raw_aux7_received, VehicleEventDispatcher.RECEIVER_AUX7_PROPERTY_EVENT)

    def _protocol_handler_changed_event(self, event, protocol_handler):
        self._protocol_handler = protocol_handler;
        
    def _receiver_channel_count_received(self, event, nb_channels):
        self._nb_channels = int(nb_channels)
        self._update_panel_display()
         
    def start(self):
        self._protocol_handler.unsubscribe_command()
    
    def stop(self):
        self._cancel_calibration()

    def start_RCcalibration(self):
        if self.ui.start.text() == 'Start' :
            self.ui.cancel.setEnabled(True)
            self.ui.next.setEnabled(False)
            self.ui.start.setText("Finish")
            self._raw_receiver_min_values = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]
            self._raw_receiver_max_values = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]
            
            self._protocol_handler.reset_receiver_calibration_values(self._nb_channels)
            self._protocol_handler.subscribe_receiver_data()
        else :
            self._send_calibration_value()
            self._cancel_calibration()
        
    def _receiver_raw_roll_received(self, event, raw_roll):
        self._raw_roll = int(raw_roll)
        self._compute_min_max_value(self._raw_roll,0)
        self._update_right_stick(self._raw_roll, self._raw_pitch)

    def _receiver_raw_pitch_received(self, event, raw_pitch):
        self._raw_pitch = int(raw_pitch)
        self._compute_min_max_value(self._raw_pitch,1)
        self._update_right_stick(self._raw_roll, self._raw_pitch)

    def _receiver_raw_yaw_received(self, event, raw_yaw):
        self._raw_yaw = int(raw_yaw)
        self._compute_min_max_value(self._raw_yaw,2)
        self._update_left_stick(self._raw_throttle, self._raw_yaw)

    def _receiver_raw_throttle_received(self, event, raw_throttle):
        self._raw_throttle = int(raw_throttle)
        self._compute_min_max_value(self._raw_throttle,3)
        self._update_left_stick(self._raw_throttle, self._raw_yaw)

    def _receiver_raw_mode_received(self, event, raw_mode):
        self._compute_min_max_value(int(raw_mode),4)
        self.ui.progressBar_RCmode.setValue(int(raw_mode))

    def _receiver_raw_aux1_received(self, event, raw_aux1):
        self._compute_min_max_value(int(raw_aux1),5)
        self.ui.progressBar_RCAux1.setValue(int(raw_aux1))

    def _receiver_raw_aux2_received(self, event, raw_aux2):
        self._compute_min_max_value(int(raw_aux2),6)
        self.ui.progressBar_RCAux2.setValue(int(raw_aux2))

    def _receiver_raw_aux3_received(self, event, raw_aux3):
        self._compute_min_max_value(int(raw_aux3),7)
        self.ui.progressBar_RCAux3.setValue(int(raw_aux3))

    def _receiver_raw_aux4_received(self, event, raw_aux4):
        self._compute_min_max_value(int(raw_aux4),8)
        self.ui.progressBar_RCAux4.setValue(int(raw_aux4))

    def _receiver_raw_aux5_received(self, event, raw_aux5):
        self._compute_min_max_value(int(raw_aux5),9)
        self.ui.progressBar_RCAux5.setValue(int(raw_aux5))

    def _receiver_raw_aux6_received(self, event, raw_aux6):
        self._compute_min_max_value(int(raw_aux6),10)
        self.ui.progressBar_RCAux6.setValue(int(raw_aux6))

    def _receiver_raw_aux7_received(self, event, raw_aux7):
        self._compute_min_max_value(int(raw_aux7),11)
        self.ui.progressBar_RCAux7.setValue(int(raw_aux7))

    def _compute_min_max_value(self, value, channel):
        self._raw_receiver_min_values[channel] = min(self._raw_receiver_min_values[channel],value)
        self._raw_receiver_max_values[channel] = max(self._raw_receiver_max_values[channel],value)

    def _cancel_calibration(self):
        self._protocol_handler.unsubscribe_command()
        self.ui.cancel.setEnabled(False)
        self.ui.next.setEnabled(True)
        self.ui.start.setText("Start")
    
    def _update_left_stick(self, throttle, yaw):
        throttlePosition = self._scale_stick_display_value(throttle, (1000.0, 2000.0), (58.0, -57.0))
        yawPosition = self._scale_stick_display_value(yaw, (1000.0, 2000.0), (-57.0, 55.0))
        self.leftStick.setPos(yawPosition, throttlePosition)
        
    def _update_right_stick(self, roll, pitch):
        rollPosition = self._scale_stick_display_value(roll, (1000.0, 2000.0), (-57.0, 55.0))
        pitchPosition = self._scale_stick_display_value(pitch, (1000.0, 2000.0), (58.0, -57.0))
        self.rightStick.setPos(rollPosition, pitchPosition)
    
    def _scale_stick_display_value(self, val, src, dst):
        return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]
    
    def _update_panel_display(self):
        for i in range(0, self.max_amount_channels):
            if i > (self._nb_channels - 1) and i == 5:
                self.ui.label_aux1.hide()
                self.ui.progressBar_RCAux1.hide()
            elif i > (self._nb_channels - 1) and i == 6:
                self.ui.label_aux2.hide()
                self.ui.progressBar_RCAux2.hide()
            elif i > (self._nb_channels - 1) and i == 7:
                self.ui.label_aux3.hide()
                self.ui.progressBar_RCAux3.hide()
            elif i > (self._nb_channels - 1) and i == 8:
                self.ui.label_aux4.hide()
                self.ui.progressBar_RCAux4.hide()
            elif i > (self._nb_channels - 1) and i == 9:
                self.ui.label_aux5.hide()
                self.ui.progressBar_RCAux5.hide()
            elif i > (self._nb_channels - 1) and i == 10:
                self.ui.label_aux6.hide()
                self.ui.progressBar_RCAux6.hide()
            elif i > (self._nb_channels - 1) and i == 11:
                self.ui.label_aux7.hide()
                self.ui.progressBar_RCAux7.hide()
    
    def _send_calibration_value(self):
        print "done"
#        self._communicator.write("X");
#        command = "G "
#        for i in range(0, self._nb_channels):
#            command += str(self._raw_receiver_min_values[i])
#            command += ";"
#            command += str(self._raw_receiver_max_values[i])
#            command += ";"
#            
#        self._communicator.write(command)    
        