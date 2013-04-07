## -*- coding: utf-8 -*-
#
## Form implementation generated from reading ui file 'calibrationWindow.ui'
##
## Created: Fri Mar 22 01:49:31 2013
##      by: PyQt4 UI code generator 4.9.5
##
## WARNING! All changes made in this file will be lost!
#
#from PyQt4 import QtCore, QtGui
#
#try:
#    _fromUtf8 = QtCore.QString.fromUtf8
#except AttributeError:
#    _fromUtf8 = lambda s: s
#
#class Ui_CalibrationWizard(object):
#    def setupUi(self, CalibrationWizard):
#        CalibrationWizard.setObjectName(_fromUtf8("CalibrationWizard"))
#        CalibrationWizard.resize(400, 300)
#        self.formLayout = QtGui.QFormLayout(CalibrationWizard)
#        self.formLayout.setObjectName(_fromUtf8("formLayout"))
#        self.pushButton = QtGui.QPushButton(CalibrationWizard)
#        self.pushButton.setObjectName(_fromUtf8("pushButton"))
#        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pushButton)
#
#        self.retranslateUi(CalibrationWizard)
#        QtCore.QMetaObject.connectSlotsByName(CalibrationWizard)
#
#    def retranslateUi(self, CalibrationWizard):
#        CalibrationWizard.setWindowTitle(QtGui.QApplication.translate("CalibrationWizard", "Calibration Wizard", None, QtGui.QApplication.UnicodeUTF8))
#        self.pushButton.setText(QtGui.QApplication.translate("CalibrationWizard", "Sensor Calibration", None, QtGui.QApplication.UnicodeUTF8))
#
#=======
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calibrationWindow.ui'
#
# Created: Fri Mar 22 01:49:31 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CalibrationWizard(object):
    def setupUi(self, CalibrationWizard):
        CalibrationWizard.setObjectName(_fromUtf8("CalibrationWizard"))
        CalibrationWizard.resize(400, 300)
        self.formLayout = QtGui.QFormLayout(CalibrationWizard)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.pushButton = QtGui.QPushButton(CalibrationWizard)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pushButton)

        self.retranslateUi(CalibrationWizard)
        QtCore.QMetaObject.connectSlotsByName(CalibrationWizard)

    def retranslateUi(self, CalibrationWizard):
        CalibrationWizard.setWindowTitle(QtGui.QApplication.translate("CalibrationWizard", "Calibration Wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("CalibrationWizard", "Sensor Calibration", None, QtGui.QApplication.UnicodeUTF8))
