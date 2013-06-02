# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AccelCalibrationPanel.ui'
#
# Created: Sun Jun 02 13:32:11 2013
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

class Ui_AccelCalibrationPanel(object):
    def setupUi(self, AccelCalibrationPanel):
        AccelCalibrationPanel.setObjectName(_fromUtf8("AccelCalibrationPanel"))
        AccelCalibrationPanel.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AccelCalibrationPanel.sizePolicy().hasHeightForWidth())
        AccelCalibrationPanel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(False)
        AccelCalibrationPanel.setFont(font)
        self.cancel_button = QtGui.QPushButton(AccelCalibrationPanel)
        self.cancel_button.setGeometry(QtCore.QRect(530, 410, 101, 31))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.information_display_text_box = QtGui.QTextBrowser(AccelCalibrationPanel)
        self.information_display_text_box.setGeometry(QtCore.QRect(410, 10, 341, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.information_display_text_box.setFont(font)
        self.information_display_text_box.setFrameShadow(QtGui.QFrame.Sunken)
        self.information_display_text_box.setObjectName(_fromUtf8("information_display_text_box"))
        self.start_button = QtGui.QPushButton(AccelCalibrationPanel)
        self.start_button.setGeometry(QtCore.QRect(420, 410, 100, 31))
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.picture_container = QtGui.QGraphicsView(AccelCalibrationPanel)
        self.picture_container.setGeometry(QtCore.QRect(10, 10, 391, 391))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.picture_container.sizePolicy().hasHeightForWidth())
        self.picture_container.setSizePolicy(sizePolicy)
        self.picture_container.setMinimumSize(QtCore.QSize(391, 391))
        self.picture_container.setMaximumSize(QtCore.QSize(391, 391))
        font = QtGui.QFont()
        font.setKerning(True)
        self.picture_container.setFont(font)
        self.picture_container.setAcceptDrops(False)
        self.picture_container.setFrameShape(QtGui.QFrame.NoFrame)
        self.picture_container.setFrameShadow(QtGui.QFrame.Plain)
        self.picture_container.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.picture_container.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.picture_container.setObjectName(_fromUtf8("picture_container"))
        self.progress_bar = QtGui.QProgressBar(AccelCalibrationPanel)
        self.progress_bar.setGeometry(QtCore.QRect(10, 420, 401, 23))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))

        self.retranslateUi(AccelCalibrationPanel)
        QtCore.QMetaObject.connectSlotsByName(AccelCalibrationPanel)

    def retranslateUi(self, AccelCalibrationPanel):
        AccelCalibrationPanel.setWindowTitle(_translate("AccelCalibrationPanel", "RC channel setup", None))
        self.cancel_button.setText(_translate("AccelCalibrationPanel", "Cancel", None))
        self.information_display_text_box.setHtml(_translate("AccelCalibrationPanel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
        self.start_button.setText(_translate("AccelCalibrationPanel", "Start", None))

