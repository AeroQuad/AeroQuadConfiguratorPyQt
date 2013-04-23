# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accelWindow.ui'
#
# Created: Mon Apr 22 17:07:10 2013
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

class ReceiverChannelDetectionPanel(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(False)
        Form.setFont(font)
        self.cancel = QtGui.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(580, 500, 101, 31))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.commLog = QtGui.QTextBrowser(Form)
        self.commLog.setGeometry(QtCore.QRect(450, 10, 341, 461))
        self.commLog.setFrameShadow(QtGui.QFrame.Sunken)
        self.commLog.setObjectName(_fromUtf8("commLog"))
        self.start = QtGui.QPushButton(Form)
        self.start.setGeometry(QtCore.QRect(470, 500, 100, 31))
        self.start.setObjectName(_fromUtf8("start"))
        self.next = QtGui.QPushButton(Form)
        self.next.setGeometry(QtCore.QRect(690, 500, 101, 31))
        self.next.setObjectName(_fromUtf8("next"))
        self.picture = QtGui.QGraphicsView(Form)
        self.picture.setGeometry(QtCore.QRect(10, 10, 391, 391))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.picture.sizePolicy().hasHeightForWidth())
        self.picture.setSizePolicy(sizePolicy)
        self.picture.setMinimumSize(QtCore.QSize(391, 391))
        self.picture.setMaximumSize(QtCore.QSize(391, 391))
        font = QtGui.QFont()
        font.setKerning(True)
        self.picture.setFont(font)
        self.picture.setAcceptDrops(False)
        self.picture.setFrameShape(QtGui.QFrame.NoFrame)
        self.picture.setFrameShadow(QtGui.QFrame.Plain)
        self.picture.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.picture.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.picture.setObjectName(_fromUtf8("picture"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "RC channel setup", None))
        self.cancel.setText(_translate("Form", "Cancel", None))
        self.commLog.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.start.setText(_translate("Form", "Start", None))
        self.next.setText(_translate("Form", "Next", None))

