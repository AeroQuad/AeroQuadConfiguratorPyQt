
from PyQt4 import QtGui
from ui.subpanel.dataplot.DataPlotPanel import Ui_DataPlotPanel
from ui.subpanel.BasePanelController import BasePanelController
from model.VehicleEventDispatcher import VehicleEventDispatcher
from ui.UIEventDispatcher import UIEventDispatcher
from pyqtgraph.graphicsItems.PlotCurveItem import PlotCurveItem

class ReceiverDataPlotContoller(QtGui.QWidget, BasePanelController):


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
        self._tree_nodes = []
        
        vehicle_event_dispatcher.register(self._receiver_nb_channels_received, VehicleEventDispatcher.RECEIVER_NB_CHANNEL_EVENT)
        ui_event_dispatcher.register(self._protocol_handler_changed_event, UIEventDispatcher.PROTOCOL_HANDLER_EVENT)
        
        vehicle_event_dispatcher.register(self._receiver_roll_event, VehicleEventDispatcher.RECEIVER_ROLL_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_pitch_event, VehicleEventDispatcher.RECEIVER_PITCH_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_yaw_event, VehicleEventDispatcher.RECEIVER_YAW_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_throttle_event, VehicleEventDispatcher.RECEIVER_THROTTLE_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_mode_event, VehicleEventDispatcher.RECEIVER_MODE_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_aux1_event, VehicleEventDispatcher.RECEIVER_AUX1_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_aux2_event, VehicleEventDispatcher.RECEIVER_AUX2_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_aux3_event, VehicleEventDispatcher.RECEIVER_AUX3_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_aux4_event, VehicleEventDispatcher.RECEIVER_AUX4_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_aux5_event, VehicleEventDispatcher.RECEIVER_AUX5_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_aux6_event, VehicleEventDispatcher.RECEIVER_AUX6_PROPERTY_EVENT)
        vehicle_event_dispatcher.register(self._receiver_aux7_event, VehicleEventDispatcher.RECEIVER_AUX7_PROPERTY_EVENT)
        
    def _receiver_nb_channels_received(self, header, nb_channel):
        
        channel_array_names = ['Roll','Pitch','Yaw','Throttle','Mode','AUX1','AUX2','AUX3','AUX4','AUX5','AUX6','AUX7','AUX8']
    
        colors = [QtGui.QColor('blue'),
                  QtGui.QColor('red'),
                  QtGui.QColor('lime'),
                  QtGui.QColor('cornflowerblue'),
                  QtGui.QColor('greenyellow'),
                  QtGui.QColor('violet'),
                  QtGui.QColor('orange'),
                  QtGui.QColor('deepskyblue'),
                  QtGui.QColor('firebrick'),
                  QtGui.QColor('aqua')]
    
        for i in range(0, int(nb_channel)) :
            self._tree_nodes.append(QtGui.QTreeWidgetItem(self.ui.tree_widget))
            self._tree_nodes[i].setCheckState(0, 2)
            self._tree_nodes[i].setText(1, channel_array_names[i])
            self._tree_nodes[i].setBackgroundColor(0, colors[i])
            self._tree_nodes[i].setText(2, '0.000')
            self._plot_datas_arrays.append([0.0] * 128)
            self._curves.append(
                   PlotCurveItem(self._plot_datas_arrays[i], pen={'color':colors[i], 'width': 2})
            )
            self.ui.plot_view.addItem(self._curves[i])
        
    def _protocol_handler_changed_event(self, event, protocol_handler):
        self._protocol_handler = protocol_handler;     
        
    def start(self):
        self._protocol_handler.subscribe_receiver_data();   
    
    def stop(self):
        self._protocol_handler.unsubscribe_command()
        
    def _receiver_roll_event(self, event, roll):
        self._update_panel_data(0, roll)
    
    def _receiver_pitch_event(self, event, pitch):
        self._update_panel_data(1, pitch)
    
    def _receiver_yaw_event(self, event, yaw):
        self._update_panel_data(2, yaw)
    
    def _receiver_throttle_event(self, event, throttle):
        self._update_panel_data(3, throttle)
    
    def _receiver_mode_event(self, event, mode):
        self._update_panel_data(4, mode)
    
    def _receiver_aux1_event(self, event, aux1):
        self._update_panel_data(5, aux1)
    
    def _receiver_aux2_event(self, event, aux2):
        self._update_panel_data(6, aux2)
    
    def _receiver_aux3_event(self, event, aux3):
        self._update_panel_data(7, aux3)
    
    def _receiver_aux4_event(self, event, aux4):
        self._update_panel_data(8, aux4)
    
    def _receiver_aux5_event(self, event, aux5):
        self._update_panel_data(9, aux5)
    
    def _receiver_aux6_event(self, event, aux6):
        self._update_panel_data(10, aux6)
    
    def _receiver_aux7_event(self, event, aux7):
        self._update_panel_data(11, aux7)
    
    def _update_panel_data(self, index, value):
        if self._tree_nodes[index].checkState(0) == 2:
            self._plot_datas_arrays[index].insert(0, value)
            self._plot_datas_arrays[index].pop()
            self._tree_nodes[index].setText(2, str(value))
            self._curves[index].setData(self._plot_datas_arrays[index])
            if self._curves[index] not in self.ui.plot_view.items():
                self.ui.plot_view.addItem(self._curves[index])
        elif self._curves[index] in self.ui.plot_view.items():
                self.ui.plot_view.removeItem(self._curves[index])
    