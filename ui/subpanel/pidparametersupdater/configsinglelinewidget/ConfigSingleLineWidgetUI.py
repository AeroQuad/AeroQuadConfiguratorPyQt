# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfigSingleLineWidgetUI.ui'
#
# Created: Sat Sep 07 12:00:37 2013
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
        PIDSingleLineWidget.resize(499, 71)
        self.gridLayout = QtGui.QGridLayout(PIDSingleLineWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridWidget = QtGui.QWidget(PIDSingleLineWidget)
        self.gridWidget.setObjectName(_fromUtf8("gridWidget"))
        self.pid_layout = QtGui.QGridLayout(self.gridWidget)
        self.pid_layout.setMargin(0)
        self.pid_layout.setObjectName(_fromUtf8("pid_layout"))
        self.title_label = QtGui.QLabel(self.gridWidget)
        self.title_label.setMinimumSize(QtCore.QSize(200, 25))
        self.title_label.setMaximumSize(QtCore.QSize(200, 25))
        self.title_label.setMidLineWidth(0)
        self.title_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.title_label.setObjectName(_fromUtf8("title_label"))
        self.pid_layout.addWidget(self.title_label, 0, 0, 1, 1)
        self.slider = QtGui.QSlider(self.gridWidget)
        self.slider.setMinimumSize(QtCore.QSize(0, 25))
        self.slider.setMaximumSize(QtCore.QSize(16777215, 25))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setTickInterval(5)
        self.slider.setObjectName(_fromUtf8("slider"))
        self.pid_layout.addWidget(self.slider, 0, 1, 1, 1)
        self.default_label = QtGui.QLabel(self.gridWidget)
        self.default_label.setMinimumSize(QtCore.QSize(50, 25))
        self.default_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.default_label.setObjectName(_fromUtf8("default_label"))
        self.pid_layout.addWidget(self.default_label, 0, 3, 1, 1)
        self.edit_box = QtGui.QDoubleSpinBox(self.gridWidget)
        self.edit_box.setStyleSheet(_fromUtf8(""))
        self.edit_box.setObjectName(_fromUtf8("edit_box"))
        self.pid_layout.addWidget(self.edit_box, 0, 2, 1, 1)
        self.sync_feedback_label = QtGui.QLabel(self.gridWidget)
        self.sync_feedback_label.setMinimumSize(QtCore.QSize(50, 0))
        self.sync_feedback_label.setText(_fromUtf8(""))
        self.sync_feedback_label.setObjectName(_fromUtf8("sync_feedback_label"))
        self.pid_layout.addWidget(self.sync_feedback_label, 0, 4, 1, 1)
        self.gridLayout.addWidget(self.gridWidget, 0, 0, 1, 1)

        self.retranslateUi(PIDSingleLineWidget)
        QtCore.QMetaObject.connectSlotsByName(PIDSingleLineWidget)

    def retranslateUi(self, PIDSingleLineWidget):
        PIDSingleLineWidget.setWindowTitle(_translate("PIDSingleLineWidget", "Update Parameter", None))
        self.title_label.setText(_translate("PIDSingleLineWidget", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">P</span></p></body></html>", None))
        self.default_label.setText(_translate("PIDSingleLineWidget", "Default", None))

