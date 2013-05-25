
from PyQt4 import QtCore, QtGui
from model.VehicleEventDispatcher import VehicleEventDispatcher
from model.VehicleConfigImageMap import VEHICLE_CONFIG_FILE_MAP
from ui.subpanel.BasePanelController import BasePanelController
from utilities.specialwidgets.BarGauge import BarGauge
from ui.subpanel.vehicleoverallstatus.VehicleOverallStatusPanel import Ui_VehicleOverallStatusPanel
import math
from ui.UIEventDispatcher import UIEventDispatcher

class VehicleOverallStatusController(QtGui.QWidget, BasePanelController):
    
    MOTORS_GAUGE_POSITION = {'Quad +'     : ((182,22), (300,140), (182,255), (62,140)),
                             'Quad X'     : ((80,35), (280,35), (80,240), (280,240)),
                             'Quad Y4'    : ((66,23), (222,23), (145,260), (300,260)),
                             'Tri'        : ((330,240), (80,35), (285,35), (182,240)),
                             'Hex +'      : ((235,30), (390,100), (390,275),(235,350), (75,275), (75,100)),
                             'Hex X'      : ((150,30), (320,30), (390,190), (320,350), (150,350), (75,190)),
                             'Hex Y6'     : ((50,45), (170,45), (170,340), (295,45), (420,45), (300,340)),
                             'Octo X8'    : ((192,27), (325,190), (192,350), (55,190),(275,27), (410,190), (275,350), (140,190)),
                             'Octo X'     : ((165,25), (295,25), (385,130), (385,260), (295,350), (165,350), (70,260), (70,130)),
                             'Octo X+'    : ((235,30), (360,65), (395,185), (360,315), (235,350), (110,315), (75,185), (110,65)) }

    
    def __init__(self, vehicle_event_dispatcher, ui_event_dispatcher):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        self.ui = Ui_VehicleOverallStatusPanel()
        self.ui.setupUi(self)
        
        self._channel_count = 0
        self._flight_config = 'Quad +'
        self._channel_bar_gauge_array = []
        self._channels_label_array_text = ['Mode']
        self._channels_label_array_object = []
        self._motor_gauge_pixel_width = 25.0
        self._label_pixel_height = 25
        self._window_height = 400
        
        self._motors_count = 4
        self._vehicle_roll = 0.0
        self._vehicle_pitch = 0.0
        
        self._receiver_roll = 0
        self._receiver_pitch = 0
        self._receiver_yaw = 0
        self._receiver_throttle = 0

        horizon_background_image = QtGui.QPixmap('./resources/artificialHorizonBackGround.svg')
        self._horizon_background_image = QtGui.QGraphicsPixmapItem(horizon_background_image)
        
        horizon_dial_image = QtGui.QPixmap('./resources/artificialHorizonDial.svg')
        horizon_dial_item = QtGui.QGraphicsPixmapItem(horizon_dial_image)
        horizon_dial_item.setPos(QtCore.QPointF(100.0, 390.0))
             
        horizon_compass_background = QtGui.QPixmap('./resources/artificialHorizonCompassBackGround.svg')
        horizon_compass_background_item = QtGui.QGraphicsPixmapItem(horizon_compass_background)
        horizon_compass_background_item.setPos(QtCore.QPointF(100.0, 390.0))
                       
        horizon_compass = QtGui.QPixmap('./resources/artificialHorizonCompass.svg')
        self._horizon_compass_item = QtGui.QGraphicsPixmapItem(horizon_compass)
        self._horizon_compass_item.setPos(QtCore.QPointF(100.0, 390.0)) 
        
        horizon_scene = QtGui.QGraphicsScene()
        horizon_scene.addItem(self._horizon_background_image)
        horizon_scene.addItem(horizon_dial_item)
        horizon_scene.addItem(horizon_compass_background_item)
        horizon_scene.addItem(self._horizon_compass_item)

        # Setup text info in artificial horizon_background_image
        rollLabel = horizon_scene.addText('Roll:')
        rollLabel.setDefaultTextColor(QtCore.Qt.white)
        rollLabel.setPos(102, 420)
        self.roll = horizon_scene.addText('0.0')
        self.roll.setDefaultTextColor(QtCore.Qt.white)
        self.roll.setPos(125, 420)
        pitchLabel = horizon_scene.addText('Pitch:')
        pitchLabel.setDefaultTextColor(QtCore.Qt.white)
        pitchLabel.setPos(102, 405)
        self.pitch = horizon_scene.addText('0.0')
        self.pitch.setDefaultTextColor(QtCore.Qt.white)
        self.pitch.setPos(132, 405)
        headingLabel = horizon_scene.addText('Heading:')
        headingLabel.setDefaultTextColor(QtCore.Qt.white)
        headingLabel.setPos(102, 390)
        self.heading = horizon_scene.addText('0.0')
        self.heading.setDefaultTextColor(QtCore.Qt.white)
        self.heading.setPos(147, 390)
        altitudeLabel = horizon_scene.addText('Altitude:')
        altitudeLabel.setDefaultTextColor(QtCore.Qt.white)
        altitudeLabel.setPos(320, 390)
        self.altitude = horizon_scene.addText('000.0')
        self.altitude.setDefaultTextColor(QtCore.Qt.white)
        self.altitude.setPos(363, 390)
        altHoldLabel = horizon_scene.addText('Alt Hold:')
        altHoldLabel.setDefaultTextColor(QtCore.Qt.white)
        altHoldLabel.setPos(331, 405)
        self.altitudeHold = horizon_scene.addText('Off')
        self.altitudeHold.setDefaultTextColor(QtCore.Qt.red)
        self.altitudeHold.setPos(374, 405)
        armLabel = horizon_scene.addText('Motors:')
        armLabel.setDefaultTextColor(QtCore.Qt.white)
        armLabel.setPos(102, 653)
        self.motorArm = horizon_scene.addText('Not Armed')
        self.motorArm.setDefaultTextColor(QtCore.Qt.red)
        self.motorArm.setPos(102, 668)
        battLabel = horizon_scene.addText('Batt:')
        battLabel.setDefaultTextColor(QtCore.Qt.white)
        battLabel.setPos(330, 653)
        self.batteryPower = horizon_scene.addText('0.000')
        self.batteryPower.setDefaultTextColor(QtCore.Qt.white)
        self.batteryPower.setPos(357, 653)
        modeLabel = horizon_scene.addText('Mode:')
        modeLabel.setDefaultTextColor(QtCore.Qt.white)
        modeLabel.setPos(330, 668)
        self.flightMode = horizon_scene.addText('Acro')
        self.flightMode.setDefaultTextColor(QtCore.Qt.yellow)
        self.flightMode.setPos(362, 668)
        self.ui.artificialHorizon.setScene(horizon_scene)
        
        # Setup left transmitter stick
        leftStickScene = QtGui.QGraphicsScene()
        leftStickBackground = QtGui.QPixmap('./resources/TxDial.png')
        leftStickItem = QtGui.QGraphicsPixmapItem(leftStickBackground)
        leftStickScene.addItem(leftStickItem)
        self.leftStick = QtGui.QGraphicsEllipseItem(QtCore.QRectF(75, 75, 30, 30))
        self.leftStick.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black, QtCore.Qt.SolidPattern), 2))
        self.leftStick.setBrush(QtGui.QBrush(QtCore.Qt.blue, QtCore.Qt.SolidPattern))
        leftStickScene.addItem(self.leftStick)
        self.ui.leftTransmitter.setScene(leftStickScene)
        
        # Setup right transmitter stick
        rightStickScene = QtGui.QGraphicsScene()
        rightStickBackground = QtGui.QPixmap('./resources/TxDial.png')
        rightStickItem = QtGui.QGraphicsPixmapItem(rightStickBackground)
        rightStickScene.addItem(rightStickItem)
        self.rightStick = QtGui.QGraphicsEllipseItem(QtCore.QRectF(75, 75, 30, 30))
        self.rightStick.setPen(QtGui.QPen(QtGui.QBrush(QtCore.Qt.black, QtCore.Qt.SolidPattern), 2))
        self.rightStick.setBrush(QtGui.QBrush(QtCore.Qt.blue, QtCore.Qt.SolidPattern))
        rightStickScene.addItem(self.rightStick)
        self.ui.rightTransmitter.setScene(rightStickScene)
        
        vehicle_event_dispatcher.register(self._flight_config_received, VehicleEventDispatcher.FLIGHT_CONFIG_EVENT)
        vehicle_event_dispatcher.register(self._receiver_channel_count_received, VehicleEventDispatcher.RECEIVER_NB_CHANNEL_EVENT)
        vehicle_event_dispatcher.register(self._motors_count_received, VehicleEventDispatcher.NUMBER_MOTORS_EVENT)
        vehicle_event_dispatcher.register(self._motor_armed_event, VehicleEventDispatcher.MOTOR_ARMED_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._vehicle_roll_event, VehicleEventDispatcher.VEHICLE_ROLL_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._vehicle_pitch_event, VehicleEventDispatcher.VEHICLE_PITCH_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._vehicle_heading_event, VehicleEventDispatcher.VEHICLE_HEADING_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._vehicle_altitude_hold_state_event, VehicleEventDispatcher.ALTITUDE_HOLD_STATE_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._vehicle_altitude_event, VehicleEventDispatcher.VEHICLE_ALTITUDE_PROPERTY_EVENT)
        
        vehicle_event_dispatcher.register(self._receiver_roll_event, VehicleEventDispatcher.RECEIVER_ROLL_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_pitch_event, VehicleEventDispatcher.RECEIVER_PITCH_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_yaw_event, VehicleEventDispatcher.RECEIVER_YAW_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_throttle_event, VehicleEventDispatcher.RECEIVER_THROTTLE_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_mode_event, VehicleEventDispatcher.RECEIVER_MODE_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_aux1_event, VehicleEventDispatcher.RECEIVER_AUX1_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_aux2_event, VehicleEventDispatcher.RECEIVER_AUX2_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_aux3_event, VehicleEventDispatcher.RECEIVER_AUX3_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_aux4_event, VehicleEventDispatcher.RECEIVER_AUX4_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_aux5_event, VehicleEventDispatcher.RECEIVER_AUX5_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_aux6_event, VehicleEventDispatcher.RECEIVER_AUX6_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_aux7_event, VehicleEventDispatcher.RECEIVER_AUX7_PROPERTY_EVENT)
        
        vehicle_event_dispatcher.register(self._motor1_throttle_event, VehicleEventDispatcher.MOTOR1_THROTTLE_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._motor2_throttle_event, VehicleEventDispatcher.MOTOR2_THROTTLE_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._motor3_throttle_event, VehicleEventDispatcher.MOTOR3_THROTTLE_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._motor4_throttle_event, VehicleEventDispatcher.MOTOR4_THROTTLE_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._motor5_throttle_event, VehicleEventDispatcher.MOTOR5_THROTTLE_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._motor6_throttle_event, VehicleEventDispatcher.MOTOR6_THROTTLE_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._motor7_throttle_event, VehicleEventDispatcher.MOTOR7_THROTTLE_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._motor8_throttle_event, VehicleEventDispatcher.MOTOR8_THROTTLE_PROPERTY_EVENT)
        
        vehicle_event_dispatcher.register(self._flight_mode_event, VehicleEventDispatcher.FLIGHT_MODE_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._battery_voltage_received, VehicleEventDispatcher.BATTERY_VOLTAGE_PROPERTY_EVENT)
        
        ui_event_dispatcher.register(self._protocol_handler_changed_event, UIEventDispatcher.PROTOCOL_HANDLER_EVENT)
        
    def _protocol_handler_changed_event(self, event, protocol_handler):
        self._protocol_handler = protocol_handler;
        
    def _flight_config_received(self, event, flight_config):
        self._flight_config = flight_config
        
    def _receiver_channel_count_received(self, event, channel_count):
        self._channel_count = int(channel_count)
        if (self._channel_count == 5) :
            self._channels_label_array_text = ['Mode']
        elif (self._channel_count == 6) :
            self._channels_label_array_text = ['Mode', 'Aux1']
        elif (self._channel_count == 7) :
            self._channels_label_array_text = ['Mode', 'Aux1', 'Aux2']
        elif (self._channel_count == 8) :
            self._channels_label_array_text = ['Mode', 'Aux1', 'Aux2', 'Aux3']
        elif (self._channel_count == 9) :
            self._channels_label_array_text = ['Mode', 'Aux1', 'Aux2', 'Aux3', 'Aux4']
        else :
            self._channels_label_array_text = ['Mode', 'Aux1', 'Aux2', 'Aux3', 'Aux4', 'Aux5']
        
        transmitterScene = QtGui.QGraphicsScene()
        for channel in range(self._channel_count-4):
            barGauge = QtGui.QGraphicsRectItem()
            barGauge.setBrush(QtGui.QBrush(QtCore.Qt.blue, QtCore.Qt.SolidPattern))
            self._channel_bar_gauge_array.append(barGauge)
            transmitterScene.addItem(self._channel_bar_gauge_array[channel])
            label = transmitterScene.addText(self._channels_label_array_text[channel])
            label.setDefaultTextColor(QtCore.Qt.white)
            label.setPos(self.compute_channel_bar_location(channel), self.ui.transmitterOutput.height())
            self._channels_label_array_object.append(label)
        self.ui.transmitterOutput.setScene(transmitterScene)     
        
        for channel in range(self._channel_count-4):
            self._update_receiver_bar_widget(channel, 1000)
            self._channels_label_array_object[channel].setPos(self.compute_channel_bar_location(channel) - 3, self.ui.transmitterOutput.height() - self._label_pixel_height)
            
        self.ui.transmitterOutput.centerOn(0.0, 0.0)
   
    def _motors_count_received(self, event, motors_count):
        self._motors_count = int(motors_count)
        motorScene = QtGui.QGraphicsScene()
        self.motor = []
        motorLocation = VehicleOverallStatusController.MOTORS_GAUGE_POSITION[self._flight_config]
        for motorIndex in range(int(motors_count)):
            self.motor.append(BarGauge('Motor ' + str(motorIndex+1)))
            self.motor[motorIndex].setPos(motorLocation[motorIndex][0], motorLocation[motorIndex][1])
            motorScene.addItem(self.motor[motorIndex])
        self.ui.motorView.setScene(motorScene)
        vehicleImage = QtGui.QPixmap(VEHICLE_CONFIG_FILE_MAP[self._flight_config])
        scaledImage = vehicleImage.scaled(400, 400, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        motorScene.addPixmap(scaledImage)
        
    def _motor_armed_event(self, event, are_motor_armed):
        if are_motor_armed :
            self.motorArm.setPlainText('Armed')
            self.motorArm.setDefaultTextColor(QtCore.Qt.green)
        else :
            self.motorArm.setPlainText('Not Armed')
            self.motorArm.setDefaultTextColor(QtCore.Qt.red)
            
    def _vehicle_roll_event(self, event, vehicle_roll):
        self._vehicle_roll = math.degrees(vehicle_roll)
        self.roll.setPlainText('{:.1f}'.format(self._vehicle_roll))
        self._update_pitch_poll_widget(self._vehicle_roll,self._vehicle_pitch)
        
    def _vehicle_pitch_event(self, event, vehicle_pitch):
        self._vehicle_pitch = math.degrees(vehicle_pitch)
        self.pitch.setPlainText('{:.1f}'.format(self._vehicle_pitch))
        self._update_pitch_poll_widget(self._vehicle_roll,self._vehicle_pitch)        

    def _update_pitch_poll_widget(self, rollAngle, pitchAngle):
        pitchPosition = self._scale_receiver_channel_to_widget(-pitchAngle, (-135.0, 135.0), (540.0, -540.0))
        rollCenter = self._scale_receiver_channel_to_widget(-pitchAngle, (-135.0, 135.0), (0, 1080.0))
        self._horizon_background_image.setPos(0, pitchPosition)
        self._horizon_background_image.setTransformOriginPoint(250.0, rollCenter)
        self._horizon_background_image.setRotation(-rollAngle)

    def _vehicle_heading_event(self, event, vehicle_heading):            
        heading = math.degrees(vehicle_heading)
        self.heading.setPlainText('{:.1f}'.format(heading).zfill(5))
        self._horizon_compass_item.setTransformOriginPoint(150.0, 150.0)
        self._horizon_compass_item.setRotation(-heading)
        
    def _vehicle_altitude_hold_state_event(self, event, vehicle_altitude):
        if vehicle_altitude == '1':
            self.altitudeHold.setPlainText('On')
            self.altitudeHold.setDefaultTextColor(QtCore.Qt.green)
        else:
            self.altitudeHold.setPlainText('Off')
            self.altitudeHold.setDefaultTextColor(QtCore.Qt.red)
        
    def _vehicle_altitude_event(self, event, vehicle_altitude):
        self.altitude.setPlainText('{:.1f}'.format(vehicle_altitude).zfill(5))
        
    def _receiver_roll_event(self, event, roll):
        self._receiver_roll = roll
        self._update_right_stick_widget(self._receiver_roll, self._receiver_pitch)
    
    def _receiver_pitch_event(self, event, pitch):
        self._receiver_pitch = pitch
        self._update_right_stick_widget(self._receiver_roll, self._receiver_pitch)
        
    def _update_right_stick_widget(self, roll, pitch):
        rollPosition = self._scale_receiver_channel_to_widget(roll, (1000.0, 2000.0), (-57.0, 55.0))
        pitchPosition = self._scale_receiver_channel_to_widget(pitch, (1000.0, 2000.0), (58.0, -57.0))
        self.rightStick.setPos(rollPosition, pitchPosition)        
    
    def _receiver_yaw_event(self, event, yaw):
        self._receiver_yaw = yaw
        self._update_left_stick_widget(self._receiver_throttle, self._receiver_yaw)
    
    def _receiver_throttle_event(self, event, throttle):
        self._receiver_throttle = throttle
        self._update_left_stick_widget(self._receiver_throttle, self._receiver_yaw)
    
    def _update_left_stick_widget(self, throttle, yaw):
        throttlePosition = self._scale_receiver_channel_to_widget(throttle, (1000.0, 2000.0), (58.0, -57.0))
        yawPosition = self._scale_receiver_channel_to_widget(yaw, (1000.0, 2000.0), (-57.0, 55.0))
        self.leftStick.setPos(yawPosition, throttlePosition)
        
    def _scale_receiver_channel_to_widget(self, val, src, dst):
        return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]
    
    def _receiver_mode_event(self, event, mode):
        self._update_receiver_bar_widget(0, mode)
    
    def _receiver_aux1_event(self, event, aux1):
        if self._channel_count >= 6 :
            self._update_receiver_bar_widget(1, aux1)
    
    def _receiver_aux2_event(self, event, aux2):
        if self._channel_count >= 7 :
            self._update_receiver_bar_widget(2, aux2)
    
    def _receiver_aux3_event(self, event, aux3):
        if self._channel_count >= 8 :
            self._update_receiver_bar_widget(3, aux3)
    
    def _receiver_aux4_event(self, event, aux4):
        if self._channel_count >= 9 :
            self._update_receiver_bar_widget(4, aux4)
    
    def _receiver_aux5_event(self, event, aux5):
        if self._channel_count >= 10 :
            self._update_receiver_bar_widget(5, aux5)
    
    def _receiver_aux6_event(self, event, aux6):
        if self._channel_count >= 11 :
            self._update_receiver_bar_widget(6, aux6)
    
    def _receiver_aux7_event(self, event, aux7):
        if self._channel_count >= 12 :
            self._update_receiver_bar_widget(7, aux7)
            
    def _motor1_throttle_event(self, event, motor1_throttle):
        self.motor[0].setValue(motor1_throttle)

    def _motor2_throttle_event(self, event, motor2_throttle):
        self.motor[1].setValue(motor2_throttle)

    def _motor3_throttle_event(self, event, motor3_throttle):
        self.motor[2].setValue(motor3_throttle)

    def _motor4_throttle_event(self, event, motor4_throttle):
        self.motor[3].setValue(motor4_throttle)

    def _motor5_throttle_event(self, event, motor5_throttle):
        if self._motors_count >= 6 :
            self.motor[4].setValue(motor5_throttle)

    def _motor6_throttle_event(self, event, motor6_throttle):
        if self._motors_count >= 6 :
            self.motor[5].setValue(motor6_throttle)

    def _motor7_throttle_event(self, event, motor7_throttle):
        if self._motors_count >= 8 :
            self.motor[6].setValue(motor7_throttle)

    def _motor8_throttle_event(self, event, motor8_throttle):
        if self._motors_count >= 8 :
            self.motor[7].setValue(motor8_throttle)
            
    def _flight_mode_event(self, event, flight_mode):
        self.flightMode.setPlainText(flight_mode)
        if flight_mode == 'Accro':
            self.flightMode.setDefaultTextColor(QtCore.Qt.yellow)
        else:
            self.flightMode.setDefaultTextColor(QtCore.Qt.green)
    
    def _battery_voltage_received(self, event, battery_voltage):
        self.batteryPower.setPlainText('{:.3f}'.format(battery_voltage))
        
    def start(self):
        print 'START'
        self._protocol_handler.unsubscribe_command()
        self._protocol_handler.subscribe_vehicle_status()
    
    def stop(self):
        self._protocol_handler.unsubscribe_command()
    
    def _update_receiver_bar_widget(self, channel, value):
        output = self._scale_receiver_channel_to_widget(value, (1000.0, 2000.0), (25.0, self._window_height - 10)) - self._label_pixel_height
        self._channel_bar_gauge_array[channel].setRect(self.compute_channel_bar_location(channel), self._window_height-(output + self._label_pixel_height), self._motor_gauge_pixel_width, output)

    def compute_channel_bar_location(self, channel):
        barPosition = (self.ui.transmitterOutput.width() - (self._motor_gauge_pixel_width * self._channel_count)) / (self._channel_count + 1)
        location = ((channel + 1) * barPosition) + (channel * self._motor_gauge_pixel_width)
        return location

    def resizeEvent(self, event):
        self._window_height = self.ui.transmitterOutput.height()
        self.windowWidth = self.ui.transmitterOutput.width()
        self.ui.transmitterOutput.setSceneRect(0, 0, self.windowWidth*2, self._window_height*2)
        self.ui.transmitterOutput.centerOn(0,0)
        for channel in range(self._channel_count-4):
            self._update_receiver_bar_widget(channel, 1000)
            self._channels_label_array_object[channel].setPos(self.compute_channel_bar_location(channel) - 3, self.ui.transmitterOutput.height() - self._label_pixel_height)

