
from ui.subpanel.BasePanelController import BasePanelController

from PyQt4 import QtGui
from ui.subpanel.pidparametersupdater.pidtuningpanel.PIDTuningPanel import Ui_PIDTuningPanel
from ui.subpanel.pidparametersupdater.pidwidget.PIDWidgetController import PIDWidgetController
from ui.UIEventDispatcher import UIEventDispatcher



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
        self._gyro_pitch_pid_controller.set_title('PID tuning')
        self._gyro_pitch_pid_controller.p_line.ui.title_label.setText('Pitch Gain')
        self._gyro_pitch_pid_controller.p_line.ui.default_label.setText('100')
        self._gyro_pitch_pid_controller.i_line.ui.title_label.setText('Pitch Error Correction')
        self._gyro_pitch_pid_controller.i_line.ui.default_label.setText('150')
        self._gyro_pitch_pid_controller.d_line.ui.title_label.setText('Pitch Set Point')
        self._gyro_pitch_pid_controller.d_line.ui.default_label.setText('-350')
        
        self._gyro_roll_pid_controller.set_title('PID tuning')
        self._gyro_roll_pid_controller.p_line.ui.title_label.setText('Gain')
        self._gyro_roll_pid_controller.p_line.ui.default_label.setText('100')
        self._gyro_roll_pid_controller.i_line.ui.title_label.setText('Error Correction')
        self._gyro_roll_pid_controller.i_line.ui.default_label.setText('150')
        self._gyro_roll_pid_controller.d_line.ui.title_label.setText('Set Point')
        self._gyro_roll_pid_controller.d_line.ui.default_label.setText('-300')
        
        self.setBeginnerMode()
        
        ui_event_dispatcher.register(self._protocol_handler_changed_event, UIEventDispatcher.PROTOCOL_HANDLER_EVENT)

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
        
    def start(self):
        self._protocol_handler.get_accro_pid();

