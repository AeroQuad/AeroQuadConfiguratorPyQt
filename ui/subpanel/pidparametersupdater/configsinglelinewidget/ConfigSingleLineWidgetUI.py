# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfigSingleLineWidgetUI.ui'
#
# Created: Thu Jun 20 20:32:37 2013
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

class Ui_PIDSingleLineWidget(object):
    def setupUi(self, PIDSingleLineWidget):
        PIDSingleLineWidget.setObjectName(_fromUtf8("PIDSingleLineWidget"))
        PIDSingleLineWidget.resize(250, 71)
        self.gridLayout = QtGui.QGridLayout(PIDSingleLineWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridWidget = QtGui.QWidget(PIDSingleLineWidget)
        self.gridWidget.setObjectName(_fromUtf8("gridWidget"))
        self.pid_layout = QtGui.QGridLayout(self.gridWidget)
        self.pid_layout.setMargin(0)
        self.pid_layout.setObjectName(_fromUtf8("pid_layout"))
        self.slider = QtGui.QSlider(self.gridWidget)
        self.slider.setMaximumSize(QtCore.QSize(16777215, 35))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName(_fromUtf8("slider"))
        self.pid_layout.addWidget(self.slider, 0, 1, 1, 1)
        self.edit_box = QtGui.QTextEdit(self.gridWidget)
        self.edit_box.setMaximumSize(QtCore.QSize(50, 35))
        self.edit_box.setObjectName(_fromUtf8("edit_box"))
        self.pid_layout.addWidget(self.edit_box, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.gridWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.pid_layout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.gridWidget, 0, 0, 1, 1)

        self.retranslateUi(PIDSingleLineWidget)
        QtCore.QMetaObject.connectSlotsByName(PIDSingleLineWidget)

    def retranslateUi(self, PIDSingleLineWidget):
        PIDSingleLineWidget.setWindowTitle(_translate("PIDSingleLineWidget", "Update Parameter", None))
        self.label.setText(_translate("PIDSingleLineWidget", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">P</span></p></body></html>", None))

