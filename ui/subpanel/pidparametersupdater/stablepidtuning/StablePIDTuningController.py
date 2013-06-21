
from ui.subpanel.BasePanelController import BasePanelController

from PyQt4 import QtGui
from ui.subpanel.pidparametersupdater.pidtuningpanel.PIDTuningPanel import Ui_PIDTuningPanel
from ui.subpanel.pidparametersupdater.pidwidget.PIDWidgetController import PIDWidgetController


class StablePIDTuningController(QtGui.QWidget, BasePanelController):

    def __init__(self, vehicle_event_dispatcher, ui_event_dispatcher):

        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        
        self.ui = Ui_PIDTuningPanel()
        self.ui.setupUi(self)

        self._accel_roll_pid_controller = PIDWidgetController()
        self.ui.main_layout.addWidget(self._accel_roll_pid_controller)
        self._accel_roll_pid_controller.hide_i_line()
        self._accel_roll_pid_controller.hide_d_line()
        self._accel_roll_pid_controller.p_line.ui.label.setText('Accel Roll Gain')
        self._accel_roll_pid_controller.i_line.ui.label.setText('Accel Roll Error Correction')
        self._accel_roll_pid_controller.d_line.ui.label.setText('Accel Roll Set Point Adjustment')
        
        self._gyro_roll_pid_controller = PIDWidgetController()
        self.ui.main_layout.addWidget(self._gyro_roll_pid_controller)
        self._gyro_roll_pid_controller.hide_i_line()
        self._gyro_roll_pid_controller.p_line.ui.label.setText('Gyro Roll Gain')
        self._gyro_roll_pid_controller.i_line.ui.label.setText('Gyro Roll Error Correction')
        self._gyro_roll_pid_controller.d_line.ui.label.setText('Gyro Roll Set Point Adjustment')
        
        self._accel_pitch_pid_controller = PIDWidgetController()
        self.ui.main_layout.addWidget(self._accel_pitch_pid_controller)
        self._accel_pitch_pid_controller.hide_i_line()
        self._accel_pitch_pid_controller.hide_d_line()
        self._accel_pitch_pid_controller.p_line.ui.label.setText('Accel Pitch Gain')
        self._accel_pitch_pid_controller.i_line.ui.label.setText('Accel Pitch Error Correction')
        self._accel_pitch_pid_controller.d_line.ui.label.setText('Accel Pitch Set Point Adjustment')
        
        self._gyro_pitch_pid_controller = PIDWidgetController()
        self.ui.main_layout.addWidget(self._gyro_pitch_pid_controller)
        self._gyro_pitch_pid_controller.p_line.ui.label.setText('Gyro Pitch Gain')
        self._gyro_pitch_pid_controller.i_line.ui.label.setText('Gyro Pitch Error Correction')
        self._gyro_pitch_pid_controller.d_line.ui.label.setText('Gyro Pitch Set Point Adjustment')
        
        self.setBeginnerMode()
        self.ui.linked_check_box.clicked.connect(self._linked_checkbox_pressed)
        self._linked_checkbox_pressed()
        
    def _linked_checkbox_pressed(self):
        if self.ui.linked_check_box.isChecked():
            self._accel_pitch_pid_controller.hide();
            self._gyro_pitch_pid_controller.hide();
            self._gyro_roll_pid_controller.p_line.ui.label.setText('Gyro Gain Factor')
            self._gyro_roll_pid_controller.i_line.ui.label.setText('Gyro Error Correction Factor')
            self._gyro_roll_pid_controller.d_line.ui.label.setText('Gyro Set Point Adjustment Factor')
        else :
            self._accel_pitch_pid_controller.show();
            self._gyro_pitch_pid_controller.show();
            self._gyro_roll_pid_controller.p_line.ui.label.setText('Gyro Roll Gain Factor')
            self._gyro_roll_pid_controller.i_line.ui.label.setText('Gyro Roll Error Correction Factor')
            self._gyro_roll_pid_controller.d_line.ui.label.setText('Gyro Roll Set Point Adjustment Factor')
        
    
    def setBeginnerMode(self):
        self.ui.linked_check_box.setChecked(True)
        self._linked_checkbox_pressed()
        self._accel_roll_pid_controller.hide_i_line()
        self._accel_roll_pid_controller.hide_d_line()
        self._accel_pitch_pid_controller.hide_i_line()
        self._accel_pitch_pid_controller.hide_d_line()
        self._gyro_roll_pid_controller.hide_i_line()
        self._gyro_pitch_pid_controller.hide_i_line()
        self._gyro_roll_pid_controller.set_edit_box_enabled(False)
        
    def setIntermediateMode(self):
        self.ui.linked_check_box.setChecked(False)
        self._linked_checkbox_pressed()
        self._accel_roll_pid_controller.hide_i_line()
        self._accel_roll_pid_controller.hide_d_line()
        self._accel_pitch_pid_controller.hide_i_line()
        self._accel_pitch_pid_controller.hide_d_line()
        self._gyro_roll_pid_controller.hide_i_line()
        self._gyro_pitch_pid_controller.hide_i_line()
        self._gyro_roll_pid_controller.set_edit_box_enabled(False)
            
    def setAdvancedMode(self):
        self.ui.linked_check_box.setChecked(False)
        self._accel_roll_pid_controller.show_i_line()
        self._accel_roll_pid_controller.show_d_line()
        self._accel_pitch_pid_controller.show_i_line()
        self._accel_pitch_pid_controller.show_d_line()
        self._gyro_roll_pid_controller.show_i_line()
        self._gyro_pitch_pid_controller.show_i_line()
        self._gyro_roll_pid_controller.set_edit_box_enabled(True)
        