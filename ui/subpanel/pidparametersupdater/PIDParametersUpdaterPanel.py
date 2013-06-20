# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PIDParametersUpdaterPanel.ui'
#
# Created: Sun Jun 16 08:02:31 2013
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

class Ui_PIDParametersUpdaterPanel(object):
    def setupUi(self, PIDParametersUpdaterPanel):
        PIDParametersUpdaterPanel.setObjectName(_fromUtf8("PIDParametersUpdaterPanel"))
        PIDParametersUpdaterPanel.resize(842, 528)
        self.gridLayout = QtGui.QGridLayout(PIDParametersUpdaterPanel)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.synchronize_button = QtGui.QPushButton(PIDParametersUpdaterPanel)
        self.synchronize_button.setObjectName(_fromUtf8("synchronize_button"))
        self.gridLayout.addWidget(self.synchronize_button, 4, 0, 1, 1)
        self.panel_container = QtGui.QStackedWidget(PIDParametersUpdaterPanel)
        self.panel_container.setMinimumSize(QtCore.QSize(0, 475))
        self.panel_container.setObjectName(_fromUtf8("panel_container"))
        self.gridLayout.addWidget(self.panel_container, 1, 1, 4, 1)
        self.save_button = QtGui.QPushButton(PIDParametersUpdaterPanel)
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.gridLayout.addWidget(self.save_button, 3, 0, 1, 1)
        self.default_button = QtGui.QPushButton(PIDParametersUpdaterPanel)
        self.default_button.setObjectName(_fromUtf8("default_button"))
        self.gridLayout.addWidget(self.default_button, 2, 0, 1, 1)
        self.pid_type_list = QtGui.QListWidget(PIDParametersUpdaterPanel)
        self.pid_type_list.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pid_type_list.setAlternatingRowColors(False)
        self.pid_type_list.setResizeMode(QtGui.QListView.Adjust)
        self.pid_type_list.setObjectName(_fromUtf8("pid_type_list"))
        self.gridLayout.addWidget(self.pid_type_list, 0, 0, 2, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.beginner_radio_button = QtGui.QRadioButton(PIDParametersUpdaterPanel)
        self.beginner_radio_button.setObjectName(_fromUtf8("beginner_radio_button"))
        self.buttonGroup = QtGui.QButtonGroup(PIDParametersUpdaterPanel)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.beginner_radio_button)
        self.horizontalLayout.addWidget(self.beginner_radio_button)
        self.intermediate_radio_button = QtGui.QRadioButton(PIDParametersUpdaterPanel)
        self.intermediate_radio_button.setObjectName(_fromUtf8("intermediate_radio_button"))
        self.buttonGroup.addButton(self.intermediate_radio_button)
        self.horizontalLayout.addWidget(self.intermediate_radio_button)
        self.advance_radiobutton = QtGui.QRadioButton(PIDParametersUpdaterPanel)
        self.advance_radiobutton.setObjectName(_fromUtf8("advance_radiobutton"))
        self.buttonGroup.addButton(self.advance_radiobutton)
        self.horizontalLayout.addWidget(self.advance_radiobutton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.retranslateUi(PIDParametersUpdaterPanel)
        QtCore.QMetaObject.connectSlotsByName(PIDParametersUpdaterPanel)

    def retranslateUi(self, PIDParametersUpdaterPanel):
        PIDParametersUpdaterPanel.setWindowTitle(_translate("PIDParametersUpdaterPanel", "Update Parameter", None))
        self.synchronize_button.setText(_translate("PIDParametersUpdaterPanel", "Synchronize", None))
        self.save_button.setText(_translate("PIDParametersUpdaterPanel", "Save", None))
        self.default_button.setText(_translate("PIDParametersUpdaterPanel", "Default", None))
        self.beginner_radio_button.setText(_translate("PIDParametersUpdaterPanel", "Beginner", None))
        self.intermediate_radio_button.setText(_translate("PIDParametersUpdaterPanel", "Intermediate", None))
        self.advance_radiobutton.setText(_translate("PIDParametersUpdaterPanel", "Advance", None))

