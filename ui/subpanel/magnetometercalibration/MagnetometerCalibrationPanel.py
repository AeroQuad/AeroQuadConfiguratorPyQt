# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MagnetometerCalibrationPanel.ui'
#
# Created: Tue Apr 30 05:23:28 2013
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
        self.start = QtGui.QPushButton(MagnetometerCalibrationPanel)
        self.start.setGeometry(QtCore.QRect(450, 510, 100, 31))
        self.start.setObjectName(_fromUtf8("start"))
        self.cancel = QtGui.QPushButton(MagnetometerCalibrationPanel)
        self.cancel.setGeometry(QtCore.QRect(570, 510, 101, 31))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.next = QtGui.QPushButton(MagnetometerCalibrationPanel)
        self.next.setGeometry(QtCore.QRect(690, 510, 101, 31))
        self.next.setObjectName(_fromUtf8("next"))
        self.commLog = QtGui.QTextBrowser(MagnetometerCalibrationPanel)
        self.commLog.setGeometry(QtCore.QRect(450, 10, 341, 461))
        self.commLog.setFrameShadow(QtGui.QFrame.Sunken)
        self.commLog.setObjectName(_fromUtf8("commLog"))
        self.x_axis_progress_bar = QtGui.QProgressBar(MagnetometerCalibrationPanel)
        self.x_axis_progress_bar.setGeometry(QtCore.QRect(70, 10, 31, 461))
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
        self.y_axis_progress_bar.setGeometry(QtCore.QRect(200, 10, 31, 461))
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
        self.z_axis_progress_bar.setGeometry(QtCore.QRect(330, 10, 31, 461))
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
        self.label_x.setGeometry(QtCore.QRect(70, 480, 46, 13))
        self.label_x.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_x.setObjectName(_fromUtf8("label_x"))
        self.label_y = QtGui.QLabel(MagnetometerCalibrationPanel)
        self.label_y.setGeometry(QtCore.QRect(200, 480, 46, 13))
        self.label_y.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_y.setObjectName(_fromUtf8("label_y"))
        self.label_z = QtGui.QLabel(MagnetometerCalibrationPanel)
        self.label_z.setGeometry(QtCore.QRect(330, 480, 46, 13))
        self.label_z.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_z.setObjectName(_fromUtf8("label_z"))
        self._x_vertical_slider = QtGui.QSlider(MagnetometerCalibrationPanel)
        self._x_vertical_slider.setGeometry(QtCore.QRect(120, 19, 22, 451))
        self._x_vertical_slider.setMinimum(-800)
        self._x_vertical_slider.setMaximum(800)
        self._x_vertical_slider.setPageStep(1)
        self._x_vertical_slider.setOrientation(QtCore.Qt.Vertical)
        self._x_vertical_slider.setObjectName(_fromUtf8("_x_vertical_slider"))
        self._y_vertical_slider_2 = QtGui.QSlider(MagnetometerCalibrationPanel)
        self._y_vertical_slider_2.setGeometry(QtCore.QRect(250, 20, 22, 451))
        self._y_vertical_slider_2.setMinimum(-800)
        self._y_vertical_slider_2.setMaximum(800)
        self._y_vertical_slider_2.setPageStep(1)
        self._y_vertical_slider_2.setOrientation(QtCore.Qt.Vertical)
        self._y_vertical_slider_2.setObjectName(_fromUtf8("_y_vertical_slider_2"))
        self._z_vertical_slider_3 = QtGui.QSlider(MagnetometerCalibrationPanel)
        self._z_vertical_slider_3.setGeometry(QtCore.QRect(380, 20, 22, 451))
        self._z_vertical_slider_3.setMinimum(-800)
        self._z_vertical_slider_3.setMaximum(800)
        self._z_vertical_slider_3.setPageStep(1)
        self._z_vertical_slider_3.setOrientation(QtCore.Qt.Vertical)
        self._z_vertical_slider_3.setObjectName(_fromUtf8("_z_vertical_slider_3"))

        self.retranslateUi(MagnetometerCalibrationPanel)
        QtCore.QMetaObject.connectSlotsByName(MagnetometerCalibrationPanel)

    def retranslateUi(self, MagnetometerCalibrationPanel):
        MagnetometerCalibrationPanel.setWindowTitle(_translate("MagnetometerCalibrationPanel", "Form", None))
        self.start.setText(_translate("MagnetometerCalibrationPanel", "Start", None))
        self.cancel.setText(_translate("MagnetometerCalibrationPanel", "Cancel", None))
        self.next.setText(_translate("MagnetometerCalibrationPanel", "Next", None))
        self.commLog.setHtml(_translate("MagnetometerCalibrationPanel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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

