
from ui.subpanel.BasePanelController import BasePanelController

from PyQt4 import QtGui
from ui.subpanel.pidparametersupdater.pidtuningpanel.PIDTuningPanel import Ui_PIDTuningPanel
from ui.subpanel.pidparametersupdater.pidwidget.PIDWidgetController import PIDWidgetController
from ui.UIEventDispatcher import UIEventDispatcher
from ui.subpanel.pidparametersupdater.configsinglelinewidget.ConfigSingleLineWidgetController import ConfigSingleLineWidgetController
from model.VehicleEventDispatcher import VehicleEventDispatcher
from ui.subpanel.pidparametersupdater.configsinglelinewidget.ConfigSingleLinePanelController import ConfigSingleLinePanelController




class AccroPIDTuningController(QtGui.QWidget, BasePanelController):
    
    def __init__(self, vehicle_event_dispatcher, ui_event_dispatcher):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        
        self.ui = Ui_PIDTuningPanel()
        self.ui.setupUi(self)
        
        
        self._gyro_roll_pid_controller = PIDWidgetController()
        self.ui.main_layout.addWidget(self._gyro_roll_pid_controller)
        
        self._gyro_pitch_pid_controller = PIDWidgetController()
        self.ui.main_layout.addWidget(self._gyro_pitch_pid_controller)
        self._gyro_pitch_pid_controller.set_p_bounds(50,200)
        self._gyro_pitch_pid_controller.set_title('PID tuning')
        self._gyro_pitch_pid_controller.p_line.ui.title_label.setText('Pitch Gain')
        self._gyro_pitch_pid_controller.p_line.ui.default_label.setText('100')
        self._gyro_pitch_pid_controller.i_line.ui.title_label.setText('Pitch Error Correction')
        self._gyro_pitch_pid_controller.i_line.ui.default_label.setText('150')
        self._gyro_pitch_pid_controller.d_line.ui.title_label.setText('Pitch Set Point')
        self._gyro_pitch_pid_controller.d_line.ui.default_label.setText('-350')
        self._gyro_pitch_pid_controller.set_p_different()
        self._gyro_pitch_pid_controller.set_i_different()
        self._gyro_pitch_pid_controller.set_d_different()
        
        self._gyro_roll_pid_controller.set_title('PID tuning')
        self._gyro_roll_pid_controller.p_line.ui.title_label.setText('Gain')
        self._gyro_roll_pid_controller.p_line.ui.default_label.setText('100')
        self._gyro_roll_pid_controller.i_line.ui.title_label.setText('Error Correction')
        self._gyro_roll_pid_controller.i_line.ui.default_label.setText('150')
        self._gyro_roll_pid_controller.d_line.ui.title_label.setText('Set Point')
        self._gyro_roll_pid_controller.d_line.ui.default_label.setText('-300')
        self._gyro_roll_pid_controller.set_p_different()
        self._gyro_roll_pid_controller.set_i_different()
        self._gyro_roll_pid_controller.set_d_different()
        
        self._stick_scaling_controller = ConfigSingleLinePanelController()
        self._stick_scaling_controller.ui.title_label.setText('Stick Scaling')
        self._stick_scaling_controller.set_different()
        self.ui.main_layout.addWidget(self._stick_scaling_controller)
        
        self.setBeginnerMode()
        
        ui_event_dispatcher.register(self._protocol_handler_changed_event, UIEventDispatcher.PROTOCOL_HANDLER_EVENT)
        vehicle_event_dispatcher.register(self._accro_roll_pid_received, VehicleEventDispatcher.PID_ACCRO_ROLL)
        vehicle_event_dispatcher.register(self._accro_pitch_pid_received, VehicleEventDispatcher.PID_ACCRO_PITCH)
        vehicle_event_dispatcher.register(self._accro_stick_scaling_received, VehicleEventDispatcher.PID_ACCRO_STICK_SCALING)

    def _protocol_handler_changed_event(self, event, protocol_handler):
        self._protocol_handler = protocol_handler;
        
    def setBeginnerMode(self):
        self._gyro_pitch_pid_controller.hide()
        self._gyro_roll_pid_controller.hide_i_line()
        self._gyro_roll_pid_controller.set_edit_box_enabled(False)
        
    def setIntermediateMode(self):
        self._gyro_roll_pid_controller.hide_i_line()
        self._gyro_pitch_pid_controller.hide_i_line()
        self._gyro_pitch_pid_controller.show()
        self._gyro_roll_pid_controller.set_edit_box_enabled(False)
    
    def setAdvancedMode(self):
        self._gyro_roll_pid_controller.show_i_line()
        self._gyro_pitch_pid_controller.show_i_line()
        self._gyro_roll_pid_controller.set_edit_box_enabled(True)
        
    def _accro_roll_pid_received(self, event, roll_pid):
        self._gyro_roll_pid_controller.set_current_p_value(roll_pid.get_p())
        self._gyro_roll_pid_controller.set_current_i_value(roll_pid.get_i())
        self._gyro_roll_pid_controller.set_current_d_value(roll_pid.get_d())
        
    def _accro_pitch_pid_received(self, event, pitch_pid):
        self._gyro_roll_pid_controller.set_current_p_value(pitch_pid.get_p())
        self._gyro_roll_pid_controller.set_current_i_value(pitch_pid.get_i())
        self._gyro_roll_pid_controller.set_current_d_value(pitch_pid.get_d())
        
    def _accro_stick_scaling_received(self, event, stick_scaling):
        self._stick_scaling_controller.set_value(stick_scaling)
        
    def start(self):
        self._protocol_handler.get_accro_pid();

