# -*- coding: utf-8 -*-

from time import sleep

from PyQt4 import QtCore, QtGui
from ui.subpanel.BasePanelController import BasePanelController
from ui.UIEventDispatcher import UIEventDispatcher
from model.VehicleEventDispatcher import VehicleEventDispatcher
from ui.subpanel.motorcommand.MotorCommandPanel import Ui_MotorCommandPanel


class MotorSlider(QtGui.QWidget):
    
    def __init__(self, motor_number, parent=None):
        super(MotorSlider, self).__init__(parent)
        
        self.slider = QtGui.QSlider(self)
        self.slider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.slider.setOrientation(QtCore.Qt.Vertical)
        self.slider.setMinimum(1000)
        self.slider.setMaximum(1200)
        self.slider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.slider.setTickInterval(10)
        self.slider.setSingleStep(10)
        self.slider.valueChanged[int].connect(self.changeValue)
        
        self.slider_label = QtGui.QLabel(self)
        self.slider_label.setText('1000')

        self.motor_number = QtGui.QLabel(self)
        self.motor_number.setText('Motor %d' % motor_number)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.slider,       0, QtCore.Qt.AlignHCenter)
        layout.addWidget(self.slider_label, 0, QtCore.Qt.AlignHCenter)
        layout.addWidget(self.motor_number, 0, QtCore.Qt.AlignHCenter)
        
        self.setLayout(layout)
    
    def changeValue(self, value):
        self.slider_label.setText(str(value))

class MotorCommandController(QtGui.QWidget, BasePanelController):
    
    def __init__(self, vehicle_event_dispatcher, ui_event_dispatcher):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        self.ui = Ui_MotorCommandPanel()
        self.ui.setupUi(self)

        self._motor_slider1 = MotorSlider(1)
        self.ui.gridLayout.addWidget(self._motor_slider1, 0, 0, 1, 1)
        self._motor_slider2 = MotorSlider(2)
        self.ui.gridLayout.addWidget(self._motor_slider2, 0, 1, 1, 1)
        self._motor_slider3 = MotorSlider(3)
        self.ui.gridLayout.addWidget(self._motor_slider3, 0, 2, 1, 1)
        self._motor_slider4 = MotorSlider(4)
        self.ui.gridLayout.addWidget(self._motor_slider4, 0, 3, 1, 1)
        self._motor_slider5 = MotorSlider(5)
        self.ui.gridLayout.addWidget(self._motor_slider5, 0, 4, 1, 1)
        self._motor_slider6 = MotorSlider(6)
        self.ui.gridLayout.addWidget(self._motor_slider6, 0, 5, 1, 1)
        self._motor_slider7 = MotorSlider(7)
        self.ui.gridLayout.addWidget(self._motor_slider7, 0, 4, 1, 1)
        self._motor_slider8 = MotorSlider(8) 
        self.ui.gridLayout.addWidget(self._motor_slider8, 0, 5, 1, 1)
        
        self.ui.unlock_check_box.stateChanged.connect(self._check_box_state_changed)
        self.ui.send_command_button.clicked.connect(self._send_motors_commands)
        self.ui.stop_all_motors_button.clicked.connect(self._send_stop_commands)
        self.ui.help_button.clicked.connect(self._display_help_image)
        
        self._timer = None
        
        ui_event_dispatcher.register(self._protocol_handler_changed_event, UIEventDispatcher.PROTOCOL_HANDLER_EVENT)
        vehicle_event_dispatcher.register(self._nb_motors_received, VehicleEventDispatcher.NUMBER_MOTORS_EVENT)
        
        
    def stop(self):
        self._stop_timer()
        self._send_stop_commands()
        
    def _protocol_handler_changed_event(self, event, protocol_handler):
        self._protocol_handler = protocol_handler;

    def _nb_motors_received(self, event, nb_motors):
        self._nb_motors = nb_motors
        self._motor_slider5.hide()
        self._motor_slider6.hide()
        self._motor_slider7.hide()
        self._motor_slider8.hide()
        if nb_motors > '4' :
            self._motor_slider5.show()
            self._motor_slider6.show()
        if nb_motors > '6' :
            self._motor_slider7.show()
            self._motor_slider8.show()
            
    def _check_box_state_changed(self, value):
        if self.ui.unlock_check_box.isChecked() :
            reply = QtGui.QMessageBox.question(self, 'ARE YOU SURE?', 
                         'Motor commands will be sent directly to the Aeroquad on slider moves', 
                         QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if QtGui.QMessageBox.No == reply:
                self.ui.unlock_check_box.setCheckState(0)
            else :
                self.ui.send_command_button.setEnabled(False)
                self.ui.stop_all_motors_button.setEnabled(False)
                self._start_command_sender_timer()
        else :
            self.ui.send_command_button.setEnabled(True)
            self.ui.stop_all_motors_button.setEnabled(True)
            self._stop_timer()
            self._send_stop_commands()
                
    def _stop_timer(self):
        if self._timer is not None:
            self._timer.stop()
            self._timer = None
        
    def _start_command_sender_timer(self):
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self._send_motor_commands_timer_callback)
        self._timer.start(400)
        
    def _send_motor_commands_timer_callback(self):
        self._send_motors_commands()
        
    def _motor_slider_value_changed(self, value):
        if self.ui.unlock_check_box.isChecked() :
            self._send_motors_commands()
        
    def _send_stop_commands(self):
        self._motor_slider1.slider.setValue(1000)
        self._motor_slider2.slider.setValue(1000)
        self._motor_slider3.slider.setValue(1000)
        self._motor_slider4.slider.setValue(1000)
        self._motor_slider5.slider.setValue(1000)
        self._motor_slider6.slider.setValue(1000)
        self._motor_slider7.slider.setValue(1000)
        self._motor_slider8.slider.setValue(1000)
        self._send_motors_commands()
        
    def _send_motors_commands(self):
        self._protocol_handler.send_motos_command(
                        self._nb_motors,
                        self._motor_slider1.slider.value(),
                        self._motor_slider2.slider.value(),
                        self._motor_slider3.slider.value(),
                        self._motor_slider4.slider.value(),
                        self._motor_slider5.slider.value(),
                        self._motor_slider6.slider.value(),
                        self._motor_slider7.slider.value(),
                        self._motor_slider8.slider.value())
        
    def _display_help_image(self):
        pass
