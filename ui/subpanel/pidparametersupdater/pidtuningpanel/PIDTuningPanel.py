# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PIDTuningPanel.ui'
#
# Created: Sat Sep 07 15:13:14 2013
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
        PIDTuningPanel.resize(792, 459)
        self.gridLayout = QtGui.QGridLayout(PIDTuningPanel)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.main_layout = QtGui.QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(_fromUtf8("main_layout"))
        self.gridLayout.addLayout(self.main_layout, 0, 0, 1, 1)

        self.retranslateUi(PIDTuningPanel)
        QtCore.QMetaObject.connectSlotsByName(PIDTuningPanel)

    def retranslateUi(self, PIDTuningPanel):
        PIDTuningPanel.setWindowTitle(_translate("PIDTuningPanel", "Update Parameter", None))

