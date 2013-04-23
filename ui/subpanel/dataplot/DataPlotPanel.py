# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from pyqtgraph import PlotWidget, setConfigOption

setConfigOption('background', (255,255,255))
setConfigOption('antialias',  True)
setConfigOption('downsample', True)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class DataPlotPanel(object):
    def setupUi(self, plotWindow):
        plotWindow.setObjectName(_fromUtf8("DataPlotPanel"))
        plotWindow.resize(540, 350)
        plotWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.gridLayout = QtGui.QGridLayout(plotWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))


        self.graphicsView = PlotWidget(plotWindow)

        self.graphicsView.hideButtons()
        self.graphicsView.showGrid(True, True)
        self.graphicsView.setMenuEnabled(False)
        self.graphicsView.setMouseEnabled(False, False)

        self.graphicsView.setFrameShadow(QtGui.QFrame.Plain)
        self.graphicsView.setFrameShape(QtGui.QFrame.StyledPanel)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 1)


        self.treeWidget = QtGui.QTreeWidget(plotWindow)
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

        self.retranslateUi(plotWindow)
        QtCore.QMetaObject.connectSlotsByName(plotWindow)

    def retranslateUi(self, plotWindow):
        plotWindow.setWindowTitle(QtGui.QApplication.translate("plotWindow", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("plotWindow", "Legend", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("plotWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("plotWindow", "Value", None, QtGui.QApplication.UnicodeUTF8))

