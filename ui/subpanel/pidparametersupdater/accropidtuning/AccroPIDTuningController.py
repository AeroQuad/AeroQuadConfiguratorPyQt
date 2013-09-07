
from ui.subpanel.BasePanelController import BasePanelController

from PyQt4 import QtGui
from ui.subpanel.pidparametersupdater.pidtuningpanel.PIDTuningPanel import Ui_PIDTuningPanel
from ui.subpanel.pidparametersupdater.pidwidget.PIDWidgetController import PIDWidgetController
from ui.UIEventDispatcher import UIEventDispatcher
from ui.subpanel.pidparametersupdater.configsinglelinewidget.ConfigSingleLineWidgetController import ConfigSingleLineWidgetController
from model.VehicleEventDispatcher import VehicleEventDispatcher
from ui.subpanel.pidparametersupdater.configsinglelinewidget.ConfigSingleLinePanelController import ConfigSingleLinePanelController
from model.PIDData import PIDData
from ui.subpanel.pidparametersupdater.PIDUpdateMode import PIDUpdateMode




class AccroPIDTuningController(QtGui.QWidget, BasePanelController):
    
    def __init__(self, vehicle_event_dispatcher, ui_event_dispatcher):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        
        self.ui = Ui_PIDTuningPanel()
        self.ui.setupUi(self)

        self._default_roll_pid = PIDData(100,150,-300)
        self._default_pitch_pid = PIDData(100,150,-300)
        self._default_stick_scaling = 1
        self._current_roll_pid = PIDData(100,150,-300)
        self._current_pitch_pid = PIDData(100,150,-300)
        self._current_stick_scaling = 1
        
        self._is_starting = False
        self._sync_in_progress = False
        
        self._user_update_mode = PIDUpdateMode.BEGINNER_MODE
                
        self._roll_pid_controller = PIDWidgetController()
        self.ui.main_layout.addWidget(self._roll_pid_controller)
        self._roll_pid_controller.set_title('PID tuning')
        self._roll_pid_controller.set_default(self._default_roll_pid)
        self._roll_pid_controller.set_p_bounds(50,200)
        self._roll_pid_controller.set_p_title('Pitch Gain')
        self._roll_pid_controller.set_i_bounds(100,150)
        self._roll_pid_controller.set_i_title('Error correction')
        self._roll_pid_controller.set_d_bounds(-1000,-100)
        self._roll_pid_controller.set_d_title('Set Point')
        self._roll_pid_controller.set_change_listener(self.user_pid_change)
        
        self._pitch_pid_controller = PIDWidgetController()
        self.ui.main_layout.addWidget(self._pitch_pid_controller)
        self._pitch_pid_controller.set_title('PID tuning')
        self._pitch_pid_controller.set_default(self._default_pitch_pid)
        self._pitch_pid_controller.set_p_bounds(50,200)
        self._pitch_pid_controller.set_p_title('Pitch Gain')
        self._pitch_pid_controller.set_i_bounds(100,150)
        self._pitch_pid_controller.set_i_title('Error correction')
        self._pitch_pid_controller.set_d_bounds(-1000,-100)
        self._pitch_pid_controller.set_d_title('Set Point')
        self._pitch_pid_controller.set_change_listener(self.user_pid_change)
        
        self._stick_scaling_controller = ConfigSingleLinePanelController()
        self._stick_scaling_controller.set_title('Stick Scaling')
        self._stick_scaling_controller.set_line_description('Stick Scaling')
        self._stick_scaling_controller.set_bounds(1,10)
        self._stick_scaling_controller.set_default('1')
        self.ui.main_layout.addWidget(self._stick_scaling_controller)
        
        self.setBeginnerMode()
        
        ui_event_dispatcher.register(self._protocol_handler_changed_event, UIEventDispatcher.PROTOCOL_HANDLER_EVENT)
        vehicle_event_dispatcher.register(self._accro_roll_pid_received, VehicleEventDispatcher.PID_ACCRO_ROLL)
        vehicle_event_dispatcher.register(self._accro_pitch_pid_received, VehicleEventDispatcher.PID_ACCRO_PITCH)
        vehicle_event_dispatcher.register(self._accro_stick_scaling_received, VehicleEventDispatcher.PID_ACCRO_STICK_SCALING)

    def _protocol_handler_changed_event(self, event, protocol_handler):
        self._protocol_handler = protocol_handler;
        
    def setBeginnerMode(self):
        self._user_update_mode = PIDUpdateMode.BEGINNER_MODE
        self._pitch_pid_controller.hide()
        self._roll_pid_controller.hide_i_line()
        self._roll_pid_controller.set_edit_box_enabled(False)
        
    def setIntermediateMode(self):
        self._user_update_mode = PIDUpdateMode.INTERMEDIATE_MODE
        self._roll_pid_controller.hide_i_line()
        self._pitch_pid_controller.hide_i_line()
        self._pitch_pid_controller.show()
        self._roll_pid_controller.set_edit_box_enabled(False)
    
    def setAdvancedMode(self):
        self._user_update_mode = PIDUpdateMode.ADVANCED_MODE
        self._roll_pid_controller.show_i_line()
        self._pitch_pid_controller.show_i_line()
        self._roll_pid_controller.set_edit_box_enabled(True)
        
    def _accro_roll_pid_received(self, event, roll_pid):
        self._current_roll_pid = roll_pid
        if self._is_starting :
            self._roll_pid_controller.set_current_pid(roll_pid)
        
    def _accro_pitch_pid_received(self, event, pitch_pid):
        self._current_pitch_pid = pitch_pid
        if self._is_starting :
            self._pitch_pid_controller.set_current_pid(pitch_pid)
        
    def _accro_stick_scaling_received(self, event, stick_scaling):
        self._current_stick_scaling = stick_scaling
        if self._is_starting :
            self._stick_scaling_controller.set_value(stick_scaling)
            self._is_starting = False
        self._process_sync_completed()
        
    def _process_sync_completed(self):
        self._sync_in_progress = False
        if self.is_synched() :
            self._set_synched()
        
    def start(self):
        self._is_starting = True
        self._sync_in_progress = True
        self._protocol_handler.get_accro_pid();
    
    def user_pid_change(self):
        if not self.is_synched() and not self._sync_in_progress : 
            self._send_pid_to_board()
            
    def is_synched(self):
        if not self._current_pitch_pid.is_equals(self._pitch_pid_controller.get_current_pid()) :
            return False
        elif not self._current_pitch_pid.is_equals(self._pitch_pid_controller.get_current_pid()) :
            return False
        elif not self._current_stick_scaling != self._stick_scaling_controller.get_value() :
            return False
        return True
    
    def _set_synched(self):
        self._roll_pid_controller.p_line.set_same()
        self._roll_pid_controller.i_line.set_same()
        self._roll_pid_controller.d_line.set_same()
        self._pitch_pid_controller.p_line.set_same()
        self._pitch_pid_controller.i_line.set_same()
        self._pitch_pid_controller.d_line.set_same()
        self._stick_scaling_controller._line.set_same()
        
    def _send_pid_to_board(self):
        pass
#         send PID to board depending of the current use update mode
         
            
        

