# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MagnetometerCalibrationPanel.ui'
#
# Created: Tue Jun 11 19:53:37 2013
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

class Ui_MagnetometerCalibrationPanel(object):
    def setupUi(self, MagnetometerCalibrationPanel):
        MagnetometerCalibrationPanel.setObjectName(_fromUtf8("MagnetometerCalibrationPanel"))
        MagnetometerCalibrationPanel.resize(800, 600)
        self.start_button = QtGui.QPushButton(MagnetometerCalibrationPanel)
        self.start_button.setGeometry(QtCore.QRect(450, 420, 100, 31))
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.cancel_button = QtGui.QPushButton(MagnetometerCalibrationPanel)
        self.cancel_button.setGeometry(QtCore.QRect(560, 420, 101, 31))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.information_box = QtGui.QTextBrowser(MagnetometerCalibrationPanel)
        self.information_box.setGeometry(QtCore.QRect(450, 10, 341, 391))
        self.information_box.setFrameShadow(QtGui.QFrame.Sunken)
        self.information_box.setObjectName(_fromUtf8("information_box"))
        self.x_axis_progress_bar = QtGui.QProgressBar(MagnetometerCalibrationPanel)
        self.x_axis_progress_bar.setGeometry(QtCore.QRect(70, 10, 31, 421))
        self.x_axis_progress_bar.setMinimum(-800)
        self.x_axis_progress_bar.setMaximum(800)
        self.x_axis_progress_bar.setProperty("value", 0)
        self.x_axis_progress_bar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.x_axis_progress_bar.setTextVisible(True)
        self.x_axis_progress_bar.setOrientation(QtCore.Qt.Vertical)
        self.x_axis_progress_bar.setInvertedAppearance(False)
        self.x_axis_progress_bar.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.x_axis_progress_bar.setObjectName(_fromUtf8("x_axis_progress_bar"))
        self.y_axis_progress_bar = QtGui.QProgressBar(MagnetometerCalibrationPanel)
        self.y_axis_progress_bar.setGeometry(QtCore.QRect(200, 10, 31, 421))
        self.y_axis_progress_bar.setMinimum(-800)
        self.y_axis_progress_bar.setMaximum(800)
        self.y_axis_progress_bar.setProperty("value", 0)
        self.y_axis_progress_bar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.y_axis_progress_bar.setTextVisible(True)
        self.y_axis_progress_bar.setOrientation(QtCore.Qt.Vertical)
        self.y_axis_progress_bar.setInvertedAppearance(False)
        self.y_axis_progress_bar.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.y_axis_progress_bar.setObjectName(_fromUtf8("y_axis_progress_bar"))
        self.z_axis_progress_bar = QtGui.QProgressBar(MagnetometerCalibrationPanel)
        self.z_axis_progress_bar.setGeometry(QtCore.QRect(330, 10, 31, 421))
        self.z_axis_progress_bar.setMinimum(-800)
        self.z_axis_progress_bar.setMaximum(800)
        self.z_axis_progress_bar.setProperty("value", 0)
        self.z_axis_progress_bar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.z_axis_progress_bar.setTextVisible(True)
        self.z_axis_progress_bar.setOrientation(QtCore.Qt.Vertical)
        self.z_axis_progress_bar.setInvertedAppearance(False)
        self.z_axis_progress_bar.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.z_axis_progress_bar.setObjectName(_fromUtf8("z_axis_progress_bar"))
        self.label_x = QtGui.QLabel(MagnetometerCalibrationPanel)
        self.label_x.setGeometry(QtCore.QRect(70, 440, 46, 13))
        self.label_x.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_x.setObjectName(_fromUtf8("label_x"))
        self.label_y = QtGui.QLabel(MagnetometerCalibrationPanel)
        self.label_y.setGeometry(QtCore.QRect(200, 440, 46, 13))
        self.label_y.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_y.setObjectName(_fromUtf8("label_y"))
        self.label_z = QtGui.QLabel(MagnetometerCalibrationPanel)
        self.label_z.setGeometry(QtCore.QRect(330, 440, 46, 13))
        self.label_z.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_z.setObjectName(_fromUtf8("label_z"))

        self.retranslateUi(MagnetometerCalibrationPanel)
        QtCore.QMetaObject.connectSlotsByName(MagnetometerCalibrationPanel)

    def retranslateUi(self, MagnetometerCalibrationPanel):
        MagnetometerCalibrationPanel.setWindowTitle(_translate("MagnetometerCalibrationPanel", "Form", None))
        self.start_button.setText(_translate("MagnetometerCalibrationPanel", "Start", None))
        self.cancel_button.setText(_translate("MagnetometerCalibrationPanel", "Cancel", None))
        self.information_box.setHtml(_translate("MagnetometerCalibrationPanel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1) Press start to start the calibration.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2) Move the AeroQuad in all directions serval times, x y and z axis.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3) When done press finish to save the calibration.</span></p></body></html>", None))
        self.x_axis_progress_bar.setFormat(_translate("MagnetometerCalibrationPanel", "%p%", None))
        self.y_axis_progress_bar.setFormat(_translate("MagnetometerCalibrationPanel", "%p%", None))
        self.z_axis_progress_bar.setFormat(_translate("MagnetometerCalibrationPanel", "%p%", None))
        self.label_x.setText(_translate("MagnetometerCalibrationPanel", "0", None))
        self.label_y.setText(_translate("MagnetometerCalibrationPanel", "0", None))
        self.label_z.setText(_translate("MagnetometerCalibrationPanel", "0", None))

