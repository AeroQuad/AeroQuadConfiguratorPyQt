# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReceiverChannelDetectionPanel.ui'
#
# Created: Wed Apr 24 17:26:04 2013
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

class Ui_ReceiverChannelDetectionPanel(object):
    def setupUi(self, ReceiverChannelDetectionPanel):
        ReceiverChannelDetectionPanel.setObjectName(_fromUtf8("ReceiverChannelDetectionPanel"))
        ReceiverChannelDetectionPanel.resize(800, 600)
        self.cancel = QtGui.QPushButton(ReceiverChannelDetectionPanel)
        self.cancel.setGeometry(QtCore.QRect(580, 500, 101, 31))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.label = QtGui.QLabel(ReceiverChannelDetectionPanel)
        self.label.setGeometry(QtCore.QRect(90, 10, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(ReceiverChannelDetectionPanel)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(ReceiverChannelDetectionPanel)
        self.label_3.setGeometry(QtCore.QRect(90, 90, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(ReceiverChannelDetectionPanel)
        self.label_4.setGeometry(QtCore.QRect(90, 130, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(ReceiverChannelDetectionPanel)
        self.label_5.setGeometry(QtCore.QRect(90, 170, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(ReceiverChannelDetectionPanel)
        self.label_6.setGeometry(QtCore.QRect(90, 210, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(ReceiverChannelDetectionPanel)
        self.label_7.setGeometry(QtCore.QRect(90, 250, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(False)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(ReceiverChannelDetectionPanel)
        self.label_8.setGeometry(QtCore.QRect(90, 290, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setScaledContents(False)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.commLog = QtGui.QTextBrowser(ReceiverChannelDetectionPanel)
        self.commLog.setGeometry(QtCore.QRect(450, 10, 341, 461))
        self.commLog.setFrameShadow(QtGui.QFrame.Sunken)
        self.commLog.setObjectName(_fromUtf8("commLog"))
        self.start = QtGui.QPushButton(ReceiverChannelDetectionPanel)
        self.start.setGeometry(QtCore.QRect(470, 500, 100, 31))
        self.start.setObjectName(_fromUtf8("start"))
        self.next = QtGui.QPushButton(ReceiverChannelDetectionPanel)
        self.next.setGeometry(QtCore.QRect(690, 500, 101, 31))
        self.next.setObjectName(_fromUtf8("next"))
        self.label_9 = QtGui.QLabel(ReceiverChannelDetectionPanel)
        self.label_9.setGeometry(QtCore.QRect(90, 330, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setScaledContents(False)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(ReceiverChannelDetectionPanel)
        self.label_10.setGeometry(QtCore.QRect(90, 370, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setScaledContents(False)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(ReceiverChannelDetectionPanel)
        self.label_11.setGeometry(QtCore.QRect(90, 410, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setScaledContents(False)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(ReceiverChannelDetectionPanel)
        self.label_12.setGeometry(QtCore.QRect(90, 450, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setScaledContents(False)
        self.label_12.setObjectName(_fromUtf8("label_12"))

        self.retranslateUi(ReceiverChannelDetectionPanel)
        QtCore.QMetaObject.connectSlotsByName(ReceiverChannelDetectionPanel)

    def retranslateUi(self, ReceiverChannelDetectionPanel):
        ReceiverChannelDetectionPanel.setWindowTitle(_translate("ReceiverChannelDetectionPanel", "RC channel setup", None))
        self.cancel.setText(_translate("ReceiverChannelDetectionPanel", "Cancel", None))
        self.label.setText(_translate("ReceiverChannelDetectionPanel", "Roll", None))
        self.label_2.setText(_translate("ReceiverChannelDetectionPanel", "Pitch", None))
        self.label_3.setText(_translate("ReceiverChannelDetectionPanel", "Throttle", None))
        self.label_4.setText(_translate("ReceiverChannelDetectionPanel", "Yaw", None))
        self.label_5.setText(_translate("ReceiverChannelDetectionPanel", "Mode", None))
        self.label_6.setText(_translate("ReceiverChannelDetectionPanel", "Aux1", None))
        self.label_7.setText(_translate("ReceiverChannelDetectionPanel", "Aux2", None))
        self.label_8.setText(_translate("ReceiverChannelDetectionPanel", "Aux3", None))
        self.commLog.setHtml(_translate("ReceiverChannelDetectionPanel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1) Press start to start the RC channel assignment.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2) When detecting a channel move </span><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">one</span><span style=\" font-size:12pt;\"> channel at the time the program automaticly moves to the next channel.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3) When all channels are assigned the procedure automaticly stops.</span></p></body></html>", None))
        self.start.setText(_translate("ReceiverChannelDetectionPanel", "Start", None))
        self.next.setText(_translate("ReceiverChannelDetectionPanel", "Next", None))
        self.label_9.setText(_translate("ReceiverChannelDetectionPanel", "Aux4", None))
        self.label_10.setText(_translate("ReceiverChannelDetectionPanel", "Aux5", None))
        self.label_11.setText(_translate("ReceiverChannelDetectionPanel", "Aux6", None))
        self.label_12.setText(_translate("ReceiverChannelDetectionPanel", "Aux7", None))

