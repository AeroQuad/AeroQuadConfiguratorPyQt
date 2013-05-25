# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenuePanel.ui'
#
# Created: Sat May 25 09:25:36 2013
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

class Ui_MainMenuePanel(object):
    def setupUi(self, MainMenuePanel):
        MainMenuePanel.setObjectName(_fromUtf8("MainMenuePanel"))
        MainMenuePanel.resize(800, 600)
        MainMenuePanel.setStyleSheet(_fromUtf8("<align=\'center\'>"))
        self.button_vehicle_setup = QtGui.QToolButton(MainMenuePanel)
        self.button_vehicle_setup.setGeometry(QtCore.QRect(300, 70, 131, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_vehicle_setup.setFont(font)
        self.button_vehicle_setup.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../resources/setup.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_vehicle_setup.setIcon(icon)
        self.button_vehicle_setup.setIconSize(QtCore.QSize(100, 100))
        self.button_vehicle_setup.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_vehicle_setup.setAutoRaise(False)
        self.button_vehicle_setup.setObjectName(_fromUtf8("button_vehicle_setup"))
        self.button_vehicle_configuration = QtGui.QToolButton(MainMenuePanel)
        self.button_vehicle_configuration.setGeometry(QtCore.QRect(160, 70, 131, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_vehicle_configuration.setFont(font)
        self.button_vehicle_configuration.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../../resources/configuration.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_vehicle_configuration.setIcon(icon1)
        self.button_vehicle_configuration.setIconSize(QtCore.QSize(100, 100))
        self.button_vehicle_configuration.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_vehicle_configuration.setAutoRaise(False)
        self.button_vehicle_configuration.setObjectName(_fromUtf8("button_vehicle_configuration"))
        self.button_vehicle_status = QtGui.QToolButton(MainMenuePanel)
        self.button_vehicle_status.setGeometry(QtCore.QRect(20, 70, 131, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_vehicle_status.setFont(font)
        self.button_vehicle_status.setAutoFillBackground(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../../../resources/info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_vehicle_status.setIcon(icon2)
        self.button_vehicle_status.setIconSize(QtCore.QSize(100, 100))
        self.button_vehicle_status.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_vehicle_status.setAutoRaise(False)
        self.button_vehicle_status.setObjectName(_fromUtf8("button_vehicle_status"))

        self.retranslateUi(MainMenuePanel)
        QtCore.QMetaObject.connectSlotsByName(MainMenuePanel)

    def retranslateUi(self, MainMenuePanel):
        MainMenuePanel.setWindowTitle(_translate("MainMenuePanel", "Form", None))
        self.button_vehicle_setup.setToolTip(_translate("MainMenuePanel", "Vechile setup wizzard", None))
        self.button_vehicle_setup.setStatusTip(_translate("MainMenuePanel", "Vechile setup wizzard", None))
        self.button_vehicle_setup.setText(_translate("MainMenuePanel", "Setup", None))
        self.button_vehicle_configuration.setToolTip(_translate("MainMenuePanel", "Vehicle configuration", None))
        self.button_vehicle_configuration.setStatusTip(_translate("MainMenuePanel", "Vehicle configuration", None))
        self.button_vehicle_configuration.setText(_translate("MainMenuePanel", "Config", None))
        self.button_vehicle_status.setToolTip(_translate("MainMenuePanel", "Vehicle status", None))
        self.button_vehicle_status.setStatusTip(_translate("MainMenuePanel", "Vehicle status", None))
        self.button_vehicle_status.setText(_translate("MainMenuePanel", "Status", None))

