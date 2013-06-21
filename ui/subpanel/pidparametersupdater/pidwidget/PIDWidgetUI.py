# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PIDWidgetUI.ui'
#
# Created: Thu Jun 20 21:54:18 2013
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
        self.gridWidget = QtGui.QWidget(PIDWidget)
        self.gridWidget.setObjectName(_fromUtf8("gridWidget"))
        self.pid_layout = QtGui.QGridLayout(self.gridWidget)
        self.pid_layout.setMargin(0)
        self.pid_layout.setObjectName(_fromUtf8("pid_layout"))
        self.d_slider = QtGui.QSlider(self.gridWidget)
        self.d_slider.setMaximumSize(QtCore.QSize(16777215, 35))
        self.d_slider.setOrientation(QtCore.Qt.Horizontal)
        self.d_slider.setObjectName(_fromUtf8("d_slider"))
        self.pid_layout.addWidget(self.d_slider, 2, 1, 1, 1)
        self.i_label = QtGui.QLabel(self.gridWidget)
        self.i_label.setObjectName(_fromUtf8("i_label"))
        self.pid_layout.addWidget(self.i_label, 1, 0, 1, 1)
        self.d_label = QtGui.QLabel(self.gridWidget)
        self.d_label.setObjectName(_fromUtf8("d_label"))
        self.pid_layout.addWidget(self.d_label, 2, 0, 1, 1)
        self.i_slider = QtGui.QSlider(self.gridWidget)
        self.i_slider.setMaximumSize(QtCore.QSize(16777215, 35))
        self.i_slider.setOrientation(QtCore.Qt.Horizontal)
        self.i_slider.setObjectName(_fromUtf8("i_slider"))
        self.pid_layout.addWidget(self.i_slider, 1, 1, 1, 1)
        self.p_slider = QtGui.QSlider(self.gridWidget)
        self.p_slider.setMaximumSize(QtCore.QSize(16777215, 35))
        self.p_slider.setOrientation(QtCore.Qt.Horizontal)
        self.p_slider.setObjectName(_fromUtf8("p_slider"))
        self.pid_layout.addWidget(self.p_slider, 0, 1, 1, 1)
        self.p_label = QtGui.QLabel(self.gridWidget)
        self.p_label.setObjectName(_fromUtf8("p_label"))
        self.pid_layout.addWidget(self.p_label, 0, 0, 1, 1)
        self.p_edit_box = QtGui.QTextEdit(self.gridWidget)
        self.p_edit_box.setMaximumSize(QtCore.QSize(50, 35))
        self.p_edit_box.setObjectName(_fromUtf8("p_edit_box"))
        self.pid_layout.addWidget(self.p_edit_box, 0, 2, 1, 1)
        self.i_edit_box = QtGui.QTextEdit(self.gridWidget)
        self.i_edit_box.setMaximumSize(QtCore.QSize(50, 35))
        self.i_edit_box.setObjectName(_fromUtf8("i_edit_box"))
        self.pid_layout.addWidget(self.i_edit_box, 1, 2, 1, 1)
        self.d_edit_box = QtGui.QTextEdit(self.gridWidget)
        self.d_edit_box.setMaximumSize(QtCore.QSize(50, 35))
        self.d_edit_box.setObjectName(_fromUtf8("d_edit_box"))
        self.pid_layout.addWidget(self.d_edit_box, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.gridWidget, 0, 0, 1, 1)

        self.retranslateUi(PIDWidget)
        QtCore.QMetaObject.connectSlotsByName(PIDWidget)

    def retranslateUi(self, PIDWidget):
        PIDWidget.setWindowTitle(_translate("PIDWidget", "Update Parameter", None))
        self.i_label.setText(_translate("PIDWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">I</span></p></body></html>", None))
        self.d_label.setText(_translate("PIDWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">D</span></p></body></html>", None))
        self.p_label.setText(_translate("PIDWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">P</span></p></body></html>", None))

