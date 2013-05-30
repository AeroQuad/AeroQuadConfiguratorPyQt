# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataPlotPanel.ui'
#
# Created: Wed May 29 18:17:05 2013
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
        self.plot_view = PlotWidget(DataPlotPanel)
        self.plot_view.setFrameShape(QtGui.QFrame.StyledPanel)
        self.plot_view.setFrameShadow(QtGui.QFrame.Plain)
        self.plot_view.setObjectName(_fromUtf8("plot_view"))
        self.gridLayout.addWidget(self.plot_view, 0, 1, 1, 1)
        self.tree_widget = QtGui.QTreeWidget(DataPlotPanel)
        self.tree_widget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.tree_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tree_widget.setRootIsDecorated(True)
        self.tree_widget.setItemsExpandable(True)
        self.tree_widget.setExpandsOnDoubleClick(False)
        self.tree_widget.setColumnCount(3)
        self.tree_widget.setObjectName(_fromUtf8("tree_widget"))
        self.tree_widget.header().setVisible(True)
        self.tree_widget.header().setDefaultSectionSize(80)
        self.gridLayout.addWidget(self.tree_widget, 0, 0, 1, 1)

        self.retranslateUi(DataPlotPanel)
        QtCore.QMetaObject.connectSlotsByName(DataPlotPanel)

    def retranslateUi(self, DataPlotPanel):
        DataPlotPanel.setWindowTitle(_translate("DataPlotPanel", "Form", None))
        self.tree_widget.headerItem().setText(0, _translate("DataPlotPanel", "Legend", None))
        self.tree_widget.headerItem().setText(1, _translate("DataPlotPanel", "Name", None))
        self.tree_widget.headerItem().setText(2, _translate("DataPlotPanel", "Value", None))

from pyqtgraph import PlotWidget
