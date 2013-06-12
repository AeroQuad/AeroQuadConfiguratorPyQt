
from PyQt4 import QtGui
from ui.subpanel.BasePanelController import BasePanelController
from ui.subpanel.magnetometercalibration.MagnetometerCalibrationPanel import Ui_MagnetometerCalibrationPanel
from model.VehicleEventDispatcher import VehicleEventDispatcher
from ui.UIEventDispatcher import UIEventDispatcher

class MagnetometerCalibrationController(QtGui.QWidget, BasePanelController):

    def __init__(self, vehicle_event_dispatcher, ui_event_dispatcher):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        self.ui = Ui_MagnetometerCalibrationPanel()
        self.ui.setupUi(self)
        
        self._min_mag_values = [0, 0, 0] 
        self._max_mag_values = [0, 0, 0] 
        
        self._axix_x = '0'
        self._axix_y = '1'
        self._axix_z = '2'
        
        self.ui.start_button.clicked.connect(self._start_button_pressed)
        self.ui.cancel_button.clicked.connect(self._cancel_button_pressed)
        
        vehicle_event_dispatcher.register(self._magnetometer_raw_data_updated, VehicleEventDispatcher.MAGNETOMETER_RAW_DATA_EVENT)
        ui_event_dispatcher.register(self._protocol_handler_changed_event, UIEventDispatcher.PROTOCOL_HANDLER_EVENT)
        

    def start(self):
        self._reset_progress_bars()

    def stop(self):
        self._cancel_button_pressed()
        
    def _protocol_handler_changed_event(self, event, protocol_handler):
        self._protocol_handler = protocol_handler;
        
    def _start_button_pressed(self):
        if self.ui.start_button.text() == 'Start':    
            self._protocol_handler.subscribe_raw_magnetometer()
            self.ui.cancel_button.setEnabled(True)
            self.ui.start_button.setText("Finish")
            self._min_mag_values = [0, 0, 0]
            self._max_mag_values = [0, 0, 0]
        else:
            self._protocol_handler.unsubscribe_command()
            self.ui.start_button.setText('Start')
            self._reset_progress_bars()
            self._send_mag_cal_values()
                
    def _cancel_button_pressed(self):
        self._protocol_handler.unsubscribe_command()
        self.ui.cancel_button.setEnabled(False)
        self.ui.start_button.setText("Start")
        self._reset_progress_bars()

    def _magnetometer_raw_data_updated(self, event, vector):
        self.ui.x_axis_progress_bar.setValue(int(vector.get_x()))
        self.ui.label_x.setText(vector.get_x())
        self._min_mag_values[0] = min(self._min_mag_values[0],vector.get_x())
        self._max_mag_values[0] = max(self._max_mag_values[0],vector.get_x())
        self.ui.y_axis_progress_bar.setValue(int(vector.get_y()))
        self.ui.label_y.setText(vector.get_y())
        self._min_mag_values[1] = min(self._min_mag_values[1],vector.get_y())
        self._max_mag_values[1] = max(self._max_mag_values[1],vector.get_y())
        self.ui.z_axis_progress_bar.setValue(int(vector.get_z()))
        self.ui.label_z.setText(vector.get_z())
        self._min_mag_values[2] = min(self._min_mag_values[2],vector.get_z())
        self._max_mag_values[2] = max(self._max_mag_values[2],vector.get_z())
        
    def _reset_progress_bars(self):
        self.ui.x_axis_progress_bar.setValue(0)
        self.ui.label_x.setText(str(0))
        self.ui.y_axis_progress_bar.setValue(0)
        self.ui.label_y.setText(str(0))
        self.ui.z_axis_progress_bar.setValue(0)
        self.ui.label_z.setText(str(0))
        
    def _send_mag_cal_values(self):
        self._protocol_handler.send_mag_calibration_values(self._min_mag_values,self._max_mag_values)
