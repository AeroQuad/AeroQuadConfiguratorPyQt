# -*- coding: utf-8 -*-

from time import sleep

from PyQt4 import QtCore, QtGui
from ui.subpanel.BasePanelController import BasePanelController
from ui.subpanel.motorcommand.MotorCommandPanel import MotorCommandPanel


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
        
        self.speed = QtGui.QLabel(self)
        self.speed.setText('1000')

        self.motor_number = QtGui.QLabel(self)
        self.motor_number.setText('Motor %d' % motor_number)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.slider,       0, QtCore.Qt.AlignHCenter)
        layout.addWidget(self.speed,        0, QtCore.Qt.AlignHCenter)
        layout.addWidget(self.motor_number, 0, QtCore.Qt.AlignHCenter)
        
        self.setLayout(layout)
    
    def changeValue(self, value):
        self.speed.setText(str(value))

class MotorCommandController(QtGui.QWidget, BasePanelController):
    
    def __init__(self, event_dispatcher, protocol_handler, parent=None):
        super(MotorCommandController, self).__init__(parent)
        BasePanelController.__init__(self)
        self.ui = MotorCommandPanel()
        self.ui.setupUi(self)
        self.ui.sendButton.setEnabled(False)
        self.ui.clearButton.setEnabled(False)
       
        self.started = False


        # Connect GUI slots and signals
        self.ui.sendButton.clicked.connect(self.sendCommand)
        self.ui.clearButton.clicked.connect(self.clearCommand)

    def start(self):
        '''This method starts a timer used for any long running loops in a subpanel'''
#        self.xmlSubPanel     = xmlSubPanel
#        self.validateCommand = self.xml.find(self.xmlSubPanel + 'ValidateCommand').text
#        self.command_motor   = self.xml.find(self.xmlSubPanel + 'CommandMotor').text
#        self.boardConfiguration = boardConfiguration
#
#        if self.comm.isConnected() == True:
#            self.ui.sendButton.setEnabled(True)
#            self.ui.clearButton.setEnabled(True)
#
#            if not self.started:
#                motor_count  = int(self.boardConfiguration['Motors'])
#                motor_layout = self.ui.motor_slider_widget.layout()
#
#                self.ui.motor_sliders = [MotorSlider(motor_number=(i + 1)) for i in xrange(motor_count)]
#                for motor in self.ui.motor_sliders:
#                    motor_layout.addWidget(motor)
#
#                self.started = True
#
#            self.timer = QtCore.QTimer()
#            self.timer.timeout.connect(self.readContinuousData)
#            self.timer.start(50)

    def sendCommand(self):
        serial_string   = self.validateCommand + ';' + ';'.join([
            str(float(motor_slider.slider.value()))
            for motor_slider in self.ui.motor_sliders
        ])
        self.comm.write(self.command_motor)
        self.comm.write(serial_string)
        sleep(0.150)

    def readContinuousData(self):
        isConnected = self.comm.isConnected()
        self.ui.sendButton.setEnabled(isConnected)
        self.ui.clearButton.setEnabled(isConnected)

    def clearCommand(self):
        serial_string   = self.validateCommand + ';' + ';'.join([
            '1000.0' for motor_slider in self.ui.motor_sliders
        ])
        self.comm.write(self.command_motor)
        self.comm.write(serial_string)
        for motor_slider in self.ui.motor_sliders:
            motor_slider.slider.setValue(1000)
        sleep(0.150)

