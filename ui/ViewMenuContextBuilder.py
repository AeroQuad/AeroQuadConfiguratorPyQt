
from PyQt4 import QtCore, QtGui
from model.VehicleEventDispatcher import VehicleEventDispatcher
from ui.UIEventDispatcher import UIEventDispatcher
from ui.PanelsContextBuilder import PanelsContextBuilder

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
    


class ViewMenuContextBuilder(object):

    def __init__(self, view_menu, ui_event_dispatcher, vehicle_event_dispatcher):
       
        self._ui_event_dispatcher = ui_event_dispatcher
        self._arrow_icon = QtGui.QIcon()
        self._arrow_icon.addPixmap(QtGui.QPixmap(_fromUtf8("resources/arrow_right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)        

        info_icon = QtGui.QIcon()
        info_icon.addPixmap(QtGui.QPixmap(_fromUtf8("resources/info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_menu_item = self._create_menu_item(view_menu, "info_menu", "Info", info_icon)
        self.vehicle_info_menu_action = self._create_menu_action(self.info_menu_item, "vehicle_info_menu", "Vehicle Info", self._arrow_icon)
        self.vehicle_info_menu_action.triggered.connect(self._vehicle_info_button_clicked)
        self.vehicle_status_menu_action = self._create_menu_action(self.info_menu_item, "vehicle_status_menu", "Vehicle Status", self._arrow_icon)
        self.vehicle_status_menu_action.triggered.connect(self._vehicle_status_button_clicked)

        setting_icon = QtGui.QIcon()
        setting_icon.addPixmap(QtGui.QPixmap(_fromUtf8("resources/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_menu_item = self._create_menu_item(view_menu, "setting_menu", "Setting", setting_icon)
        self.accel_calibration_menu_action = self._create_menu_action(self.setting_menu_item, "accel_calibration_menu", "Accelerometer Calibration", self._arrow_icon)
        self.accel_calibration_menu_action.triggered.connect(self._accel_calibration_button_clicked)
        self.receiver_calibration_menu_action = self._create_menu_action(self.setting_menu_item, "receiver_calibration_menu", "Receiver Calibration", self._arrow_icon)
        self.receiver_calibration_menu_action.triggered.connect(self._receiver_calibration_button_clicked)
        self.pid_calibration_menu_action = self._create_menu_action(self.setting_menu_item, "pid_calibration_menu", "PID's Calibration", self._arrow_icon)
        self.pid_calibration_menu_action.triggered.connect(self._pid_tuning_button_clicked)
        self.motor_command_menu_action = self._create_menu_action(self.setting_menu_item, "motor_command_menu", "Motors Command", self._arrow_icon)
        self.motor_command_menu_action.triggered.connect(self._motor_command_button_clicked)

        
        plotting_icon = QtGui.QIcon()
        plotting_icon.addPixmap(QtGui.QPixmap(_fromUtf8("resources/graphic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.data_plot_menu_item = self._create_menu_item(view_menu, "data_plot_menu", "Data Plot", plotting_icon)
        self.sensors_plotting_menu_action = self._create_menu_action(self.data_plot_menu_item, "sensors_plotting_menu", "Sensors plotting", self._arrow_icon)
        self.sensors_plotting_menu_action.triggered.connect(self._sensor_plot_button_clicked)
        self.receiver_plotting_menu_action = self._create_menu_action(self.data_plot_menu_item, "receiver_plotting_menu", "Receiver plotting", self._arrow_icon)
        self.receiver_plotting_menu_action.triggered.connect(self._receiver_plot_button_clicked)
        
        vehicle_event_dispatcher.register(self._is_magnetometer_detected_event, VehicleEventDispatcher.MAGNETOMETER_DETECTED_EVENT)
        
    def _create_menu_item(self, parent, menu_object_name, menu_text_name, icon):
        menu_item = QtGui.QMenu(parent)
        menu_item.setObjectName(_fromUtf8(menu_object_name))
        menu_item.setTitle(_translate("MainWindow", menu_text_name, None))
        menu_item.setIcon(icon)
        parent.addAction(menu_item.menuAction())
        return menu_item
    
    def _create_menu_action(self, parent, menu_object_name, menu_text_name, icon):
        menu_action = QtGui.QAction(parent)
        menu_action.setObjectName(_fromUtf8(menu_object_name))
        menu_action.setText(_translate("MainWindow", menu_text_name, None))
        menu_action.setIcon(icon)
        parent.addAction(menu_action)
        return menu_action
    
    def _is_magnetometer_detected_event(self, header, is_detected):
        if is_detected == 'Detected':
            self.magnetometer_calibration_menu_action = self._create_menu_action(self.setting_menu_item, "magnetometer_calibration_menu", "Magnetometer Calibration", self._arrow_icon)
            self.magnetometer_calibration_menu_action.triggered.connect(self._magnetometer_calibration_button_clicked)
            
    # @todo kenny, clean those message, should belong somewhere else thatn into the PanelsContextBuilder            
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

    