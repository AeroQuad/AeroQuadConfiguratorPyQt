
from PyQt4 import QtGui
from ui.subpanel.dataplot.DataPlotController import DataPlotController
from graphicsItems.PlotCurveItem import PlotCurveItem
from ui.UIEventDispatcher import UIEventDispatcher
from model.VehicleEventDispatcher import VehicleEventDispatcher

class SensorsDataPlotContoller(DataPlotController):

    def __init__(self, vehicle_event_dispatcher, ui_event_dispatcher):
        DataPlotController.__init__(self)
        
        self.ui.plot_view.setRange(xRange=(0, 128), padding=0.0)
        self.ui.plot_view.clear()
        self.ui.tree_widget.clear()
        self._plot_index = 0
        
        self.data, self.curves, colors = [], [], [
            QtGui.QColor('blue'),
            QtGui.QColor('red'),
            QtGui.QColor('lime'),
            QtGui.QColor('cornflowerblue'),
            QtGui.QColor('greenyellow'),
            QtGui.QColor('violet'),
            QtGui.QColor('orange'),
            QtGui.QColor('deepskyblue'),
            QtGui.QColor('firebrick'),
            QtGui.QColor('aqua')]
        
        self.gyro_parent = QtGui.QTreeWidgetItem(self.ui.tree_widget)
        self.gyro_parent.setCheckState(0, 2)
        self.gyro_parent.setText(0, 'Gyro')
        self.gyro_parent.addChild (self.createPlotLine(0, colors[0], 'Gyro X Axis'))
        self.gyro_parent.addChild (self.createPlotLine(1, colors[1], 'Gyro Y Axis'))
        self.gyro_parent.addChild (self.createPlotLine(2, colors[2], 'Gyro Z Axis'))
        self.ui.tree_widget.expandItem(self.gyro_parent)
        
        self.accel_parent = QtGui.QTreeWidgetItem(self.ui.tree_widget)
        self.accel_parent.setCheckState(0, 2)
        self.accel_parent.setText(0, 'Accel')
        self.accel_parent.addChild (self.createPlotLine(3, colors[3], 'Accel X Axis'))
        self.accel_parent.addChild (self.createPlotLine(4, colors[4], 'Accel Y Axis'))
        self.accel_parent.addChild (self.createPlotLine(5, colors[5], 'Accel Z Axis'))
        self.ui.tree_widget.expandItem(self.accel_parent)
        
        ui_event_dispatcher.register(self._protocol_handler_changed_event, UIEventDispatcher.PROTOCOL_HANDLER_EVENT)
        vehicle_event_dispatcher.register(self._gyro_raw_data_receved, VehicleEventDispatcher.GYRO_RAW_DATA_EVENT)
        vehicle_event_dispatcher.register(self._accel_raw_data_receved, VehicleEventDispatcher.ACCEL_RAW_DATA_EVENT)
        vehicle_event_dispatcher.register(self._mag_raw_data_receved, VehicleEventDispatcher.MAGNETOMETER_RAW_DATA_EVENT)

    def createPlotLine(self, idx, color, plotName):
        self.data.append([0.0] * 128)
        self.curves.append(
            PlotCurveItem(self.data[idx], pen={'color':color, 'width': 2})
        )
        self.ui.plot_view.addItem(self.curves[idx])

        newLine = QtGui.QTreeWidgetItem()
        newLine.setCheckState(0, 2)
        newLine.setBackgroundColor(0, color)
        newLine.setText(1, plotName + '   ')
        newLine.setText(2, '0.000')
        return newLine
        
    def _protocol_handler_changed_event(self, event, protocol_handler):
        self._protocol_handler = protocol_handler;
                
    def start(self):
#        self.ui.plot_view.clear()
        self._protocol_handler.subscribe_sensors_data();
        
    def stop(self):
        self._protocol_handler.unsubscribe_command()
        
    def _gyro_raw_data_receved(self, event, gyro_vector):
        if self.gyro_parent.checkState(0) != 2:
            for i in range(0, 3):
                if self.curves[i] in self.ui.plot_view.items():
#                self.data[i].insert(0, 0.0)
#                self.curves[i].setData(self.data[i])
                    self.ui.plot_view.removeItem(self.curves[i])
            return
        
        gyro_data_array = [gyro_vector.get_x(),gyro_vector.get_y(),gyro_vector.get_z()]
        for i in range(0, 3):
            gyro_child_node = self.gyro_parent.child(i)
            if gyro_child_node.checkState(0) == 2:
                self.data[i].insert(0, float(gyro_data_array[i]))
                self.data[i].pop()
                gyro_child_node.setText(2, gyro_data_array[i])
                self.curves[i].setData(self.data[i])
                if self.curves[i] not in self.ui.plot_view.items():
                    self.ui.plot_view.addItem(self.curves[i])
            elif self.curves[i] in self.ui.plot_view.items():
