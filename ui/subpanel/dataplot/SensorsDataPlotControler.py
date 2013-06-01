
from PyQt4 import QtGui
from ui.subpanel.dataplot.DataPlotPanel import Ui_DataPlotPanel
from ui.subpanel.BasePanelController import BasePanelController
from ui.UIEventDispatcher import UIEventDispatcher
from model.VehicleEventDispatcher import VehicleEventDispatcher
from pyqtgraph.graphicsItems.PlotCurveItem import PlotCurveItem

class SensorsDataPlotContoller(QtGui.QWidget, BasePanelController):

    def __init__(self, vehicle_event_dispatcher, ui_event_dispatcher):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        self.ui = Ui_DataPlotPanel()
        self.ui.setupUi(self)
        
        self.ui.plot_view.setRange(xRange=(0, 128), padding=0.0)
        self.ui.plot_view.clear()
        self.ui.plot_view.setBackground(QtGui.QColor('white'))
        self.ui.tree_widget.clear()
        self._plot_index = 0
        
        self._plot_datas_arrays = []
        self._curves = [] 
        colors = [
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
        vehicle_event_dispatcher.register(self._gyro_raw_data_receved, VehicleEventDispatcher.GYRO_DATA_EVENT)
        vehicle_event_dispatcher.register(self._accel_raw_data_receved, VehicleEventDispatcher.ACCEL_DATA_EVENT)
        vehicle_event_dispatcher.register(self._mag_raw_data_receved, VehicleEventDispatcher.MAGNETOMETER_DATA_EVENT)

    def createPlotLine(self, idx, color, plotName):
        self._plot_datas_arrays.append([0.0] * 128)
        self._curves.append(
            PlotCurveItem(self._plot_datas_arrays[idx], pen={'color':color, 'width': 2})
        )
        self.ui.plot_view.addItem(self._curves[idx])

        newLine = QtGui.QTreeWidgetItem()
        newLine.setCheckState(0, 2)
        newLine.setBackgroundColor(0, color)
        newLine.setText(1, plotName + '   ')
        newLine.setText(2, '0.000')
        return newLine
        
    def _protocol_handler_changed_event(self, event, protocol_handler):
        self._protocol_handler = protocol_handler;
                
    def start(self):
        self._protocol_handler.subscribe_sensors_data();
        
    def stop(self):
        self._protocol_handler.unsubscribe_command()
        
    def _gyro_raw_data_receved(self, event, gyro_vector):
        if self.gyro_parent.checkState(0) != 2:
            for i in range(0, 3):
                if self._curves[i] in self.ui.plot_view.items():
                    self.ui.plot_view.removeItem(self._curves[i])
            return
        
        gyro_data_array = [gyro_vector.get_x(),gyro_vector.get_y(),gyro_vector.get_z()]
        for i in range(0, 3):
            gyro_child_node = self.gyro_parent.child(i)
            if gyro_child_node.checkState(0) == 2:
                self._plot_datas_arrays[i].insert(0, float(gyro_data_array[i]))
                self._plot_datas_arrays[i].pop()
                gyro_child_node.setText(2, gyro_data_array[i])
                self._curves[i].setData(self._plot_datas_arrays[i])
                if self._curves[i] not in self.ui.plot_view.items():
                    self.ui.plot_view.addItem(self._curves[i])
            elif self._curves[i] in self.ui.plot_view.items():
                self.ui.plot_view.removeItem(self._curves[i])
        
    def _accel_raw_data_receved(self, event, accel_vector):
        if self.accel_parent.checkState(0) != 2:
            for i in range(0, 3):
                if self._curves[i+3] in self.ui.plot_view.items():
                    self.ui.plot_view.removeItem(self._curves[i+3])
            return

        accel_data_array = [accel_vector.get_x(),accel_vector.get_y(),accel_vector.get_z()]
        for i in range(0, 3):
            accel_child_node = self.accel_parent.child(i)
            if accel_child_node.checkState(0) == 2:
                self._plot_datas_arrays[i+3].insert(0, float(accel_data_array[i]))
                self._plot_datas_arrays[i+3].pop()
                accel_child_node.setText(2, accel_data_array[i])
                self._curves[i+3].setData(self._plot_datas_arrays[i+3])
                if self._curves[i+3] not in self.ui.plot_view.items():
                    self.ui.plot_view.addItem(self._curves[i+3])
            elif self._curves[i+3] in self.ui.plot_view.items():
                self.ui.plot_view.removeItem(self._curves[i+3])
        
    def _mag_raw_data_receved(self, event, mag_vector):
        return
#        if self.mag_parent.checkState(0) != 2:
#            for i in range(0, 3):
#                if self._curves[i+3] in self.ui.plot_view.items():
#                self._plot_datas_arrays[i].insert(0, 0.0)
#                self._curves[i].setData(self._plot_datas_arrays[i])
#                    self.ui.plot_view.removeItem(self._curves[i+3])
#            return
#
#        mag_data_array = [mag_vector.get_x(),mag_vector.get_y(),mag_vector.get_z()]
#        for i in range(0, 3):
#            accel_child_node = self.mag_parent.child(i)
#            if accel_child_node.checkState(0) == 2:
#                self._plot_datas_arrays[i+6].insert(0, float(mag_data_array[i]))
#                self._plot_datas_arrays[i+6].pop()
#                accel_child_node.setText(2, mag_data_array[i])
#                self._curves[i+6].setData(self._plot_datas_arrays[i])
#                if self._curves[i+6] not in self.ui.plot_view.items():
#                    self.ui.plot_view.addItem(self._curves[i+6])
#            elif self._curves[i] in self.ui.plot_view.items():
##                self._plot_datas_arrays[i].insert(0, 0.0)
##                self._curves[i].setData(self._plot_datas_arrays[i])
#                self.ui.plot_view.removeItem(self._curves[i+6])
#        self.ui.plot_view.autoRange()


