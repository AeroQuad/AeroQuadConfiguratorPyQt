
from ui.subpanel.BasePanelController import BasePanelController

from PyQt4 import QtGui
from ui.subpanel.pidparametersupdater.pidtuningpanel.PIDTuningPanel import Ui_PIDTuningPanel
from ui.subpanel.pidparametersupdater.pidwidget.PIDWidgetController import PIDWidgetController
from ui.UIEventDispatcher import UIEventDispatcher
from model.VehicleEventDispatcher import VehicleEventDispatcher
from ui.subpanel.pidparametersupdater.configsinglelinewidget.ConfigSingleLinePanelController import ConfigSingleLinePanelController
from model.PIDData import PIDData
from ui.subpanel.pidparametersupdater.PIDUpdateMode import PIDUpdateMode
from utilities.math.MathUtils import MathUtil



class AccroPIDTuningController(QtGui.QWidget, BasePanelController):
    
    def __init__(self, vehicle_event_dispatcher, ui_event_dispatcher):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        
        self.ui = Ui_PIDTuningPanel()
        self.ui.setupUi(self)

        self._current_roll_pid = PIDData(100,150,-300)
        self._current_pitch_pid = PIDData(100,150,-300)
        self._current_stick_scaling = 1
        
        self._is_starting = False
        
        self._user_update_mode = PIDUpdateMode.BEGINNER_MODE
                
        self._roll_pid_controller = PIDWidgetController()
        self.ui.main_layout.addWidget(self._roll_pid_controller)
        self._roll_pid_controller.set_title('PID tuning')
        self._roll_pid_controller.set_default(PIDData(100,150,-350))
        self._roll_pid_controller.set_p_bounds(50,200)
        self._roll_pid_controller.set_p_title('Pitch Gain')
        self._roll_pid_controller.set_i_bounds(100,300)
        self._roll_pid_controller.set_i_title('Error correction')
        self._roll_pid_controller.set_d_bounds(-1000,-100)
        self._roll_pid_controller.set_d_title('Set Point')
        
        self._pitch_pid_controller = PIDWidgetController()
        self.ui.main_layout.addWidget(self._pitch_pid_controller)
        self._pitch_pid_controller.set_title('PID tuning')
        self._pitch_pid_controller.set_default(PIDData(100,150,-350))
        self._pitch_pid_controller.set_p_bounds(50,200)
        self._pitch_pid_controller.set_p_title('Pitch Gain')
        self._pitch_pid_controller.set_i_bounds(100,300)
        self._pitch_pid_controller.set_i_title('Error correction')
        self._pitch_pid_controller.set_d_bounds(-1000,-100)
        self._pitch_pid_controller.set_d_title('Set Point')
        
        self._stick_scaling_controller = ConfigSingleLinePanelController()
        self._stick_scaling_controller.set_title('Stick Scaling')
        self._stick_scaling_controller.set_line_description('Stick Scaling')
        self._stick_scaling_controller.set_bounds(1,6)
        self._stick_scaling_controller.set_default('1')
        self.ui.main_layout.addWidget(self._stick_scaling_controller)
        
        ui_event_dispatcher.register(self._protocol_handler_changed_event, UIEventDispatcher.PROTOCOL_HANDLER_EVENT)
        vehicle_event_dispatcher.register(self._roll_pid_received, VehicleEventDispatcher.PID_ACCRO_ROLL)
        vehicle_event_dispatcher.register(self._pitch_pid_received, VehicleEventDispatcher.PID_ACCRO_PITCH)
        vehicle_event_dispatcher.register(self._accro_stick_scaling_received, VehicleEventDispatcher.PID_ACCRO_STICK_SCALING)
        
        self._cpt_before_send = 5
        self.set_beginner_mode()

    def _protocol_handler_changed_event(self, event, protocol_handler):
        self._protocol_handler = protocol_handler;
        
    def set_beginner_mode(self):
        self._user_update_mode = PIDUpdateMode.BEGINNER_MODE
        self._pitch_pid_controller.hide()
        self._roll_pid_controller.hide_i_line()
        self._roll_pid_controller.set_edit_box_enabled(False)
        self._stick_scaling_controller.set_edit_box_enabled(False)
        
    def set_intermediate_mode(self):
        self._user_update_mode = PIDUpdateMode.INTERMEDIATE_MODE
        self._pitch_pid_controller.show()
        self._roll_pid_controller.hide_i_line()
        self._pitch_pid_controller.hide_i_line()
        self._pitch_pid_controller.show()
        self._roll_pid_controller.set_edit_box_enabled(False)
        self._pitch_pid_controller.set_edit_box_enabled(False)
        self._stick_scaling_controller.set_edit_box_enabled(False)
    
    def set_advanced_mode(self):
        self._user_update_mode = PIDUpdateMode.ADVANCED_MODE
        self._pitch_pid_controller.show()
        self._roll_pid_controller.show_i_line()
        self._pitch_pid_controller.show_i_line()
        self._roll_pid_controller.set_edit_box_enabled(True)
        self._pitch_pid_controller.set_edit_box_enabled(True)
        self._stick_scaling_controller.set_edit_box_enabled(True)
        
    def _roll_pid_received(self, event, roll_pid):
        self._current_roll_pid = roll_pid
        if self._is_starting :
            self._roll_pid_controller.set_current_pid(roll_pid)
        
    def _pitch_pid_received(self, event, pitch_pid):
        self._current_pitch_pid = pitch_pid
        if self._is_starting :
            self._pitch_pid_controller.set_current_pid(pitch_pid)
        
    def _accro_stick_scaling_received(self, event, stick_scaling):
        self._current_stick_scaling = self.translate_current_stick_scaling_from_board(stick_scaling)
        if self._is_starting :
            self._stick_scaling_controller.set_value(self._current_stick_scaling)
            self._set_synched()
            self._is_starting = False
        
        if self.is_synched():
            self._set_synched()
            self._protocol_handler.send_command_wihout_subscription(self._protocol_handler.COMMANDS['WriteUserValuesEEPROM'])
        
    def start(self):
        self._is_starting = True
        self._sync_in_progress = True
        self._protocol_handler.get_accro_pid();
    
    def stop(self):
        self._protocol_handler.unsubscribe_command()
        
    def sync_with_board(self):
        if self._is_starting :
            return

        if self.is_synched() :
            self._protocol_handler.unsubscribe_command()
            self._set_synched()
            return
        
        if self._cpt_before_send == 5 :
            self._protocol_handler.unsubscribe_command()
            self._send_pid_to_board()
            self._cpt_before_send = 0
            self._protocol_handler.get_accro_pid();
        else:
            self._protocol_handler.send_command_wihout_subscription(self._protocol_handler.COMMANDS['GetRatePID']);
            self._cpt_before_send = self._cpt_before_send + 1
            
    def is_synched(self):
        try:
            if not self._current_roll_pid.is_equals(self._roll_pid_controller.get_current_pid()) :
                return False
            elif not self._current_pitch_pid.is_equals(self._pitch_pid_controller.get_current_pid()) :
                return False
            elif float(self._current_stick_scaling) != float(self._stick_scaling_controller.get_value()):
                return False
        except:
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
        roll_pid = self._roll_pid_controller.get_current_pid()
        pitch_pid = self.get_pitch_pid_from_panel()
        stick_scaling = self.get_stick_scaling_from_panel()
        self._protocol_handler.set_accro_pid(roll_pid, pitch_pid, stick_scaling)
        
    def get_pitch_pid_from_panel(self):
        if self._user_update_mode == PIDUpdateMode.BEGINNER_MODE :
            self._pitch_pid_controller.set_current_pid(self._roll_pid_controller.get_current_pid())
            return self._roll_pid_controller.get_current_pid()
        else :
            return self._pitch_pid_controller.get_current_pid()
    
    def get_stick_scaling_from_panel(self):
        panel_value = self._stick_scaling_controller.get_value()
        return self.translate_stick_scaling_for_board(panel_value)
     
    def reset_default(self):
        self._roll_pid_controller.reset_default()
        self._pitch_pid_controller.reset_default()
        self._stick_scaling_controller.reset_default()
        
    def translate_current_stick_scaling_from_board(self,stick_scaling):
        if str(stick_scaling) == '1.00':
            return 1
        elif str(stick_scaling) == '0.90':
            return 2
        elif str(stick_scaling) == '0.80':
            return 3
        elif str(stick_scaling) == '0.70':
            return 4
        elif str(stick_scaling) == '0.60':
            return 5
        elif str(stick_scaling) == '0.50':
            return 6
    
    def translate_stick_scaling_for_board(self,panel_value):
        if int(panel_value) == 1 :
            return '1.00'
        elif float(panel_value) == 2 :
            return '0.90'
        elif float(panel_value) == 3 :
            return '0.80'
        elif float(panel_value) == 4 :
            return '0.70'
        elif float(panel_value) == 5 :
            return '0.60'
        elif float(panel_value) == 6 :
            return '0.50'
        
