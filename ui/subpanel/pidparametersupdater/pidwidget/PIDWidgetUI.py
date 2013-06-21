# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PIDWidgetUI.ui'
#
# Created: Fri Jun 21 05:29:07 2013
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

class Ui_PIDWidget(object):
    def setupUi(self, PIDWidget):
        PIDWidget.setObjectName(_fromUtf8("PIDWidget"))
        PIDWidget.resize(250, 153)
        self.gridLayout = QtGui.QGridLayout(PIDWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.main_layout = QtGui.QVBoxLayout()
        self.main_layout.setObjectName(_fromUtf8("main_layout"))
        self.gridLayout.addLayout(self.main_layout, 0, 0, 1, 1)

        self.retranslateUi(PIDWidget)
        QtCore.QMetaObject.connectSlotsByName(PIDWidget)

    def retranslateUi(self, PIDWidget):
        PIDWidget.setWindowTitle(_translate("PIDWidget", "Update Parameter", None))

