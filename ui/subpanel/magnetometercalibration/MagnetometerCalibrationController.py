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
        
        self.running = False
        self.amount_axis = 3
        self.axix_max = [0, 0, 0] # x y z
        self.axis_min = [0, 0, 0] # x y z
        
        self.axix_x = '0'
        self.axix_y = '1'
        self.axix_z = '2'
        
        self.ui.start.clicked.connect(self.start_magnetometer_calibration)
        self.ui.cancel.clicked.connect(self.cancel_magnetometer_calibration)
        
        self._vehicle_model.register(self._magnetometer_x_raw_data_updated, VehicleModel.MAGNETOMETER_X_RAW_DATA_EVENT)
        self._vehicle_model.register(self._magnetometer_y_raw_data_updated, VehicleModel.MAGNETOMETER_Y_RAW_DATA_EVENT)
        self._vehicle_model.register(self._magnetometer_z_raw_data_updated, VehicleModel.MAGNETOMETER_Z_RAW_DATA_EVENT)
        
    
    def start_magnetometer_calibration(self):
        if self.running:    
            self.ui.start.setText("Start")
            self.cancel_magnetometer_calibration() #we can stop the calibration it's done
#            self.timer.stop()
            self.send_calibration_value()
        
        elif not self.running:
            if self.comm.is_connected() == True:
                self._protocol_handler.unsubscribe_command()
                self._protocol_handler.subscribe_raw_magnetometer()
                self.running = True
                
                self.ui.cancel.setEnabled(True)
                self.ui.next.setEnabled(False)
                
                self.ui.start.setText("Finish")
                
                self.axix_max = [0, 0, 0]
                self.axis_min = [0, 0, 0]
                
    def cancel_magnetometer_calibration(self):
        self.comm.write("x")
        self.running = False
        self.ui.cancel.setEnabled(False)
        self.ui.next.setEnabled(True)
        self.ui.start.setText("Start")
        self._protocol_handler.unsubscribe_command()
    
#    def read_continuousData(self):
#        isConnected = self.comm.isConnected()
#        if isConnected and not self.commData.empty():
#            string = self.commData.get()
#            string_out = string.split(',')
#            if self.running:
#                for i in range(0, self.amount_axis):
#                    if int(string_out[i]) < self.axis_min[i]:  
#                        self.axis_min[i] = int(string_out[i])
#                    if int(string_out[i]) > self.axix_max[i]:  
#                        self.axix_max[i] = int(string_out[i])
#                    self.update_gui(i, int(string_out[i]))
#                    
#        self.ui.commLog.append(self.timeStamp() + " <- " + self.commData.get())
#        self.ui.commLog.ensureCursorVisible() 

    def _magnetometer_x_raw_data_updated(self, sender, event, x = None):
        time.sleep(0.1)
#        self.ui.x_axis_progress_bar.setValue(int(x))
        self.ui._x_vertical_slider.setValue(int(x))
        self.ui.label_x.setText(x)
        
    def _magnetometer_y_raw_data_updated(self, sender, event, y = None):
        time.sleep(0.1)
#        self.ui.y_axis_progress_bar.setValue(int(y))
        self.ui._y_vertical_slider_2.setValue(int(y))
        self.ui.label_y.setText(y)
        
    def _magnetometer_z_raw_data_updated(self, sender, event, z = None):
        time.sleep(0.1)
#        self.ui.z_axis_progress_bar.setValue(int(z))
        self.ui._z_vertical_slider_3.setValue(int(z))
        self.ui.label_z.setText(z)
        
       
    def update_gui(self, axis, value):
        if axis == int(self.axix_x):
            self.ui.x_axis_progress_bar.setValue(value)
            self.ui.label_x.setText(str(value))
        if axis == int(self.axix_y):
            self.ui.x_axis_progress_bar.setValue(value)
            self.ui.label_y.setText(str(value))
        if axis == int(self.axix_z):
            self.ui.x_axis_progress_bar.setValue(value)
            self.ui.label_z.setText(str(value))
            
    #def send_calibration_value(self):
        #self.comm.write("X");
        #command = "M "
        #commands here
            
        #self.comm.write(command)