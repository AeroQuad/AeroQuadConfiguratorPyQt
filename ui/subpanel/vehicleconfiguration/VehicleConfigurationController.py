
from PyQt4 import QtCore, QtGui
from model.EventDispatcher import EventDispatcher
from model.VehicleConfigImageMap import VEHICLE_CONFIG_FILE_MAP
from ui.subpanel.BasePanelController import BasePanelController
from ui.subpanel.vehicleconfiguration.VehicleConfigurationPanel import Ui_VehicleConfigurationPanel

class VehicleConfigurationController(QtGui.QWidget, BasePanelController):
    
    def __init__(self, event_dispatcher, protocol_handler):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        self.ui = Ui_VehicleConfigurationPanel()
        self.ui.setupUi(self)
        
        self.ui.configSpecs.setRowCount(15)
        self.ui.configSpecs.setColumnCount(1)
        self._reset_panel()
        
        event_dispatcher.register(self._connection_state_changed, EventDispatcher.CONNECTION_STATE_CHANGED_EVENT)
        event_dispatcher.register(self._flight_config_received, EventDispatcher.FLIGHT_CONFIG_EVENT)
        event_dispatcher.register(self._board_config_received, EventDispatcher.BOAR_TYPE_EVENT)
        event_dispatcher.register(self._board_config_received, EventDispatcher.RECEIVER_TYPE_EVENT)
        event_dispatcher.register(self._board_config_received, EventDispatcher.RECEIVER_NB_CHANNEL_EVENT)
        event_dispatcher.register(self._board_config_received, EventDispatcher.NUMBER_MOTORS_EVENT)
        event_dispatcher.register(self._board_config_received, EventDispatcher.GYROSCOPE_DETECTED_EVENT)
        event_dispatcher.register(self._board_config_received, EventDispatcher.ACCELEROMETER_DETECTED_EVENT)
        event_dispatcher.register(self._board_config_received, EventDispatcher.BAROMETER_DETECTED_EVENT)
        event_dispatcher.register(self._board_config_received, EventDispatcher.MAGNETOMETER_DETECTED_EVENT)
        event_dispatcher.register(self._board_config_received, EventDispatcher.HEADING_HOLD_ENABLED_EVENT)
        event_dispatcher.register(self._board_config_received, EventDispatcher.ALTITUDE_HOLD_ENABLED_EVENT)
        event_dispatcher.register(self._board_config_received, EventDispatcher.BATTERY_MONITOR_ENABLED_EVENT)

    def _reset_panel(self):
        self.ui.configSpecs.clear()
        self._row = 0
        self._vehicle_config_image = QtGui.QPixmap(VEHICLE_CONFIG_FILE_MAP['Quad +'])
        self._display_vehicle_config()

    def _connection_state_changed(self, event, is_connected):
        self._reset_panel()
        
    def _flight_config_received(self, header, information):
        self._board_config_received(header,information)
        self._vehicle_config_image = QtGui.QPixmap(VEHICLE_CONFIG_FILE_MAP[information])
        self._display_vehicle_config()            
    
    def _board_config_received(self, header, information):
        information_cellule = QtGui.QTableWidgetItem()                           
        information_cellule.setTextColor(QtCore.Qt.white)
        information_cellule.setTextAlignment(QtCore.Qt.AlignCenter)
        information_cellule.setFlags(QtCore.Qt.ItemIsTristate)
        information_cellule.setText(str(header + ' : ' + information))
        self.ui.configSpecs.setItem(self._row, 0, information_cellule)
        self.ui.configSpecs.resizeColumnToContents(0)
        self._row += 1

    def resizeEvent(self, event):
        self._display_vehicle_config()
        
    def _display_vehicle_config(self):
        width = self.ui.configView.width() - 50
        height = self.ui.configView.height() - 50
        scaledImage = self._vehicle_config_image.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.ui.configView.setPixmap(scaledImage)
        self.ui.configView.setAlignment(QtCore.Qt.AlignCenter)