#                self.data[i].insert(0, 0.0)
#                self.curves[i].setData(self.data[i])
                self.ui.plot_view.removeItem(self.curves[i])
        self.ui.plot_view.autoRange()
        
    def _accel_raw_data_receved(self, event, accel_vector):
        if self.accel_parent.checkState(0) != 2:
            for i in range(0, 3):
                if self.curves[i+3] in self.ui.plot_view.items():
#                self.data[i].insert(0, 0.0)
#                self.curves[i].setData(self.data[i])
                    self.ui.plot_view.removeItem(self.curves[i+3])
            return

        accel_data_array = [accel_vector.get_x(),accel_vector.get_y(),accel_vector.get_z()]
        for i in range(0, 3):
            accel_child_node = self.accel_parent.child(i)
            if accel_child_node.checkState(0) == 2:
                self.data[i+3].insert(0, float(accel_data_array[i]))
                self.data[i+3].pop()
                accel_child_node.setText(2, accel_data_array[i])
                self.curves[i+3].setData(self.data[i])
                if self.curves[i+3] not in self.ui.plot_view.items():
                    self.ui.plot_view.addItem(self.curves[i+3])
            elif self.curves[i] in self.ui.plot_view.items():
#                self.data[i].insert(0, 0.0)
#                self.curves[i].setData(self.data[i])
                self.ui.plot_view.removeItem(self.curves[i+3])
        self.ui.plot_view.autoRange()

        
    def _mag_raw_data_receved(self, event, mag_vector):
        return
        if self.mag_parent.checkState(0) != 2:
            for i in range(0, 3):
                if self.curves[i+3] in self.ui.plot_view.items():
#                self.data[i].insert(0, 0.0)
#                self.curves[i].setData(self.data[i])
                    self.ui.plot_view.removeItem(self.curves[i+3])
            return

        mag_data_array = [mag_vector.get_x(),mag_vector.get_y(),mag_vector.get_z()]
        for i in range(0, 3):
            accel_child_node = self.mag_parent.child(i)
            if accel_child_node.checkState(0) == 2:
                self.data[i+6].insert(0, float(mag_data_array[i]))
                self.data[i+6].pop()
                accel_child_node.setText(2, mag_data_array[i])
                self.curves[i+6].setData(self.data[i])
                if self.curves[i+6] not in self.ui.plot_view.items():
                    self.ui.plot_view.addItem(self.curves[i+6])
            elif self.curves[i] in self.ui.plot_view.items():
#                self.data[i].insert(0, 0.0)
#                self.curves[i].setData(self.data[i])
                self.ui.plot_view.removeItem(self.curves[i+6])
        self.ui.plot_view.autoRange()










#        self.treeWidget = QtGui.QTreeWidget(DataPlotPanel)
#        self.treeWidget.setMaximumSize(QtCore.QSize(200, 16777215))
#        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
#        self.treeWidget.setRootIsDecorated(True)
#        self.treeWidget.setItemsExpandable(True)
#        self.treeWidget.setExpandsOnDoubleClick(False)
#        self.treeWidget.setColumnCount(3)
#        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
#        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
#        item_0.setCheckState(0, QtCore.Qt.Checked)
#        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
#        item_1 = QtGui.QTreeWidgetItem(item_0)
#        item_1.setCheckState(0, QtCore.Qt.Checked)
#        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
#        item_1 = QtGui.QTreeWidgetItem(item_0)
#        item_1.setCheckState(0, QtCore.Qt.Checked)
#        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
#        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
#        item_1 = QtGui.QTreeWidgetItem(item_0)
#        item_1 = QtGui.QTreeWidgetItem(item_0)        


#        DataPlotPanel.setWindowTitle(_translate("DataPlotPanel", "Form", None))
#        self.treeWidget.headerItem().setText(0, _translate("DataPlotPanel", "Legend", None))
#        self.treeWidget.headerItem().setText(1, _translate("DataPlotPanel", "Name", None))
#        self.treeWidget.headerItem().setText(2, _translate("DataPlotPanel", "Value", None))
#        __sortingEnabled = self.treeWidget.isSortingEnabled()
#        self.treeWidget.setSortingEnabled(False)
#        self.treeWidget.topLevelItem(0).setText(0, _translate("DataPlotPanel", "Gyro", None))
#        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("DataPlotPanel", "Gyro X", None))
#        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("DataPlotPanel", "Gyro Y", None))
#        self.treeWidget.topLevelItem(1).setText(0, _translate("DataPlotPanel", "Accel", None))
#        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("DataPlotPanel", "Accel X", None))
#        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("DataPlotPanel", "Accel Y", None))
#        self.treeWidget.setSortingEnabled(__sortingEnabled)
