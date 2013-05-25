
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
        
        # TODO: figure out way to configure for different _communicator types (TCP, MAVLINK, etc)
        # Kenny answer: use a different communicator if not serial, protocol handler will be responsible to feed the model correcly 
        self._communicator = SerialCommunicator()
        self._vehicle_event_dispatcher = VehicleEventDispatcher()
        self._connection_manager = ConnectionManager(app, self.ui, xml, self._communicator, self._vehicle_event_dispatcher)
        
        # Default main window conditions
        self.ui.buttonDisconnect.setEnabled(False)
        self.ui.buttonConnect.setEnabled(True)
        self.ui.comPort.setEnabled(True)
        self.ui.baudRate.setEnabled(True)
        self.ui.status.setText("Not connected to the AeroQuad")
        self.availablePorts = []
        self.boardConfiguration = {}
        self.manualConnect = True
        
        self._ui_event_dispatcher = UIEventDispatcher()
        
        self._side_menu_contextual_builder = SideMenuContextualBuilder(self._vehicle_event_dispatcher,
                                                                       self._ui_event_dispatcher,
                                                                       self.ui.side_menu_info_page,
                                                                       self.ui.side_menu_setting_page,
                                                                       self.ui.side_menu_troubleshooting_page,
                                                                       self.ui.side_menu_mission_planer_page)
                
        
        
        
        # Load splash screen
        splash = SplashScreen()
        splash.setupUi(splash)
        self.ui.panel_container.addWidget(splash)
        
        # Dynamically configure board type menu and subPanel menu from XML configuration file
        self.configureSubPanelMenu()
        self.activeSubPanel = None
        self.activeSubPanelName = ""

        # Connect GUI slots and signals
        self.ui.comPort.return_handler = self._connection_manager.connect_to_aeroquad
        self.ui.buttonConnect.clicked.connect(self._connection_manager.connect_to_aeroquad)
        self.ui.buttonDisconnect.clicked.connect(self._connection_manager.disconnect_from_aeroquad)
        self.ui.action_exit.triggered.connect(QtGui.qApp.quit)
        self.ui.comPort.currentIndexChanged.connect(self._connection_manager.search_for_available_COM_port)
        self.ui.action_bootup_delay.triggered.connect(self._connection_manager.save_boot_delay)
        self.ui.action_comm_timeout.triggered.connect(self._connection_manager.save_connection_timeout_delay)
#        self.ui.button_home.clicked.connect(self.return_home)
       
        #SideMenuButtons
#        self.ui.sidemenu_button_vehicle_status.clicked.connect(self.button_vehicle_status)
#        self.ui.sidemenu_button_vehicle_configuration.clicked.connect(self.button_vehicle_configuration)
#        
#        self.ui.sidemenu_button_vehicle_setup.clicked.connect(self.button_vehicle_setup)
#        self.ui.sidemenu_button_sensors_calibration.clicked.connect(self.button_sensors_calibration)
#        self.ui.sidemenu_button_magnetometer_calibration.clicked.connect(self.button_magnetometer_calibration)
#        self.ui.sidemenu_button_RC_channels_detection.clicked.connect(self.button_RC_channels_detection)
#        self.ui.sidemenu_button_RC_calibartion.clicked.connect(self.button_RC_calibration)
#        self.ui.sidemenu_button_motor_command.clicked.connect(self.button_motor_command)
#        self.ui.sidemenu_button_PID_update.clicked.connect(self.button_PID_update)
#        
#        self.ui.sidemenu_button_serial_monitor.clicked.connect(self.button_serial_monitor)
#        self.ui.sidemenu_button_sensor_data.clicked.connect(self.button_sensor_data)
#        self.ui.sidemenu_button_gyroscope_data.clicked.connect(self.button_gyroscope_data)
#        self.ui.sidemenu_button_accelerometer_data.clicked.connect(self.accelerometer_data)
#        self.ui.sidemenu_button_magnetometer_data.clicked.connect(self.magnetometer_data)
#        self.ui.sidemenu_button_attitude_data.clicked.connect(self.button_attitude_data)
#        self.ui.sidemenu_button_transmitter_data.clicked.connect(self.button_transmitter_data)
#        self.ui.sidemenu_button_altitude_data.clicked.connect(self.button_altitude_data)
        
#        self.selectSubPanel("Home")



    ####### SubPanel Methods #######
    def configureSubPanelMenu(self):
        pass
