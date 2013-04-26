# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MagnetometerCalibrationPanel.ui'
#
# Created: Fri Apr 26 13:35:03 2013
#      by: PyQt4 UI code generator 4.10
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
        self.progressBar_Xaxis = QtGui.QProgressBar(MagnetometerCalibrationPanel)
        self.progressBar_Xaxis.setGeometry(QtCore.QRect(70, 10, 31, 461))
        self.progressBar_Xaxis.setMinimum(-800)
        self.progressBar_Xaxis.setMaximum(800)
        self.progressBar_Xaxis.setProperty("value", 0)
        self.progressBar_Xaxis.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.progressBar_Xaxis.setTextVisible(False)
        self.progressBar_Xaxis.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_Xaxis.setInvertedAppearance(False)
        self.progressBar_Xaxis.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar_Xaxis.setObjectName(_fromUtf8("progressBar_Xaxis"))
        self.progressBar_Yaxis = QtGui.QProgressBar(MagnetometerCalibrationPanel)
        self.progressBar_Yaxis.setGeometry(QtCore.QRect(200, 10, 31, 461))
        self.progressBar_Yaxis.setMinimum(-800)
        self.progressBar_Yaxis.setMaximum(800)
        self.progressBar_Yaxis.setProperty("value", 0)
        self.progressBar_Yaxis.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.progressBar_Yaxis.setTextVisible(False)
        self.progressBar_Yaxis.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_Yaxis.setInvertedAppearance(False)
        self.progressBar_Yaxis.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar_Yaxis.setObjectName(_fromUtf8("progressBar_Yaxis"))
        self.progressBar_Zaxis = QtGui.QProgressBar(MagnetometerCalibrationPanel)
        self.progressBar_Zaxis.setGeometry(QtCore.QRect(330, 10, 31, 461))
        self.progressBar_Zaxis.setMinimum(-800)
        self.progressBar_Zaxis.setMaximum(800)
        self.progressBar_Zaxis.setProperty("value", 0)
        self.progressBar_Zaxis.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.progressBar_Zaxis.setTextVisible(False)
        self.progressBar_Zaxis.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_Zaxis.setInvertedAppearance(False)
        self.progressBar_Zaxis.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar_Zaxis.setObjectName(_fromUtf8("progressBar_Zaxis"))
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
        self.progressBar_Xaxis.setFormat(_translate("MagnetometerCalibrationPanel", "%p%", None))
        self.progressBar_Yaxis.setFormat(_translate("MagnetometerCalibrationPanel", "%p%", None))
        self.progressBar_Zaxis.setFormat(_translate("MagnetometerCalibrationPanel", "%p%", None))
        self.label_x.setText(_translate("MagnetometerCalibrationPanel", "0", None))
        self.label_y.setText(_translate("MagnetometerCalibrationPanel", "0", None))
        self.label_z.setText(_translate("MagnetometerCalibrationPanel", "0", None))

