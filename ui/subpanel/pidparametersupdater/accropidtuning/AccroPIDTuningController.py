
from ui.subpanel.BasePanelController import BasePanelController

from PyQt4 import QtGui
from ui.subpanel.pidparametersupdater.pidtuningpanel.PIDTuningPanel import Ui_PIDTuningPanel
from ui.subpanel.pidparametersupdater.pidwidget.PIDWidgetController import PIDWidgetController



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
        self._gyro_pitch_pid_controller.p_line.ui.label.setText('Pitch Gain')
        self._gyro_pitch_pid_controller.i_line.ui.label.setText('Pitch Error Correction')
        self._gyro_pitch_pid_controller.d_line.ui.label.setText('Pitch Set Point Adjustment')
        
        self.setBeginnerMode()
        self.ui.linked_check_box.clicked.connect(self._linked_checkbox_pressed)
        self._linked_checkbox_pressed()
        
    def _linked_checkbox_pressed(self):
        if self.ui.linked_check_box.isChecked():
            self._gyro_pitch_pid_controller.hide();
            self._gyro_roll_pid_controller.p_line.ui.label.setText('Gain')
            self._gyro_roll_pid_controller.i_line.ui.label.setText('Error Correction')
            self._gyro_roll_pid_controller.d_line.ui.label.setText('Set Point Adjustment')
        else :
            self._gyro_pitch_pid_controller.show();
            self._gyro_roll_pid_controller.p_line.ui.label.setText('Roll Gain')
            self._gyro_roll_pid_controller.i_line.ui.label.setText('Roll Error Correction')
            self._gyro_roll_pid_controller.d_line.ui.label.setText('Roll Set Point Adjustment')
        
    
    def setBeginnerMode(self):
        self.ui.linked_check_box.setChecked(True)
        self._linked_checkbox_pressed()
        self._gyro_pitch_pid_controller.hide()
        self._gyro_roll_pid_controller.hide_i_line()
        self._gyro_pitch_pid_controller.hide_i_line()
        self._gyro_roll_pid_controller.set_edit_box_enabled(False)
        
    def setIntermediateMode(self):
        self.ui.linked_check_box.setChecked(False)
        self._linked_checkbox_pressed()
        self._gyro_roll_pid_controller.hide_i_line()
        self._gyro_pitch_pid_controller.hide_i_line()
        self._gyro_pitch_pid_controller.show()
        self._gyro_roll_pid_controller.set_edit_box_enabled(False)
    
    def setAdvancedMode(self):
        self.ui.linked_check_box.setChecked(False)
        self._linked_checkbox_pressed()
        self._gyro_roll_pid_controller.show_i_line()
        self._gyro_pitch_pid_controller.show_i_line()
        self._gyro_roll_pid_controller.set_edit_box_enabled(True)

