
from PyQt4 import QtGui
from ui.subpanel.BasePanelController import BasePanelController
from ui.subpanel.accelcalibration.AccelCalibrationPanel import Ui_AccelCalibrationPanel
from ui.UIEventDispatcher import UIEventDispatcher
from model.VehicleEventDispatcher import VehicleEventDispatcher
import math


class AccelCalibrationController(QtGui.QWidget, BasePanelController):

    LEVELLED_CALIBRATION_STEP_ID = 0
    UPSIDE_DOWN_CALIBRATION_STEP_ID = 1
    LEFT_SIDE_CALIBRATION_STEP_ID = 2
    RIGHT_SIDE_CALIBRATION_STEP_ID = 3
    NOSE_UP_CALIBRATION_STEP_ID = 4
    NOSE_DOWN_CALIBRATION_STEP_ID = 5
    COMPLETE_ACCEL_CALIBRATION_STEP_ID = 6
    
    NB_SAMPLE_TO_READ = 50
    ONE_G = 9.80665

    def __init__(self, vehicle_event_dispatcher, ui_event_dispatcher):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        
        self.ui = Ui_AccelCalibrationPanel()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self._start_button_pressed)
        self.ui.cancel_button.clicked.connect(self._cancel_button_pressed)
        self.ui.next_button.clicked.connect(self._next_button_pressed)
        self.ui.progress_bar.setMaximum(AccelCalibrationController.NB_SAMPLE_TO_READ)
        
        ui_event_dispatcher.register(self._protocol_handler_changed_event, UIEventDispatcher.PROTOCOL_HANDLER_EVENT)
        vehicle_event_dispatcher.register(self._accel_raw_data_received, VehicleEventDispatcher.ACCEL_RAW_DATA_EVENT)
        
        self._set_initial_panel_state()
        
    def _start_button_pressed(self):
        self._protocol_handler.subscribe_raw_accelerometer() 
        self.ui.start_button.setEnabled(False)
        self.ui.next_button.setEnabled(False)
        self.ui.cancel_button.setEnabled(True)
        self._calibration_raw_sum_values = [0,0,0,0,0,0]
        self._current_calibration_step = 0
        self._current_nb_sampled_read = 0
    
    def _cancel_button_pressed(self):
        self._protocol_handler.unsubscribe_command()
        self._set_initial_panel_state()
                   
    def _next_button_pressed(self): 
        if self.ui.next_button.text() == 'Next' :
            self._protocol_handler.subscribe_raw_accelerometer()
            self.ui.next_button.setEnabled(False)
        else :
            self._send_calibration_score()
            self._set_initial_panel_state()
        
    def _protocol_handler_changed_event(self, event, protocol_handler):
        self._protocol_handler = protocol_handler;
        
    def _accel_raw_data_received(self, event, accel_raw_data_vector):
        if self._current_calibration_step == AccelCalibrationController.LEVELLED_CALIBRATION_STEP_ID or \
           self._current_calibration_step == AccelCalibrationController.UPSIDE_DOWN_CALIBRATION_STEP_ID :
                self._calibration_raw_sum_values[self._current_calibration_step] = \
                    self._calibration_raw_sum_values[self._current_calibration_step] + accel_raw_data_vector.get_z()
                print " step 1"
        elif self._current_calibration_step == AccelCalibrationController.LEFT_SIDE_CALIBRATION_STEP_ID or \
             self._current_calibration_step == AccelCalibrationController.RIGHT_SIDE_CALIBRATION_STEP_ID :
                self._calibration_raw_sum_values[self._current_calibration_step] = \
                    self._calibration_raw_sum_values[self._current_calibration_step] + accel_raw_data_vector.get_y()
                print " step 2"
        else :
            self._calibration_raw_sum_values[self._current_calibration_step] = \
                self._calibration_raw_sum_values[self._current_calibration_step] + accel_raw_data_vector.get_x()
            print " step 3"
        
        self._current_nb_sampled_read = self._current_nb_sampled_read + 1
        self.ui.progress_bar.setValue(self._current_nb_sampled_read)
        
        if self._current_nb_sampled_read >= AccelCalibrationController.NB_SAMPLE_TO_READ:
            self._proceed_to_next_calibration_step();
            self._protocol_handler.unsubscribe_command()
        
    def _proceed_to_next_calibration_step(self):
        self._current_nb_sampled_read = 0
        self._current_calibration_step = self._current_calibration_step + 1
        self._update_panel_to_current_calibration_stage()
        self.ui.next_button.setEnabled(True)

    def start(self):
        self._protocol_handler.unsubscribe_command()
        self.ui.start_button.setEnabled(True)
        self.ui.next_button.setEnabled(False)
        self.ui.cancel_button.setEnabled(False)
        
        self._calibration_raw_sum_values = [0,0,0,0,0,0]
        self._current_calibration_step = 0
        self._current_nb_sampled_read = 0
        self._update_panel_to_current_calibration_stage()
    
    def _update_panel_to_current_calibration_stage (self):
        pictureScene = QtGui.QGraphicsScene()
        self.ui.next_button.setText("Next")
        
        if self._current_calibration_step == self.LEVELLED_CALIBRATION_STEP_ID:
            pictureBackground = QtGui.QPixmap("./resources/callevel.png")
            self.ui.information_display_text_box.setText("Place the AeroQuad on a flat and motionless surface and press the start to begin the calibration procedure")
        elif self._current_calibration_step == self.UPSIDE_DOWN_CALIBRATION_STEP_ID:
            pictureBackground = QtGui.QPixmap("./resources/callevel.png")
            self.ui.information_display_text_box.setText("Place the AeroQuad upside down and press start")
        elif self._current_calibration_step == self.LEFT_SIDE_CALIBRATION_STEP_ID:
            pictureBackground = QtGui.QPixmap("./resources/calleft.png")
            self.ui.information_display_text_box.setText("Place the AeroQuad left edge down and press start")
        elif self._current_calibration_step == self.RIGHT_SIDE_CALIBRATION_STEP_ID:
            pictureBackground = QtGui.QPixmap("./resources/calright.png")
            self.ui.information_display_text_box.setText("Place the AeroQuad right edge down and press start")
        elif self._current_calibration_step == self.NOSE_UP_CALIBRATION_STEP_ID:
            pictureBackground = QtGui.QPixmap("./resources/calfront.png")
            self.ui.information_display_text_box.setText("Place the AeroQuad front edge down and press start. The arrow indicates the front of the AeroQuad")
        elif self._current_calibration_step == self.NOSE_DOWN_CALIBRATION_STEP_ID:
            pictureBackground = QtGui.QPixmap("./resources/calrear.png")
            self.ui.information_display_text_box.setText("Place the AeroQuad rear edge down and press start. The arrow indicates the front of the AeroQuad")
        elif self._current_calibration_step == self.COMPLETE_ACCEL_CALIBRATION_STEP_ID:
            pictureBackground = QtGui.QPixmap("./resources/callevel.png")
            self.ui.information_display_text_box.setText("Place the AeroQuad on a flat surface and motionless surface and press the complete button to complete the calibration")
            self.ui.next_button.setText("Complete")
            
        pictureItem = QtGui.QGraphicsPixmapItem(pictureBackground)
        pictureScene.addItem(pictureItem)
        self.ui.picture_container.setScene(pictureScene)
    
    def _set_initial_panel_state(self):
        self.ui.start_button.setEnabled(True)
        self.ui.next_button.setEnabled(False)
        self.ui.cancel_button.setEnabled(False)
        self._current_calibration_step = 0
        self._calibration_raw_sum_values = [0,0,0,0,0,0]
        self._update_panel_to_current_calibration_stage()
        self.ui.progress_bar.setValue(0)
    
    def _send_calibration_score(self):
