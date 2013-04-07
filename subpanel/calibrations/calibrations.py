#'''
#Created on Mar 21, 2013
#
#@author: Ted Carancho
#'''
#
#from PyQt4 import QtGui
#from subpanel.subPanel import SubPanel
#from subpanel.calibrations.calibrationWindow import Ui_CalibrationWizard
#from subpanel.calibrations.sensorCalibration import SensorWizard
#
#class Calibrations(QtGui.QWidget, SubPanel):
#    '''This will show a wizard interface to the user to perform required AeroQuad calibrations
#    '''
#    def __init__(self):
#        '''This initializes the calibration subpanel
#        '''
#        QtGui.QWidget.__init__(self)
#        SubPanel.__init__(self)
#        self.ui = Ui_CalibrationWizard()
#        self.ui.setupUi(self)
#        self.ui.pushButton.clicked.connect(self.sensorCalibration)
#
#    def sensorCalibration(self):
#        self.wiz = SensorWizard()
#        self.wiz.show()
#        self.wiz.exec_()
#        
#=======
'''
Created on Mar 21, 2013

@author: Ted Carancho
'''

from PyQt4 import QtGui
from subpanel.subPanel import SubPanel
from subpanel.calibrations.calibrationWindow import Ui_CalibrationWizard
from subpanel.calibrations.sensorCalibration import SensorWizard

class Calibrations(QtGui.QWidget, SubPanel):
    '''This will show a wizard interface to the user to perform required AeroQuad calibrations
    '''
    def __init__(self):
        '''This initializes the calibration subpanel
        '''
        QtGui.QWidget.__init__(self)
        SubPanel.__init__(self)
        self.ui = Ui_CalibrationWizard()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.sensorCalibration)

    def sensorCalibration(self):
        self.wiz = SensorWizard()
        self.wiz.show()
        self.wiz.exec_()
        