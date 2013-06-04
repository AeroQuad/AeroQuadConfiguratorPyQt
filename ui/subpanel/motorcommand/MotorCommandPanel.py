# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MotorCommandPanel.ui'
#
# Created: Tue Jun 04 16:59:12 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MotorCommandPanel(object):
    def setupUi(self, MotorCommandPanel):
        MotorCommandPanel.setObjectName(_fromUtf8("MotorCommandPanel"))
        MotorCommandPanel.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MotorCommandPanel.sizePolicy().hasHeightForWidth())
        MotorCommandPanel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(False)
        MotorCommandPanel.setFont(font)
        self.stop_all_motors_button = QtGui.QPushButton(MotorCommandPanel)
        self.stop_all_motors_button.setGeometry(QtCore.QRect(600, 390, 101, 31))
        self.stop_all_motors_button.setObjectName(_fromUtf8("stop_all_motors_button"))
        self.send_command_button = QtGui.QPushButton(MotorCommandPanel)
        self.send_command_button.setGeometry(QtCore.QRect(600, 350, 100, 31))
        self.send_command_button.setObjectName(_fromUtf8("send_command_button"))
        self.unlock_check_box = QtGui.QCheckBox(MotorCommandPanel)
        self.unlock_check_box.setGeometry(QtCore.QRect(600, 320, 91, 17))
        self.unlock_check_box.setObjectName(_fromUtf8("unlock_check_box"))
        self.information_label = QtGui.QLabel(MotorCommandPanel)
        self.information_label.setGeometry(QtCore.QRect(0, 10, 581, 71))
        self.information_label.setAlignment(QtCore.Qt.AlignCenter)
        self.information_label.setWordWrap(True)
        self.information_label.setObjectName(_fromUtf8("information_label"))
        self.help_button = QtGui.QPushButton(MotorCommandPanel)
        self.help_button.setGeometry(QtCore.QRect(600, 10, 100, 31))
        self.help_button.setObjectName(_fromUtf8("help_button"))
        self.motor_slider_container = QtGui.QFrame(MotorCommandPanel)
        self.motor_slider_container.setGeometry(QtCore.QRect(10, 100, 581, 331))
        self.motor_slider_container.setFrameShape(QtGui.QFrame.Box)
        self.motor_slider_container.setObjectName(_fromUtf8("motor_slider_container"))
        self.gridLayout = QtGui.QGridLayout(self.motor_slider_container)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.retranslateUi(MotorCommandPanel)
        QtCore.QMetaObject.connectSlotsByName(MotorCommandPanel)

    def retranslateUi(self, MotorCommandPanel):
        MotorCommandPanel.setWindowTitle(_translate("MotorCommandPanel", "RC channel setup", None))
        self.stop_all_motors_button.setText(_translate("MotorCommandPanel", "Stop all motors", None))
        self.send_command_button.setText(_translate("MotorCommandPanel", "Send Command", None))
        self.unlock_check_box.setText(_translate("MotorCommandPanel", "Unlock sliders", None))
        self.information_label.setText(_translate("MotorCommandPanel", "<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">Sending motor commands to the AeroQuad will make motors spin!</span></p><p><span style=\" font-size:11pt; color:#ff0000;\">PLEASE REMOVE PROPELLERS TO PREVENT POSSIBLE INJURY</span></p></body></html>", None))
        self.help_button.setText(_translate("MotorCommandPanel", "HELP", None))