#        '''Dynamically add subpanels to View menu based on XML file configuration
#        This also adds the subpanel to a stacked widget and stores object instances so that they can run when selected'''
#        subPanels = xml.findall("./Subpanels/Subpanel")
#        subPanelCount = 1
#        self.subPanelList = [] # Stores subpanel names
#        self.subPanelClasses = [] # Stores subpanel object instances
#        for subPanel in subPanels:
#            self.subPanelList.append(subPanel.get("Name"))
#            pathName = xml.find("./Subpanels/Subpanel/[@Name='" + subPanel.get("Name") +"']/Path").text
#            className = xml.find("./Subpanels/Subpanel/[@Name='" + subPanel.get("Name") +"']/Class").text
#            packageList = pathName.split('.')
#            packageList.insert(0, 'subpanel')
#            packageString = packageList[0] + '.' + packageList[1] + '.' + packageList[2]
#            module = __import__(packageString)
#            for package in packageList[1:]: 
#                module = getattr(module, package)
#            module = getattr(module, className)
#            tempSubPanel = module(self._event_dispatcher, self._connection_manager.protocol_handler)          
#            tempSubPanel.initialize()
#            self.ui.subPanel.addWidget(tempSubPanel)
#            self.subPanelClasses.append(tempSubPanel)
#            subPanelCount += 1
#        self.subPanelMapper = QtCore.QSignalMapper(self)
#        self.subPanelMenu = []
#        for subPanelName in self.subPanelList:
#            subPanel = self.ui.menuView.addAction(subPanelName)
#            self.subPanelMenu.append(subPanel) 
#            self.subPanelMapper.setMapping(subPanel, subPanelName)
#            subPanel.triggered.connect(self.subPanelMapper.map)
#            subPanel.setCheckable(True)
#        self.subPanelMapper.mapped[str].connect(self.selectSubPanel)       
  
    def selectSubPanel(self, subPanelName):
        pass
#        if self.activeSubPanel != None:
#            self.activeSubPanel.stop()
#        types = len(self.subPanelList)
#        for index in range(types):
#            self.subPanelMenu[index].setChecked(False)
#        selected = self.subPanelList.index(subPanelName)
#        self.subPanelMenu[selected].setChecked(True)
#        self.ui.subPanel.setCurrentIndex(selected+1) # index 0 is splash screen
#        self.activeSubPanel = self.subPanelClasses[selected]
#        self.activeSubPanelName = "./Subpanels/Subpanel/[@Name='" + str(subPanelName) + "']" 
#        self.activeSubPanel.start()
#        if subPanelName == "Menu":
#            self.ui.status.setText("Choose Configurator Function")
#        else:
#            self.ui.status.setText(subPanelName)
#        app.processEvents()

#    def clearSubPanelMenu(self):
#        self.ui.menuView.clear()
#        self.subPanelMapper.mapped[str].disconnect(self.selectSubPanel)
            

    ####### Housekeeping Functions #######
    def exit(self):
        self._communicator.disconnect()
        sys.exit(app.exec_())

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
#    def return_home(self):
#        self.selectSubPanel("Home") 
#        
#    def button_vehicle_status(self):
#        self.selectSubPanel("Vehicle Status") 
#    
#    def button_vehicle_configuration(self):
#        self.selectSubPanel("Vehicle Configuration")
#
#    def button_vehicle_setup(self):
#        self.selectSubPanel("Vehicle configuration")
#        
#    def button_sensors_calibration(self):
#        self.selectSubPanel("Sensors calibration")
#        
#    def button_magnetometer_calibration(self):
#        self.selectSubPanel("Magnetometer calibration")
#        
#    def button_RC_channels_detection(self):
#        self.selectSubPanel("Receiver channels detection")
#        
#    def button_RC_calibration(self):
#        self.selectSubPanel("Receiver Calibration")
#        
#    def button_motor_command(self):
#        self.selectSubPanel("Motor Command")
#    
#    def button_PID_update(self):
#        self.selectSubPanel("PID Update")
#    
#    def button_serial_monitor(self):
#        self.selectSubPanel("Serial Monitor")
#    
#    def button_sensor_data(self):
#        self.selectSubPanel("Sensor Data")
#    
#    def button_gyroscope_data(self):
#        self.selectSubPanel("Gyroscope Data")
#        
#    def accelerometer_data(self):
#        self.selectSubPanel("Accelerometer Data")
#        
#    def magnetometer_data(self):
#        self.selectSubPanel("Magnetometer Data")
#        
#    def button_attitude_data(self):
#        self.selectSubPanel("Attitude Data")
#    
#    def button_transmitter_data(self):
#        self.selectSubPanel("Transmitter Data")
#    
#    def button_altitude_data(self):
#        self.selectSubPanel("Altitude Data")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    splash_pix = QtGui.QPixmap('./resources/AQ.png')
    splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()
    
    MainWindow = AQMain()
    MainWindow.show()
    MainWindow.center()
    if sys.platform == 'darwin':
        MainWindow.raise_()
    splash.finish(MainWindow)
    sys.exit(app.exec_())