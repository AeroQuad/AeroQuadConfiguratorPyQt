# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataPlotPanel.ui'
#
# Created: Wed Apr 24 17:15:54 2013
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

class Ui_DataPlotPanel(object):
    def setupUi(self, DataPlotPanel):
        DataPlotPanel.setObjectName(_fromUtf8("DataPlotPanel"))
        DataPlotPanel.resize(540, 350)
        DataPlotPanel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout = QtGui.QGridLayout(DataPlotPanel)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = PlotWidget(DataPlotPanel)
        self.graphicsView.setFrameShape(QtGui.QFrame.StyledPanel)
        self.graphicsView.setFrameShadow(QtGui.QFrame.Plain)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 1)
        self.treeWidget = QtGui.QTreeWidget(DataPlotPanel)
        self.treeWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setItemsExpandable(False)
        self.treeWidget.setExpandsOnDoubleClick(False)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setDefaultSectionSize(80)
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.retranslateUi(DataPlotPanel)
        QtCore.QMetaObject.connectSlotsByName(DataPlotPanel)

    def retranslateUi(self, DataPlotPanel):
        DataPlotPanel.setWindowTitle(_translate("DataPlotPanel", "Form", None))
        self.treeWidget.headerItem().setText(0, _translate("DataPlotPanel", "Legend", None))
        self.treeWidget.headerItem().setText(1, _translate("DataPlotPanel", "Name", None))
        self.treeWidget.headerItem().setText(2, _translate("DataPlotPanel", "Value", None))

from pyqtgraph import PlotWidget
