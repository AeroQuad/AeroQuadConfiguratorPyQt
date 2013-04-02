'''
Created on Apr 1, 2013

@author: Ted Carancho
'''

import time
from PyQt4 import QtGui, QtCore

class SensorWizard(QtGui.QWizard):
    '''This calibration wizard is for the sensors: gyros, accles, magnetometer
    '''
    def __init__(self, parent=None):
        super(SensorWizard, self).__init__(parent)
        self.addPage(AccelLevel(self))
        self.addPage(AccelLeft(self))
        self.addPage(AccelRight(self))
        self.addPage(AccelBack(self))
        self.addPage(AccelFront(self))
        self.addPage(Magnetometer(self))
        # images won't show in Windows 7 if style not set
        self.setWizardStyle(self.ModernStyle)
        self.setPixmap(QtGui.QWizard.LogoPixmap, QtGui.QPixmap("./resources/AQ.png"))
        self.setWindowTitle("Sensor Calibration Wizard")
 

class AccelLevel(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(AccelLevel, self).__init__(parent)
        self.setTitle("Level the AeroQuad")
        self.setPixmap(QtGui.QWizard.WatermarkPixmap, QtGui.QPixmap("./resources/calLevel.png"))
        topLabel = QtGui.QLabel("Place the AeroQuad on a level surface and do not move.")
        topLabel.setWordWrap(True)
        self.calButton = QtGui.QPushButton("Start Calibration Measurement")
        self.statusLabel = QtGui.QLineEdit()
        self.statusLabel.hide()
        self.statusBar = QtGui.QProgressBar()
        self.statusBar.setValue(0)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(topLabel)
        layout.addWidget(self.calButton)
        layout.addWidget(self.statusBar)
        layout.addWidget(self.statusLabel)
        self.setLayout(layout)
        self.registerField("statusLevel*", self.statusLabel)
        self.calButton.clicked.connect(self.levelCalibration)
        
    def levelCalibration(self):
        for status in range(101):
            self.statusBar.setValue(status)
            time.sleep(0.025)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setText("Calibration Complete")
        self.calButton.setText("Redo Calibration Measurement")
        
        
class AccelLeft(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(AccelLeft, self).__init__(parent)
        self.setTitle("Left Side Calibration")
        self.setPixmap(QtGui.QWizard.WatermarkPixmap, QtGui.QPixmap("./resources/calLeft.png"))
        topLabel = QtGui.QLabel("Position the AeroQuad with it's left side pointed down.  The arrow denotes the front of the AeroQuad.")
        topLabel.setWordWrap(True)
        self.calButton = QtGui.QPushButton("Start Calibration Measurement")
        self.statusLabel = QtGui.QLineEdit()
        self.statusLabel.hide()
        self.statusBar = QtGui.QProgressBar()
        self.statusBar.setValue(0)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(topLabel)
        layout.addWidget(self.calButton)
        layout.addWidget(self.statusBar)
        layout.addWidget(self.statusLabel)
        self.setLayout(layout)
        self.registerField("statusLeft*", self.statusLabel);
        self.calButton.clicked.connect(self.levelCalibration)
        
    def levelCalibration(self):
        for status in range(101):
            self.statusBar.setValue(status)
            time.sleep(0.025)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setText("Calibration Complete")
        self.calButton.setText("Redo Calibration Measurement")
 
class AccelRight(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(AccelRight, self).__init__(parent)
        self.setTitle("Right Side Calibration")
        self.setPixmap(QtGui.QWizard.WatermarkPixmap, QtGui.QPixmap("./resources/calRight.png"))
        topLabel = QtGui.QLabel("Position the AeroQuad with it's right side pointed down.  The arrow denotes the front of the AeroQuad.")
        topLabel.setWordWrap(True)
        self.calButton = QtGui.QPushButton("Start Calibration Measurement")
        self.statusLabel = QtGui.QLineEdit()
        self.statusLabel.hide()
        self.statusBar = QtGui.QProgressBar()
        self.statusBar.setValue(0)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(topLabel)
        layout.addWidget(self.calButton)
        layout.addWidget(self.statusBar)
        layout.addWidget(self.statusLabel)
        self.setLayout(layout)
        self.registerField("statusRight*", self.statusLabel);
        self.calButton.clicked.connect(self.levelCalibration)
        
    def levelCalibration(self):
        for status in range(101):
            self.statusBar.setValue(status)
            time.sleep(0.025)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setText("Calibration Complete")
        self.calButton.setText("Redo Calibration Measurement")

class AccelBack(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(AccelBack, self).__init__(parent)
        self.setTitle("Rear Calibration")
        self.setPixmap(QtGui.QWizard.WatermarkPixmap, QtGui.QPixmap("./resources/calRear.png"))
        topLabel = QtGui.QLabel("Position the AeroQuad with it's rear side pointed down.  The arrow denotes the front of the AeroQuad.")
        topLabel.setWordWrap(True)
        self.calButton = QtGui.QPushButton("Start Calibration Measurement")
        self.statusLabel = QtGui.QLineEdit()
        self.statusLabel.hide()
        self.statusBar = QtGui.QProgressBar()
        self.statusBar.setValue(0)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(topLabel)
        layout.addWidget(self.calButton)
        layout.addWidget(self.statusBar)
        layout.addWidget(self.statusLabel)
        self.setLayout(layout)
        self.registerField("statusRear*", self.statusLabel);
        self.calButton.clicked.connect(self.levelCalibration)
        
    def levelCalibration(self):
        for status in range(101):
            self.statusBar.setValue(status)
            time.sleep(0.025)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setText("Calibration Complete")
        self.calButton.setText("Redo Calibration Measurement")

class AccelFront(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(AccelFront, self).__init__(parent)
        self.setTitle("Front Calibration")
        self.setPixmap(QtGui.QWizard.WatermarkPixmap, QtGui.QPixmap("./resources/calFront.png"))
        topLabel = QtGui.QLabel("Position the AeroQuad with it's front side pointed down.  The arrow denotes the front of the AeroQuad.")
        topLabel.setWordWrap(True)
        self.calButton = QtGui.QPushButton("Start Calibration Measurement")
        self.statusLabel = QtGui.QLineEdit()
        self.statusLabel.hide()
        self.statusBar = QtGui.QProgressBar()
        self.statusBar.setValue(0)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(topLabel)
        layout.addWidget(self.calButton)
        layout.addWidget(self.statusBar)
        layout.addWidget(self.statusLabel)
        self.setLayout(layout)
        self.registerField("statusFront*", self.statusLabel);
        self.calButton.clicked.connect(self.levelCalibration)
        
    def levelCalibration(self):
        for status in range(101):
            self.statusBar.setValue(status)
            time.sleep(0.025)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setText("Calibration Complete")
        self.calButton.setText("Redo Calibration Measurement")

class Magnetometer(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Magnetometer, self).__init__(parent)
        self.setTitle("Magnetometer")
        self.setPixmap(QtGui.QWizard.WatermarkPixmap, QtGui.QPixmap("./resources/calLevel.png"))
        topLabel = QtGui.QLabel("Rotate the AeroQuad along it's X, Y and Z axis.")
        topLabel.setWordWrap(True)
        self.calButton = QtGui.QPushButton("Start Calibration Measurement")
        self.statusLabel = QtGui.QLineEdit()
        self.statusLabel.hide()
        self.statusBar = QtGui.QProgressBar()
        self.statusBar.setValue(0)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(topLabel)
        layout.addWidget(self.calButton)
        layout.addWidget(self.statusBar)
        layout.addWidget(self.statusLabel)
        self.setLayout(layout)
        self.registerField("statusMag*", self.statusLabel);
        self.calButton.clicked.connect(self.magCalibration)
        
    def magCalibration(self):
        for status in range(101):
            self.statusBar.setValue(status)
            time.sleep(0.025)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setText("Calibration Complete")
        self.calButton.setText("Redo Calibration Measurement")
        print(self.field("statusMag").toString())