# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePanel.ui'
#
# Created: Sat Apr 27 19:46:06 2013
#      by: PyQt4 UI code generator 4.10
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

class Ui_HomePanel(object):
    def setupUi(self, HomePanel):
        HomePanel.setObjectName(_fromUtf8("HomePanel"))
        HomePanel.resize(800, 600)
        HomePanel.setStyleSheet(_fromUtf8("<align=\'center\'>"))
        self.button_vehicle_setup = QtGui.QToolButton(HomePanel)
        self.button_vehicle_setup.setGeometry(QtCore.QRect(580, 70, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_vehicle_setup.setFont(font)
        self.button_vehicle_setup.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./resources/setup.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_vehicle_setup.setIcon(icon)
        self.button_vehicle_setup.setIconSize(QtCore.QSize(150, 150))
        self.button_vehicle_setup.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_vehicle_setup.setAutoRaise(False)
        self.button_vehicle_setup.setObjectName(_fromUtf8("button_vehicle_setup"))
        self.button_serial_monitor = QtGui.QToolButton(HomePanel)
        self.button_serial_monitor.setGeometry(QtCore.QRect(300, 70, 131, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_serial_monitor.setFont(font)
        self.button_serial_monitor.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./resources/serial_monitor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_serial_monitor.setIcon(icon1)
        self.button_serial_monitor.setIconSize(QtCore.QSize(100, 100))
        self.button_serial_monitor.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_serial_monitor.setAutoRaise(False)
        self.button_serial_monitor.setObjectName(_fromUtf8("button_serial_monitor"))
        self.button_firmware_download = QtGui.QToolButton(HomePanel)
        self.button_firmware_download.setGeometry(QtCore.QRect(440, 70, 131, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_firmware_download.setFont(font)
        self.button_firmware_download.setAutoFillBackground(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./resources/download.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_firmware_download.setIcon(icon2)
        self.button_firmware_download.setIconSize(QtCore.QSize(100, 100))
        self.button_firmware_download.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_firmware_download.setAutoRaise(False)
        self.button_firmware_download.setObjectName(_fromUtf8("button_firmware_download"))
        self.button_vehicle_configuration = QtGui.QToolButton(HomePanel)
        self.button_vehicle_configuration.setGeometry(QtCore.QRect(160, 70, 131, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_vehicle_configuration.setFont(font)
        self.button_vehicle_configuration.setAutoFillBackground(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./resources/configuration.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_vehicle_configuration.setIcon(icon3)
        self.button_vehicle_configuration.setIconSize(QtCore.QSize(100, 100))
        self.button_vehicle_configuration.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_vehicle_configuration.setAutoRaise(False)
        self.button_vehicle_configuration.setObjectName(_fromUtf8("button_vehicle_configuration"))
        self.button_vehicle_status = QtGui.QToolButton(HomePanel)
        self.button_vehicle_status.setGeometry(QtCore.QRect(20, 70, 131, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_vehicle_status.setFont(font)
        self.button_vehicle_status.setAutoFillBackground(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("./resources/info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_vehicle_status.setIcon(icon4)
        self.button_vehicle_status.setIconSize(QtCore.QSize(100, 100))
        self.button_vehicle_status.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_vehicle_status.setAutoRaise(False)
        self.button_vehicle_status.setObjectName(_fromUtf8("button_vehicle_status"))

        self.retranslateUi(HomePanel)
        QtCore.QMetaObject.connectSlotsByName(HomePanel)

    def retranslateUi(self, HomePanel):
        HomePanel.setWindowTitle(_translate("HomePanel", "Form", None))
        self.button_vehicle_setup.setToolTip(_translate("HomePanel", "Vechile setup wizzard", None))
        self.button_vehicle_setup.setStatusTip(_translate("HomePanel", "Vechile setup wizzard", None))
        self.button_vehicle_setup.setText(_translate("HomePanel", "Vehicle setup", None))
        self.button_serial_monitor.setToolTip(_translate("HomePanel", "Serial monitor", None))
        self.button_serial_monitor.setStatusTip(_translate("HomePanel", "Serial monitor", None))
        self.button_serial_monitor.setText(_translate("HomePanel", "Serial monitor", None))
        self.button_firmware_download.setToolTip(_translate("HomePanel", "Download firmware to the AeroQuad", None))
        self.button_firmware_download.setStatusTip(_translate("HomePanel", "Download firmware to the AeroQuad", None))
        self.button_firmware_download.setText(_translate("HomePanel", "Download", None))
        self.button_vehicle_configuration.setToolTip(_translate("HomePanel", "Vehicle configuration", None))
        self.button_vehicle_configuration.setStatusTip(_translate("HomePanel", "Vehicle configuration", None))
        self.button_vehicle_configuration.setText(_translate("HomePanel", "Vehicle config", None))
        self.button_vehicle_status.setToolTip(_translate("HomePanel", "Vehicle status", None))
        self.button_vehicle_status.setStatusTip(_translate("HomePanel", "Vehicle status", None))
        self.button_vehicle_status.setText(_translate("HomePanel", "Vehicle status", None))

