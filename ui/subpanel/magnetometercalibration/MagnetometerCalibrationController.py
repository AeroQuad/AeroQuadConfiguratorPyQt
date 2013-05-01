'''
Created on 26 apr. 2013

@author: Erik
'''

import logging
from PyQt4 import QtGui
import time

from ui.subpanel.BasePanelController import BasePanelController
from ui.subpanel.magnetometercalibration.MagnetometerCalibrationPanel import Ui_MagnetometerCalibrationPanel
from model.VehicleModel import VehicleModel

class MagnetometerCalibrationController(QtGui.QWidget, BasePanelController):

    def __init__(self, vehicle_model, protocol_handler):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        
        self._vehicle_model = vehicle_model
        self._protocol_handler = protocol_handler
        
        self.ui = Ui_MagnetometerCalibrationPanel()
        self.ui.setupUi(self)
        
        self._is_running = False
        self._amount_axis = 3
        self._axix_max = [0, 0, 0] # x y z
        self._axis_min = [0, 0, 0] # x y z
        
        self._axix_x = '0'
        self._axix_y = '1'
        self._axix_z = '2'
        
        self._is_connected = False
        
        self.ui.start.clicked.connect(self.start_magnetometer_calibration)
        self.ui.cancel.clicked.connect(self.cancel_magnetometer_calibration)
        
        self._vehicle_model.register(self._magnetometer_raw_data_updated, VehicleModel.MAGNETOMETER_RAW_DATA_EVENT)
        self._vehicle_model.register(self._connection_state_changed, VehicleModel.CONNECTION_STATE_CHANGED_EVENT)
        
    
    def start_magnetometer_calibration(self):
        if self._is_running:    
            self.ui.start.setText("Start")
            self.cancel_magnetometer_calibration() #we can stop the calibration it's done
#            self.send_calibration_value()
        
        elif not self._is_running:
            if self._is_connected:
                self._protocol_handler.unsubscribe_command()
                self._protocol_handler.subscribe_raw_magnetometer()
                self._is_running = True
                
                self.ui.cancel.setEnabled(True)
                self.ui.next.setEnabled(False)
                
                self.ui.start.setText("Finish")
                
                self._axix_max = [0, 0, 0]
                self._axis_min = [0, 0, 0]
                
    def cancel_magnetometer_calibration(self):
        self._protocol_handler.unsubscribe_command()
        self._is_running = False
        self.ui.cancel.setEnabled(False)
        self.ui.next.setEnabled(True)
        self.ui.start.setText("Start")
        
    
#    def read_continuousData(self):
#        isConnected = self.comm.isConnected()
#        if isConnected and not self.commData.empty():
#            string = self.commData.get()
#            string_out = string.split(',')
#            if self._is_running:
#                for i in range(0, self._amount_axis):
#                    if int(string_out[i]) < self._axis_min[i]:  
#                        self._axis_min[i] = int(string_out[i])
#                    if int(string_out[i]) > self._axix_max[i]:  
#                        self._axix_max[i] = int(string_out[i])
#                    self.update_gui(i, int(string_out[i]))
#                    
#        self.ui.commLog.append(self.timeStamp() + " <- " + self.commData.get())
#        self.ui.commLog.ensureCursorVisible() 

    def _connection_state_changed(self, sender, event, is_connected = None):
        self._is_connected = is_connected

    def _magnetometer_raw_data_updated(self, sender, event, vector = None):
        self.ui.x_axis_progress_bar.setValue(int(vector.get_x()))
        self.ui.label_x.setText(vector.get_x())
        self.ui.y_axis_progress_bar.setValue(int(vector.get_y()))
        self.ui.label_y.setText(vector.get_y())
        self.ui.z_axis_progress_bar.setValue(int(vector.get_z()))
        self.ui.label_z.setText(vector.get_z())
        
    def update_gui(self, axis, value):
        if axis == int(self._axix_x):
            self.ui.x_axis_progress_bar.setValue(value)
            self.ui.label_x.setText(str(value))
        if axis == int(self._axix_y):
            self.ui.x_axis_progress_bar.setValue(value)
            self.ui.label_y.setText(str(value))
        if axis == int(self._axix_z):
            self.ui.x_axis_progress_bar.setValue(value)
            self.ui.label_z.setText(str(value))
            
    #def send_calibration_value(self):
        #self.comm.write("X");
        #command = "M "
        #commands here
            
        #self.comm.write(command)