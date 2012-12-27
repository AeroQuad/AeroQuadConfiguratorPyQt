# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateParametersWindow.ui'
#
# Created: Thu Dec 27 01:32:47 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_parameterUpdate(object):
    def setupUi(self, parameterUpdate):
        parameterUpdate.setObjectName(_fromUtf8("parameterUpdate"))
        parameterUpdate.resize(588, 374)
        self.gridLayout = QtGui.QGridLayout(parameterUpdate)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonUpload = QtGui.QPushButton(parameterUpdate)
        self.buttonUpload.setObjectName(_fromUtf8("buttonUpload"))
        self.gridLayout.addWidget(self.buttonUpload, 2, 5, 1, 1)
        self.listParameterType = QtGui.QListWidget(parameterUpdate)
        self.listParameterType.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listParameterType.setAlternatingRowColors(False)
        self.listParameterType.setResizeMode(QtGui.QListView.Adjust)
        self.listParameterType.setObjectName(_fromUtf8("listParameterType"))
        self.gridLayout.addWidget(self.listParameterType, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        self.parameterTable = QtGui.QTableWidget(parameterUpdate)
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
        self.buttonSave = QtGui.QPushButton(parameterUpdate)
        self.buttonSave.setObjectName(_fromUtf8("buttonSave"))
        self.gridLayout.addWidget(self.buttonSave, 2, 4, 1, 1)
        self.buttonLoad = QtGui.QPushButton(parameterUpdate)
        self.buttonLoad.setObjectName(_fromUtf8("buttonLoad"))
        self.gridLayout.addWidget(self.buttonLoad, 2, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)

        self.retranslateUi(parameterUpdate)
        QtCore.QMetaObject.connectSlotsByName(parameterUpdate)

    def retranslateUi(self, parameterUpdate):
        parameterUpdate.setWindowTitle(QtGui.QApplication.translate("parameterUpdate", "Update Parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUpload.setText(QtGui.QApplication.translate("parameterUpdate", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        item = self.parameterTable.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("parameterUpdate", "Parameter", None, QtGui.QApplication.UnicodeUTF8))
        item = self.parameterTable.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("parameterUpdate", "Value", None, QtGui.QApplication.UnicodeUTF8))
        item = self.parameterTable.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("parameterUpdate", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSave.setText(QtGui.QApplication.translate("parameterUpdate", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoad.setText(QtGui.QApplication.translate("parameterUpdate", "Load", None, QtGui.QApplication.UnicodeUTF8))

