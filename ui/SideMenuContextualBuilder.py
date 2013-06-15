
from PyQt4 import QtCore, QtGui
from ui.UIEventDispatcher import UIEventDispatcher
from ui.PanelsContextBuilder import PanelsContextBuilder
from model.VehicleEventDispatcher import VehicleEventDispatcher

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
    
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
    

class SideMenuContextualBuilder(object):

    def __init__(self, ui_event_dispatcher,
                       vehicle_event_dispatcher,
                       side_menu_info_page, 
                       side_menu_setting_page, 
                       side_menu_troubleshooting_page, 
                       side_menu_mission_planer_page):
        
        
        self._ui_event_dispatcher = ui_event_dispatcher

        
        self._side_menu_info_page = side_menu_info_page
        self._side_menu_setting_page = side_menu_setting_page
        self._side_menu_troubleshooting_page = side_menu_troubleshooting_page
        self._side_menu_mission_planer_page = side_menu_mission_planer_page
        
        self._vehicle_status_button = None
        
        vehicle_event_dispatcher.register(self._is_magnetometer_detected_event, VehicleEventDispatcher.MAGNETOMETER_DETECTED_EVENT)
        self._ui_event_dispatcher.register(self._connection_state_changed, UIEventDispatcher.CONNECTION_STATE_CHANGED_EVENT)
        
        
    def _connection_state_changed(self, event, is_connected):
        if is_connected :
            self._create_menu_info_page()
            self._create_settings_page()
            self._create_trouble_shooting_page()
        elif self._vehicle_status_button is not None:
            self._vehicle_status_button.setParent(None)
            self._vehicle_info_button.setParent(None)
            
            self._accel_calibration_button.setParent(None)
            self._receiver_calibration_button.setParent(None)
            self._pid_tuning_button.setParent(None)
            self._motor_command_button.setParent(None)
            
            self._sensor_plot_button.setParent(None)
            self._receiver_plot_button.setParent(None)
            
        self._side_menu_info_page.setEnabled(is_connected)
        self._side_menu_setting_page.setEnabled(is_connected)
        self._side_menu_troubleshooting_page.setEnabled(is_connected)
        
    def _is_magnetometer_detected_event(self, header, is_detected):
        if is_detected == 'Detected':
            self._pixel_button_height_counter = 80
            self._magnteomter_calibration_button = self._create_side_menu_button(self._side_menu_setting_page,
                                                                      "Magnetometer Calibation",
                                                                      self._pixel_button_height_counter)
            self._magnteomter_calibration_button.clicked.connect(self._magnetometer_calibration_button_clicked);
            self._magnteomter_calibration_button.show()
            
    def _create_menu_info_page(self):
        self._pixel_button_height_counter = 0;
        self._vehicle_info_button = self._create_side_menu_button(self._side_menu_info_page,
                                                                  "Vehicle info",
                                                                  self._pixel_button_height_counter)
        self._vehicle_info_button.clicked.connect(self._vehicle_info_button_clicked);
        self._vehicle_info_button.show()
        
        self._pixel_button_height_counter += 20 
        self._vehicle_status_button = self._create_side_menu_button(self._side_menu_info_page,
                                                                  "Vehicle status",
                                                                  self._pixel_button_height_counter)
        self._vehicle_status_button.clicked.connect(self._vehicle_status_button_clicked);
        self._vehicle_status_button.show()
        
    def _create_settings_page(self):
        self._pixel_button_height_counter = 0;
        self._accel_calibration_button = self._create_side_menu_button(self._side_menu_setting_page,
                                                                  "Accelerometer Calibration",
                                                                  self._pixel_button_height_counter)
        self._accel_calibration_button.clicked.connect(self._accel_calibration_button_clicked);
        self._accel_calibration_button.show()
        
        self._pixel_button_height_counter += 20
        self._receiver_calibration_button = self._create_side_menu_button(self._side_menu_setting_page,
                                                                  "Receiver Calibration",
                                                                  self._pixel_button_height_counter)
        self._receiver_calibration_button.clicked.connect(self._receiver_calibration_button_clicked);
        self._receiver_calibration_button.show()
        
        self._pixel_button_height_counter += 20
        self._pid_tuning_button = self._create_side_menu_button(self._side_menu_setting_page,
                                                                  "PID's Tuning",
                                                                  self._pixel_button_height_counter)
        self._pid_tuning_button.clicked.connect(self._pid_tuning_button_clicked);
        self._pid_tuning_button.show()
        
        self._pixel_button_height_counter += 20
        self._motor_command_button = self._create_side_menu_button(self._side_menu_setting_page,
                                                                  "Motor commands",
                                                                  self._pixel_button_height_counter)
        self._motor_command_button.clicked.connect(self._motor_command_button_clicked);
        self._motor_command_button.show()   
        
    def _create_trouble_shooting_page(self):
        self._pixel_button_height_counter = 0;
        self._sensor_plot_button = self._create_side_menu_button(self._side_menu_troubleshooting_page,
                                                                  "Sensors plotting",
                                                                  self._pixel_button_height_counter)
        self._sensor_plot_button.clicked.connect(self._sensor_plot_button_clicked);
        self._sensor_plot_button.show()
        
        self._pixel_button_height_counter += 20
        self._receiver_plot_button = self._create_side_menu_button(self._side_menu_troubleshooting_page,
                                                                  "Receiver plotting",
                                                                  self._pixel_button_height_counter)
        self._receiver_plot_button.clicked.connect(self._receiver_plot_button_clicked);
        self._receiver_plot_button.show()

    def _vehicle_info_button_clicked(self):
        self._ui_event_dispatcher.dispatch(UIEventDispatcher.DISPLAY_PANEL_EVENT,PanelsContextBuilder.VEHICLE_INFORMATION_PANEL_ID)

    def _vehicle_status_button_clicked(self):
        self._ui_event_dispatcher.dispatch(UIEventDispatcher.DISPLAY_PANEL_EVENT,PanelsContextBuilder.VEHICLE_STATUS_PANEL_ID)
        
    def _accel_calibration_button_clicked(self):
        self._ui_event_dispatcher.dispatch(UIEventDispatcher.DISPLAY_PANEL_EVENT,PanelsContextBuilder.ACCEL_CALIBRATION_PANEL_ID)        
            
    def _receiver_calibration_button_clicked(self):
        self._ui_event_dispatcher.dispatch(UIEventDispatcher.DISPLAY_PANEL_EVENT,PanelsContextBuilder.RECEIVER_CALIBRATION_PANEL_ID)
        
    def _pid_tuning_button_clicked(self):
        self._ui_event_dispatcher.dispatch(UIEventDispatcher.DISPLAY_PANEL_EVENT,PanelsContextBuilder.PID_TUNING_PANEL_ID)
        
    def _motor_command_button_clicked(self):
        self._ui_event_dispatcher.dispatch(UIEventDispatcher.DISPLAY_PANEL_EVENT,PanelsContextBuilder.MOTOR_COMMAND_PANEL_ID)
                
    def _sensor_plot_button_clicked(self):
        self._ui_event_dispatcher.dispatch(UIEventDispatcher.DISPLAY_PANEL_EVENT,PanelsContextBuilder.SENSOR_PLOT_PANEL_ID)

    def _receiver_plot_button_clicked(self):
        self._ui_event_dispatcher.dispatch(UIEventDispatcher.DISPLAY_PANEL_EVENT,PanelsContextBuilder.RECEIVER_PLOT_PANEL_ID)
                
    def _magnetometer_calibration_button_clicked(self):
        self._ui_event_dispatcher.dispatch(UIEventDispatcher.DISPLAY_PANEL_EVENT,PanelsContextBuilder.MAGNETOMETER_CALIBRATION_PANEL_ID)
        
    def _create_side_menu_button(self, page_owner, name, starting_pixel):
        button = QtGui.QPushButton(page_owner)
        button.setGeometry(QtCore.QRect(3, starting_pixel, 176, 23))
        button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        button.setFont(font)
        button.setLayoutDirection(QtCore.Qt.LeftToRight)
        button.setAutoFillBackground(False)
        button.setStyleSheet(_fromUtf8("text-align: left"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("resources/arrow_right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon1)
        button.setDefault(False)
        button.setFlat(True)
        button.setObjectName(_fromUtf8("_vehicle_info_button"))
        button.setText(_translate("MainWindow", name, None))
        return button
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#        
#        self.sidemenu_button_vehicle_configuration = QtGui.QPushButton(self._side_menu_info_page)
#        self.sidemenu_button_vehicle_configuration.setGeometry(QtCore.QRect(3, 20, 176, 23))
#        self.sidemenu_button_vehicle_configuration.setMinimumSize(QtCore.QSize(0, 0))
#        font = QtGui.QFont()
#        font.setPointSize(10)
#        font.setUnderline(False)
#        self.sidemenu_button_vehicle_configuration.setFont(font)
#        self.sidemenu_button_vehicle_configuration.setLayoutDirection(QtCore.Qt.LeftToRight)
#        self.sidemenu_button_vehicle_configuration.setAutoFillBackground(False)
#        self.sidemenu_button_vehicle_configuration.setStyleSheet(_fromUtf8("text-align: left"))
#        self.sidemenu_button_vehicle_configuration.setIcon(icon1)
#        self.sidemenu_button_vehicle_configuration.setDefault(False)
#        self.sidemenu_button_vehicle_configuration.setFlat(True)
#        self.sidemenu_button_vehicle_configuration.setObjectName(_fromUtf8("sidemenu_button_vehicle_configuration"))
#        self.sidemenu_button_vehicle_configuration.setText(_translate("MainWindow", "Vehicle Configuration", None))
        
#        
#        self.sidemenu_button_vehicle_setup = QtGui.QPushButton(setting_page)
#        self.sidemenu_button_vehicle_setup.setGeometry(QtCore.QRect(3, 0, 176, 23))
#        self.sidemenu_button_vehicle_setup.setMinimumSize(QtCore.QSize(0, 0))
#        font = QtGui.QFont()
#        font.setPointSize(10)
#        font.setUnderline(False)
#        self.sidemenu_button_vehicle_setup.setFont(font)
#        self.sidemenu_button_vehicle_setup.setLayoutDirection(QtCore.Qt.LeftToRight)
#        self.sidemenu_button_vehicle_setup.setAutoFillBackground(False)
#        self.sidemenu_button_vehicle_setup.setStyleSheet(_fromUtf8("text-align: left"))
#        self.sidemenu_button_vehicle_setup.setIcon(icon1)
#        self.sidemenu_button_vehicle_setup.setDefault(False)
#        self.sidemenu_button_vehicle_setup.setFlat(True)
#        self.sidemenu_button_vehicle_setup.setObjectName(_fromUtf8("sidemenu_button_vehicle_setup"))
#
#        self.sidemenu_button_sensors_calibration = QtGui.QPushButton(setting_page)
#        self.sidemenu_button_sensors_calibration.setGeometry(QtCore.QRect(3, 20, 176, 23))
#        self.sidemenu_button_sensors_calibration.setMinimumSize(QtCore.QSize(0, 0))
#        font = QtGui.QFont()
#        font.setPointSize(10)
#        font.setUnderline(False)
#        self.sidemenu_button_sensors_calibration.setFont(font)
#        self.sidemenu_button_sensors_calibration.setLayoutDirection(QtCore.Qt.LeftToRight)
#        self.sidemenu_button_sensors_calibration.setAutoFillBackground(False)
#        self.sidemenu_button_sensors_calibration.setStyleSheet(_fromUtf8("text-align: left"))
#        self.sidemenu_button_sensors_calibration.setIcon(icon1)
#        self.sidemenu_button_sensors_calibration.setDefault(False)
#        self.sidemenu_button_sensors_calibration.setFlat(True)
#        self.sidemenu_button_sensors_calibration.setObjectName(_fromUtf8("sidemenu_button_sensors_calibration"))
#        
#        self.sidemenu_button_magnetometer_calibration = QtGui.QPushButton(setting_page)
#        self.sidemenu_button_magnetometer_calibration.setGeometry(QtCore.QRect(3, 40, 176, 23))
#        self.sidemenu_button_magnetometer_calibration.setMinimumSize(QtCore.QSize(0, 0))
#        font = QtGui.QFont()
#        font.setPointSize(10)
#        font.setUnderline(False)
#        self.sidemenu_button_magnetometer_calibration.setFont(font)
#        self.sidemenu_button_magnetometer_calibration.setLayoutDirection(QtCore.Qt.LeftToRight)
#        self.sidemenu_button_magnetometer_calibration.setAutoFillBackground(False)
#        self.sidemenu_button_magnetometer_calibration.setStyleSheet(_fromUtf8("text-align: left"))
#        self.sidemenu_button_magnetometer_calibration.setIcon(icon1)
#        self.sidemenu_button_magnetometer_calibration.setDefault(False)
#        self.sidemenu_button_magnetometer_calibration.setFlat(True)
#        self.sidemenu_button_magnetometer_calibration.setObjectName(_fromUtf8("sidemenu_button_magnetometer_calibration"))
#        
#        self.sidemenu_button_RC_channels_detection = QtGui.QPushButton(setting_page)
#        self.sidemenu_button_RC_channels_detection.setGeometry(QtCore.QRect(3, 60, 176, 23))
#        self.sidemenu_button_RC_channels_detection.setMinimumSize(QtCore.QSize(0, 0))
#        font = QtGui.QFont()
#        font.setPointSize(10)
#        font.setUnderline(False)
#        self.sidemenu_button_RC_channels_detection.setFont(font)
#        self.sidemenu_button_RC_channels_detection.setLayoutDirection(QtCore.Qt.LeftToRight)
#        self.sidemenu_button_RC_channels_detection.setAutoFillBackground(False)
#        self.sidemenu_button_RC_channels_detection.setStyleSheet(_fromUtf8("text-align: left"))
#        self.sidemenu_button_RC_channels_detection.setIcon(icon1)
#        self.sidemenu_button_RC_channels_detection.setDefault(False)
#        self.sidemenu_button_RC_channels_detection.setFlat(True)
#        self.sidemenu_button_RC_channels_detection.setObjectName(_fromUtf8("sidemenu_button_RC_channels_detection"))
#        
#        self.sidemenu_button_RC_calibartion = QtGui.QPushButton(setting_page)
#        self.sidemenu_button_RC_calibartion.setGeometry(QtCore.QRect(3, 80, 176, 23))
#        self.sidemenu_button_RC_calibartion.setMinimumSize(QtCore.QSize(0, 0))
#        font = QtGui.QFont()
#        font.setPointSize(10)
#        font.setUnderline(False)
#        self.sidemenu_button_RC_calibartion.setFont(font)
#        self.sidemenu_button_RC_calibartion.setLayoutDirection(QtCore.Qt.LeftToRight)
#        self.sidemenu_button_RC_calibartion.setAutoFillBackground(False)
#        self.sidemenu_button_RC_calibartion.setStyleSheet(_fromUtf8("text-align: left"))
#        self.sidemenu_button_RC_calibartion.setIcon(icon1)
#        self.sidemenu_button_RC_calibartion.setDefault(False)
#        self.sidemenu_button_RC_calibartion.setFlat(True)
#        self.sidemenu_button_RC_calibartion.setObjectName(_fromUtf8("sidemenu_button_RC_calibartion"))
#        
#        self.sidemenu_button_motor_command = QtGui.QPushButton(setting_page)
#        self.sidemenu_button_motor_command.setGeometry(QtCore.QRect(3, 100, 176, 23))
#        self.sidemenu_button_motor_command.setMinimumSize(QtCore.QSize(0, 0))
#        font = QtGui.QFont()
#        font.setPointSize(10)
#        font.setUnderline(False)
#        self.sidemenu_button_motor_command.setFont(font)
#        self.sidemenu_button_motor_command.setLayoutDirection(QtCore.Qt.LeftToRight)
#        self.sidemenu_button_motor_command.setAutoFillBackground(False)
#        self.sidemenu_button_motor_command.setStyleSheet(_fromUtf8("text-align: left"))
#        self.sidemenu_button_motor_command.setIcon(icon1)
#        self.sidemenu_button_motor_command.setDefault(False)
#        self.sidemenu_button_motor_command.setFlat(True)
#        self.sidemenu_button_motor_command.setObjectName(_fromUtf8("sidemenu_button_motor_command"))
#        
#        self.sidemenu_button_PID_update = QtGui.QPushButton(setting_page)
#        self.sidemenu_button_PID_update.setGeometry(QtCore.QRect(3, 120, 176, 23))
#        self.sidemenu_button_PID_update.setMinimumSize(QtCore.QSize(0, 0))
#        font = QtGui.QFont()
#        font.setPointSize(10)
#        font.setUnderline(False)
#        self.sidemenu_button_PID_update.setFont(font)
#        self.sidemenu_button_PID_update.setLayoutDirection(QtCore.Qt.LeftToRight)
#        self.sidemenu_button_PID_update.setAutoFillBackground(False)
#        self.sidemenu_button_PID_update.setStyleSheet(_fromUtf8("text-align: left"))
#        self.sidemenu_button_PID_update.setIcon(icon1)
#        self.sidemenu_button_PID_update.setDefault(False)
#        self.sidemenu_button_PID_update.setFlat(True)
#        self.sidemenu_button_PID_update.setObjectName(_fromUtf8("sidemenu_button_PID_update"))
#        
#        self.sidemenu_button_serial_monitor = QtGui.QPushButton(troubleshooting_page)
#        self.sidemenu_button_serial_monitor.setGeometry(QtCore.QRect(3, 0, 176, 23))
#        self.sidemenu_button_serial_monitor.setMinimumSize(QtCore.QSize(0, 0))
#        font = QtGui.QFont()
#        font.setPointSize(10)
#        font.setUnderline(False)
#        self.sidemenu_button_serial_monitor.setFont(font)
#        self.sidemenu_button_serial_monitor.setLayoutDirection(QtCore.Qt.LeftToRight)
#        self.sidemenu_button_serial_monitor.setAutoFillBackground(False)
#        self.sidemenu_button_serial_monitor.setStyleSheet(_fromUtf8("text-align: left"))
#        self.sidemenu_button_serial_monitor.setIcon(icon1)
#        self.sidemenu_button_serial_monitor.setDefault(False)
#        self.sidemenu_button_serial_monitor.setFlat(True)
#        self.sidemenu_button_serial_monitor.setObjectName(_fromUtf8("sidemenu_button_serial_monitor"))
#        
#        self.sidemenu_button_sensor_data = QtGui.QPushButton(troubleshooting_page)
#        self.sidemenu_button_sensor_data.setGeometry(QtCore.QRect(3, 20, 176, 23))
#        self.sidemenu_button_sensor_data.setMinimumSize(QtCore.QSize(0, 0))
#        font = QtGui.QFont()
#        font.setPointSize(10)
#        font.setUnderline(False)
#        self.sidemenu_button_sensor_data.setFont(font)
#        self.sidemenu_button_sensor_data.setLayoutDirection(QtCore.Qt.LeftToRight)
#        self.sidemenu_button_sensor_data.setAutoFillBackground(False)
#        self.sidemenu_button_sensor_data.setStyleSheet(_fromUtf8("text-align: left"))
#        self.sidemenu_button_sensor_data.setIcon(icon1)
#        self.sidemenu_button_sensor_data.setDefault(False)
#        self.sidemenu_button_sensor_data.setFlat(True)
#        self.sidemenu_button_sensor_data.setObjectName(_fromUtf8("sidemenu_button_sensor_data"))
#        
#        self.sidemenu_button_gyroscope_data = QtGui.QPushButton(troubleshooting_page)
#        self.sidemenu_button_gyroscope_data.setGeometry(QtCore.QRect(3, 40, 176, 23))
#        self.sidemenu_button_gyroscope_data.setMinimumSize(QtCore.QSize(0, 0))
#        font = QtGui.QFont()
#        font.setPointSize(10)
#        font.setUnderline(False)
#        self.sidemenu_button_gyroscope_data.setFont(font)
#        self.sidemenu_button_gyroscope_data.setLayoutDirection(QtCore.Qt.LeftToRight)
#        self.sidemenu_button_gyroscope_data.setAutoFillBackground(False)
#        self.sidemenu_button_gyroscope_data.setStyleSheet(_fromUtf8("text-align: left"))
#        self.sidemenu_button_gyroscope_data.setIcon(icon1)
#        self.sidemenu_button_gyroscope_data.setDefault(False)
#        self.sidemenu_button_gyroscope_data.setFlat(True)
#        self.sidemenu_button_gyroscope_data.setObjectName(_fromUtf8("sidemenu_button_gyroscope_data"))
#        
#        self.sidemenu_button_accelerometer_data = QtGui.QPushButton(troubleshooting_page)
#        self.sidemenu_button_accelerometer_data.setGeometry(QtCore.QRect(3, 60, 176, 23))
#        self.sidemenu_button_accelerometer_data.setMinimumSize(QtCore.QSize(0, 0))
#        font = QtGui.QFont()
#        font.setPointSize(10)
#        font.setUnderline(False)
#        self.sidemenu_button_accelerometer_data.setFont(font)
#        self.sidemenu_button_accelerometer_data.setLayoutDirection(QtCore.Qt.LeftToRight)
#        self.sidemenu_button_accelerometer_data.setAutoFillBackground(False)
#        self.sidemenu_button_accelerometer_data.setStyleSheet(_fromUtf8("text-align: left"))
#        self.sidemenu_button_accelerometer_data.setIcon(icon1)
#        self.sidemenu_button_accelerometer_data.setDefault(False)
#        self.sidemenu_button_accelerometer_data.setFlat(True)
#        self.sidemenu_button_accelerometer_data.setObjectName(_fromUtf8("sidemenu_button_accelerometer_data"))
#        
#        self.sidemenu_button_magnetometer_data = QtGui.QPushButton(troubleshooting_page)
#        self.sidemenu_button_magnetometer_data.setGeometry(QtCore.QRect(3, 80, 176, 23))
#        self.sidemenu_button_magnetometer_data.setMinimumSize(QtCore.QSize(0, 0))
#        font = QtGui.QFont()
#        font.setPointSize(10)
#        font.setUnderline(False)
#        self.sidemenu_button_magnetometer_data.setFont(font)
#        self.sidemenu_button_magnetometer_data.setLayoutDirection(QtCore.Qt.LeftToRight)
#        self.sidemenu_button_magnetometer_data.setAutoFillBackground(False)
#        self.sidemenu_button_magnetometer_data.setStyleSheet(_fromUtf8("text-align: left"))
#        self.sidemenu_button_magnetometer_data.setIcon(icon1)
#        self.sidemenu_button_magnetometer_data.setDefault(False)
#        self.sidemenu_button_magnetometer_data.setFlat(True)
#        self.sidemenu_button_magnetometer_data.setObjectName(_fromUtf8("sidemenu_button_magnetometer_data"))
#        
#        self.sidemenu_button_attitude_data = QtGui.QPushButton(troubleshooting_page)
#        self.sidemenu_button_attitude_data.setGeometry(QtCore.QRect(3, 100, 176, 23))
#        self.sidemenu_button_attitude_data.setMinimumSize(QtCore.QSize(0, 0))
#        font = QtGui.QFont()
#        font.setPointSize(10)
#        font.setUnderline(False)
#        self.sidemenu_button_attitude_data.setFont(font)
#        self.sidemenu_button_attitude_data.setLayoutDirection(QtCore.Qt.LeftToRight)
#        self.sidemenu_button_attitude_data.setAutoFillBackground(False)
#        self.sidemenu_button_attitude_data.setStyleSheet(_fromUtf8("text-align: left"))
#        self.sidemenu_button_attitude_data.setIcon(icon1)
#        self.sidemenu_button_attitude_data.setDefault(False)
#        self.sidemenu_button_attitude_data.setFlat(True)
#        self.sidemenu_button_attitude_data.setObjectName(_fromUtf8("sidemenu_button_attitude_data"))
#        
#        self.sidemenu_button_transmitter_data = QtGui.QPushButton(troubleshooting_page)
#        self.sidemenu_button_transmitter_data.setGeometry(QtCore.QRect(3, 120, 176, 23))
#        self.sidemenu_button_transmitter_data.setMinimumSize(QtCore.QSize(0, 0))
#        font = QtGui.QFont()
#        font.setPointSize(10)
#        font.setUnderline(False)
#        self.sidemenu_button_transmitter_data.setFont(font)
#        self.sidemenu_button_transmitter_data.setLayoutDirection(QtCore.Qt.LeftToRight)
#        self.sidemenu_button_transmitter_data.setAutoFillBackground(False)
#        self.sidemenu_button_transmitter_data.setStyleSheet(_fromUtf8("text-align: left"))
#        self.sidemenu_button_transmitter_data.setIcon(icon1)
#        self.sidemenu_button_transmitter_data.setDefault(False)
#        self.sidemenu_button_transmitter_data.setFlat(True)
#        self.sidemenu_button_transmitter_data.setObjectName(_fromUtf8("sidemenu_button_transmitter_data"))
#        
#        self.sidemenu_button_altitude_data = QtGui.QPushButton(troubleshooting_page)
#        self.sidemenu_button_altitude_data.setGeometry(QtCore.QRect(3, 140, 176, 23))
#        self.sidemenu_button_altitude_data.setMinimumSize(QtCore.QSize(0, 0))
#        font = QtGui.QFont()
#        font.setPointSize(10)
#        font.setUnderline(False)
#        self.sidemenu_button_altitude_data.setFont(font)
#        self.sidemenu_button_altitude_data.setLayoutDirection(QtCore.Qt.LeftToRight)
#        self.sidemenu_button_altitude_data.setAutoFillBackground(False)
#        self.sidemenu_button_altitude_data.setStyleSheet(_fromUtf8("text-align: left"))
#        self.sidemenu_button_altitude_data.setIcon(icon1)
#        self.sidemenu_button_altitude_data.setDefault(False)
#        self.sidemenu_button_altitude_data.setFlat(True)
#        self.sidemenu_button_altitude_data.setObjectName(_fromUtf8("sidemenu_button_altitude_data"))

        