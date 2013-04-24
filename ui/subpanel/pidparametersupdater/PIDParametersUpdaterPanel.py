# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PIDParametersUpdaterPanel.ui'
#
# Created: Wed Apr 24 17:20:14 2013
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

class Ui_PIDParametersUpdaterPanel(object):
    def setupUi(self, PIDParametersUpdaterPanel):
        PIDParametersUpdaterPanel.setObjectName(_fromUtf8("PIDParametersUpdaterPanel"))
        PIDParametersUpdaterPanel.resize(588, 374)
        self.gridLayout = QtGui.QGridLayout(PIDParametersUpdaterPanel)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonUpload = QtGui.QPushButton(PIDParametersUpdaterPanel)
        self.buttonUpload.setObjectName(_fromUtf8("buttonUpload"))
        self.gridLayout.addWidget(self.buttonUpload, 2, 5, 1, 1)
        self.listParameterType = QtGui.QListWidget(PIDParametersUpdaterPanel)
        self.listParameterType.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listParameterType.setAlternatingRowColors(False)
        self.listParameterType.setResizeMode(QtGui.QListView.Adjust)
        self.listParameterType.setObjectName(_fromUtf8("listParameterType"))
        self.gridLayout.addWidget(self.listParameterType, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        self.parameterTable = QtGui.QTableWidget(PIDParametersUpdaterPanel)
        self.parameterTable.setStyleSheet(_fromUtf8(""))
        self.parameterTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.parameterTable.setAlternatingRowColors(True)
        self.parameterTable.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.parameterTable.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.parameterTable.setObjectName(_fromUtf8("parameterTable"))
        self.parameterTable.setColumnCount(3)
        self.parameterTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.parameterTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.parameterTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.parameterTable.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.parameterTable, 0, 1, 1, 5)
        self.buttonSave = QtGui.QPushButton(PIDParametersUpdaterPanel)
        self.buttonSave.setObjectName(_fromUtf8("buttonSave"))
        self.gridLayout.addWidget(self.buttonSave, 2, 4, 1, 1)
        self.buttonLoad = QtGui.QPushButton(PIDParametersUpdaterPanel)
        self.buttonLoad.setObjectName(_fromUtf8("buttonLoad"))
        self.gridLayout.addWidget(self.buttonLoad, 2, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)

        self.retranslateUi(PIDParametersUpdaterPanel)
        QtCore.QMetaObject.connectSlotsByName(PIDParametersUpdaterPanel)

    def retranslateUi(self, PIDParametersUpdaterPanel):
        PIDParametersUpdaterPanel.setWindowTitle(_translate("PIDParametersUpdaterPanel", "Update Parameter", None))
        self.buttonUpload.setText(_translate("PIDParametersUpdaterPanel", "Upload", None))
        item = self.parameterTable.horizontalHeaderItem(0)
        item.setText(_translate("PIDParametersUpdaterPanel", "Parameter", None))
        item = self.parameterTable.horizontalHeaderItem(1)
        item.setText(_translate("PIDParametersUpdaterPanel", "Value", None))
        item = self.parameterTable.horizontalHeaderItem(2)
        item.setText(_translate("PIDParametersUpdaterPanel", "Description", None))
        self.buttonSave.setText(_translate("PIDParametersUpdaterPanel", "Save", None))
        self.buttonLoad.setText(_translate("PIDParametersUpdaterPanel", "Load", None))

