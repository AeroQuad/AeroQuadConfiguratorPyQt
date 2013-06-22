# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PIDTuningPanel.ui'
#
# Created: Sat Jun 22 10:25:49 2013
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

class Ui_PIDTuningPanel(object):
    def setupUi(self, PIDTuningPanel):
        PIDTuningPanel.setObjectName(_fromUtf8("PIDTuningPanel"))
        PIDTuningPanel.resize(516, 437)
        self.gridLayout = QtGui.QGridLayout(PIDTuningPanel)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.main_layout = QtGui.QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(_fromUtf8("main_layout"))
        self.gridLayout.addLayout(self.main_layout, 2, 0, 1, 1)
        self.linked_check_box = QtGui.QCheckBox(PIDTuningPanel)
        self.linked_check_box.setObjectName(_fromUtf8("linked_check_box"))
        self.gridLayout.addWidget(self.linked_check_box, 0, 0, 1, 1)
        self.header_layout = QtGui.QHBoxLayout()
        self.header_layout.setSpacing(0)
        self.header_layout.setObjectName(_fromUtf8("header_layout"))
        self.header_name_label = QtGui.QLabel(PIDTuningPanel)
        self.header_name_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.header_name_label.setObjectName(_fromUtf8("header_name_label"))
        self.header_layout.addWidget(self.header_name_label)
        self.user_values_title_label = QtGui.QLabel(PIDTuningPanel)
        self.user_values_title_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.user_values_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.user_values_title_label.setObjectName(_fromUtf8("user_values_title_label"))
        self.header_layout.addWidget(self.user_values_title_label)
        self.default_value_title_label = QtGui.QLabel(PIDTuningPanel)
        self.default_value_title_label.setMinimumSize(QtCore.QSize(50, 0))
        self.default_value_title_label.setMaximumSize(QtCore.QSize(50, 25))
        self.default_value_title_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.default_value_title_label.setObjectName(_fromUtf8("default_value_title_label"))
        self.header_layout.addWidget(self.default_value_title_label)
        self.gridLayout.addLayout(self.header_layout, 1, 0, 1, 1)

        self.retranslateUi(PIDTuningPanel)
        QtCore.QMetaObject.connectSlotsByName(PIDTuningPanel)

    def retranslateUi(self, PIDTuningPanel):
        PIDTuningPanel.setWindowTitle(_translate("PIDTuningPanel", "Update Parameter", None))
        self.linked_check_box.setText(_translate("PIDTuningPanel", "Linked", None))
        self.header_name_label.setText(_translate("PIDTuningPanel", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Name</span></p></body></html>", None))
        self.user_values_title_label.setText(_translate("PIDTuningPanel", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Users values</span></p></body></html>", None))
        self.default_value_title_label.setText(_translate("PIDTuningPanel", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Default</span></p></body></html>", None))