#        z_scale_factor = ((2.0 * AccelCalibrationController.ONE_G) / (math.fabs(self._calibration_raw_sum_values[0]) + math.fabs(self._calibration_raw_sum_values[1])))
#        y_scale_factor = ((2.0 * AccelCalibrationController.ONE_G) / (math.fabs(self._calibration_raw_sum_values[2]) + math.fabs(self._calibration_raw_sum_values[3])))
#        x_scale_factor = ((2.0 * AccelCalibrationController.ONE_G) / (math.fabs(self._calibration_raw_sum_values[4]) + math.fabs(self._calibration_raw_sum_values[5])))
        
        z_scale_factor = (2.0 * AccelCalibrationController.ONE_G) / (self._calibration_raw_sum_values[0] + self._calibration_raw_sum_values[1])
        y_scale_factor = (2.0 * AccelCalibrationController.ONE_G) / (self._calibration_raw_sum_values[2] + self._calibration_raw_sum_values[3])
        x_scale_factor = (2.0 * AccelCalibrationController.ONE_G) / (self._calibration_raw_sum_values[4] + self._calibration_raw_sum_values[5])

        print "value = " + str(x_scale_factor) + "," + str(y_scale_factor) + "," + str(z_scale_factor)
        
        self._protocol_handler.set_accel_calibration_scale_factor(x_scale_factor, y_scale_factor, z_scale_factor)
        