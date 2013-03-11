# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuWindow.ui'
#
# Created: Mon Mar 04 15:47:23 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName(_fromUtf8("Menu"))
        Menu.resize(800, 600)
        self.formLayout = QtGui.QFormLayout(Menu)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setMargin(20)
        self.formLayout.setSpacing(20)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QtGui.QApplication.translate("Menu", "Form", None, QtGui.QApplication.UnicodeUTF8))

