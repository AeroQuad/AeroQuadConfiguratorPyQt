
import sys
import logging
import xml.etree.ElementTree as xmlParser

from PyQt4 import QtCore, QtGui

from communication.SerialCommunicator import SerialCommunicator
from model.VehicleEventDispatcher import VehicleEventDispatcher
from connectionmanager.ConnectionManager import ConnectionManager
from ui.SplashScreen import SplashScreen
from ui.MainWindow import Ui_MainWindow
from ui.SideMenuContextualBuilder import SideMenuContextualBuilder
from ui.UIEventDispatcher import UIEventDispatcher
from ui.PanelsContextBuilder import PanelsContextBuilder
from ui.ViewMenuContextBuilder import ViewMenuContextBuilder

xml = xmlParser.parse('AeroQuadConfigurator.xml')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class AQMain(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        background = xml.find("./Settings/Background").text
        self.ui.panel_container.setStyleSheet("QStackedWidget{background-image: url(" + background + ");}")
        
        #logging
        logging.basicConfig(filename='logfile.log',level=logging.DEBUG)
        logging.basicConfig(format='%(asctime)s %(filename)s %(lineno)d %(message)s')
                
        self._ui_event_dispatcher = UIEventDispatcher() 
        self._communicator = SerialCommunicator()
        self._vehicle_event_dispatcher = VehicleEventDispatcher()
        self._connection_manager = ConnectionManager(app, 
                                                     self.ui, 
                                                     xml, 
                                                     self._communicator, 
                                                     self._ui_event_dispatcher, 
                                                     self._vehicle_event_dispatcher)
        self._panels_context_builder = PanelsContextBuilder(self._ui_event_dispatcher, self._vehicle_event_dispatcher)
        self._view_menu_context_builder = ViewMenuContextBuilder(self.ui.menu_view,
                                                                 self._ui_event_dispatcher,
                                                                 self._ui_event_dispatcher) 
        self._side_menu_contextual_builder = SideMenuContextualBuilder(self._ui_event_dispatcher,
                                                                       self._ui_event_dispatcher,
                                                                       self.ui.side_menu_info_page,
                                                                       self.ui.side_menu_setting_page,
                                                                       self.ui.side_menu_troubleshooting_page,
                                                                       self.ui.side_menu_mission_planer_page)
        
        # Default main window conditions
        self.ui.buttonDisconnect.setEnabled(False)
        self.ui.buttonConnect.setEnabled(True)
        self.ui.comPort.setEnabled(True)
        self.ui.baudRate.setEnabled(True)
        self.ui.status.setText("Not connected to the AeroQuad")
        self.availablePorts = []
        self.boardConfiguration = {}
        self.manualConnect = True
        
        # Load splash_screen screen
        self._splash_screen = SplashScreen()
        self._splash_screen.setupUi(self._splash_screen)
        self.ui.panel_container.addWidget(self._splash_screen)
        
        # Dynamically configure board type menu and subPanel menu from XML configuration file
        self._current_active_panel = None
        self.activeSubPanelName = ""

        # Connect GUI slots and signals
        self.ui.comPort.return_handler = self._connection_manager.connect_to_aeroquad
        self.ui.buttonConnect.clicked.connect(self._connection_manager.connect_to_aeroquad)
        self.ui.buttonDisconnect.clicked.connect(self._connection_manager.disconnect_from_aeroquad)
        self.ui.action_exit.triggered.connect(QtGui.qApp.quit)
        self.ui.comPort.currentIndexChanged.connect(self._connection_manager.search_for_available_COM_port)
        self.ui.action_bootup_delay.triggered.connect(self._connection_manager.save_boot_delay)
        self.ui.action_comm_timeout.triggered.connect(self._connection_manager.save_connection_timeout_delay)
        
        self._ui_event_dispatcher.register(self._display_panel_event, UIEventDispatcher.DISPLAY_PANEL_EVENT)
        self._ui_event_dispatcher.register(self._connection_state_changed, UIEventDispatcher.CONNECTION_STATE_CHANGED_EVENT)
       
    def _display_panel_event(self, event, panel_id):
        if self._current_active_panel != None:
            self._current_active_panel.stop()
            self.ui.panel_container.removeWidget(self._current_active_panel)
        
        self._current_active_panel = PanelsContextBuilder.PANELS_DICTIONNARY[panel_id]
        self.ui.panel_container.addWidget(self._current_active_panel)
        self.ui.panel_container.setCurrentWidget(self._current_active_panel)
        self._current_active_panel.start();
        
    def _connection_state_changed(self, event, is_connected):
        if not is_connected :
            if self._current_active_panel != None:
                self._current_active_panel.stop()
                self.ui.panel_container.removeWidget(self._current_active_panel)
                self._current_active_panel = None
            
            self.ui.panel_container.setCurrentIndex(0)

    ####### Housekeeping Functions #######
    def exit(self):
        self._communicator.disconnect()
        sys.exit(app.exec_())

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    splash_pix = QtGui.QPixmap('./resources/AQ.png')
    splash_screen = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash_screen.setMask(splash_pix.mask())
    splash_screen.show()
    app.processEvents()
    
    MainWindow = AQMain()
    MainWindow.show()
    MainWindow.center()
    if sys.platform == 'darwin':
        MainWindow.raise_()
    splash_screen.finish(MainWindow)
    sys.exit(app.exec_())