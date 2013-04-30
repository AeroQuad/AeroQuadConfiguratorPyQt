'''
AeroQuad Configurator v4.0
Created on Nov 6, 2012

@author: Ted Carancho
'''
import sys
import logging

from PyQt4 import QtCore, QtGui
from serial import SerialException
from ui.MainWindow import Ui_MainWindow
from communication.SerialCommunicator import SerialCommunicator
from ui.SplashScreen import SplashScreen
import xml.etree.ElementTree as xmlParser
from model.VehicleModel import VehicleModel
from communication.aqprotocolhandler.AQV4ProtocolHandler import AQV4ProtocolHandler
from communication.aqprotocolhandler.AQV32ProtocolHandler import AQV32ProtocolHandler
from communication.aqprotocolhandler.ProtocolHandler import ProtocolHandler
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
        self.ui.subPanel.setStyleSheet("QStackedWidget{background-image: url(" + background + ");}")
        
        #logging
        logging.basicConfig(filename='logfile.log',level=logging.DEBUG)
        logging.basicConfig(format='%(asctime)s %(filename)s %(lineno)d %(message)s')
        
        # TODO: figure out way to configure for different comm types (TCP, MAVLINK, etc)
        # Kenny answer: use a different communicator if not serial, protocol handler will be responsible to feed the model correcly 
        self.comm = SerialCommunicator()
        

        self._vehicle_model = VehicleModel()
        # @todo Kenny, remove this!
        self._protocol_handler = AQV32ProtocolHandler(self.comm,self._vehicle_model)
#        self.message_sender = AQV4MessageSender(self.comm)

        
                
        # Default main window conditions
        self.ui.buttonDisconnect.setEnabled(False)
        self.ui.buttonConnect.setEnabled(True)
        self.ui.comPort.setEnabled(True)
        self.ui.baudRate.setEnabled(True)
        self.ui.status.setText("Not connected to the AeroQuad")
        self.availablePorts = []
        self.updateComPortSelection()
        self.updateBaudRates()
        self.boardConfiguration = {}
        self.manualConnect = True
        
        # Update comm port combo box to use last used comm port
        defaultComPort = xml.find("./Settings/DefaultComPort").text
        commIndex = self.ui.comPort.findText(defaultComPort)
        if commIndex == -1:
            commIndex = 0
        self.ui.comPort.setCurrentIndex(commIndex)
        
        # Load splash screen
        splash = SplashScreen()
        splash.setupUi(splash)
        self.ui.subPanel.addWidget(splash)
        
        # Dynamically configure board type menu and subPanel menu from XML configuration file
        self.configureSubPanelMenu()
        self.activeSubPanel = None
        self.activeSubPanelName = ""

        # Connect GUI slots and signals
        self.ui.comPort.return_handler = self.connectBoard
        self.ui.buttonConnect.clicked.connect(self.connectBoard)
        self.ui.buttonDisconnect.clicked.connect(self.disconnectBoard)
        self.ui.actionExit.triggered.connect(QtGui.qApp.quit)
        self.ui.comPort.currentIndexChanged.connect(self.updateDetectedPorts)
        self.ui.actionBootUpDelay.triggered.connect(self.updateBootUpDelay)
        self.ui.actionCommTimeout.triggered.connect(self.updateCommTimeOut)
        self.ui.button_home.clicked.connect(self.return_home)
       
        #SideMenuButtons
        self.ui.sidemenu_button_vehicle_status.clicked.connect(self.button_vehicle_status)
        self.ui.sidemenu_button_vehicle_configuration.clicked.connect(self.button_vehicle_configuration)
        
        self.ui.sidemenu_button_vehicle_setup.clicked.connect(self.button_vehicle_setup)
        self.ui.sidemenu_button_sensors_calibration.clicked.connect(self.button_sensors_calibration)
        self.ui.sidemenu_button_magnetometer_calibration.clicked.connect(self.button_magnetometer_calibration)
        self.ui.sidemenu_button_RC_channels_detection.clicked.connect(self.button_RC_channels_detection)
        self.ui.sidemenu_button_RC_calibartion.clicked.connect(self.button_RC_calibration)
        self.ui.sidemenu_button_motor_command.clicked.connect(self.button_motor_command)
        self.ui.sidemenu_button_PID_update.clicked.connect(self.button_PID_update)
        
        self.ui.sidemenu_button_serial_monitor.clicked.connect(self.button_serial_monitor)
        self.ui.sidemenu_button_sensor_data.clicked.connect(self.button_sensor_data)
        self.ui.sidemenu_button_gyroscope_data.clicked.connect(self.button_gyroscope_data)
        self.ui.sidemenu_button_accelerometer_data.clicked.connect(self.accelerometer_data)
        self.ui.sidemenu_button_magnetometer_data.clicked.connect(self.magnetometer_data)
        self.ui.sidemenu_button_attitude_data.clicked.connect(self.button_attitude_data)
        self.ui.sidemenu_button_transmitter_data.clicked.connect(self.button_transmitter_data)
        self.ui.sidemenu_button_altitude_data.clicked.connect(self.button_altitude_data)
            
    ####### Communication Methods #######       
    def connectBoard(self):
        '''Initiates communication with the AeroQuad'''
        # Setup GUI
        self.ui.status.setText("Connecting...")
        self.ui.buttonDisconnect.setEnabled(True)
        self.ui.buttonConnect.setEnabled(False)
        self.ui.comPort.setEnabled(False)
        self.ui.baudRate.setEnabled(False)
        # Update the GUI
        app.processEvents()
        
        # Setup serial port
        bootupDelay = float(xml.find("./Settings/BootUpDelay").text)
        commTimeOut = float(xml.find("./Settings/CommTimeOut").text)
        try:
            self.comm.connect(str(self.ui.comPort.currentText()), int(self.ui.baudRate.currentText()), bootupDelay, commTimeOut)

            self._protocol_handler.unsubscribe_command()
            version = self._protocol_handler.get_flight_software_version()

            if version != "":
                self.storeComPortSelection()
                self.ui.status.setText("Connected to AeroQuad Flight Software v" + version)
                
                if version == '4.0' :
                    self._protocol_handler.request_board_configuration()
                    pass
                    # this do nothign really for now, but, should be like this, currently, panels need it instantiated before!
#                    self.communication_protocol_handler = AQV4ProtocolHandler(self.comm,self.vehicle_model)
#                    self.message_sender = AQV4MessageSender(self.comm)
                elif version == '3.2' :
                    self._protocol_handler.request_board_configuration()
                    pass
#                    self.communication_protocol_handler = AQV32ProtocolHandler(self.comm,self.vehicle_model)
#                    self.message_sender = AQV32MessageSender(self.comm)

                else :
                    logging.error("Flight software version " + version + " unsuported")
                    self.disconnectBoard()
                    self.ui.status.setText("Not connected to the AeroQuad")
                
                return True
            else:
                self.disconnectBoard()
                self.ui.status.setText("Not connected to the AeroQuad")
                if self.manualConnect:
                    QtGui.QMessageBox.information(self, "Connection Error", "Unable to connect to the AeroQuad.  Verify the board is plugged in.\n\nIf it is, try increasing the Boot Up Delay.\nThis is found under File->Preferences->Boot Up Delay.")
                return False
        except SerialException:
            self.ui.buttonDisconnect.setEnabled(False)
            self.ui.buttonConnect.setEnabled(True)
            self.ui.comPort.setEnabled(True)
            self.ui.baudRate.setEnabled(True)
            self.ui.status.setText("Connection Failed")
            self.boardConfiguration = {}
            return False
        
    def disconnectBoard(self):
        '''Disconnect from the AeroQuad'''
        self.comm.write(xml.find("./Settings/StopTelemetry").text)
        self.comm.disconnect()
        # Update GUI
        self.ui.buttonDisconnect.setEnabled(False)
        self.ui.buttonConnect.setEnabled(True)
        self.ui.comPort.setEnabled(True)
        self.ui.baudRate.setEnabled(True)
        self.ui.status.setText("Disconnected from the AeroQuad")
        self.boardConfiguration = {}
        self.restartSubPanel()

    def updateDetectedPorts(self):
        '''Cycles through 256 ports and checks if there is a response from them.'''
        selection = self.ui.comPort.currentText()
        if selection == "Refresh":
            self.updateComPortSelection()
            self.ui.comPort.setCurrentIndex(0)
            self.ui.status.setText("Updated list of available COM ports")
        elif selection == "Autoconnect":
            self.updateComPortSelection()
            self.ui.comPort.setCurrentIndex(0)
            self.ui.status.setText("Beginning autoconnect...")
            self.autoConnect()
            
    def autoConnect(self):
        self.manualConnect = False
        autoConnectState = False
        self.updateComPortSelection()
        self.ui.comPort.setCurrentIndex(0)
        for port in xrange(self.ui.comPort.count() - 2):
            self.ui.comPort.setCurrentIndex(port)
            self.ui.status.setText("Attempting to connect to " + self.ui.comPort.currentText() + "...")
            if self.connectBoard():
                self.ui.status.setText("Autoconnect successful!")
                autoConnectState = True
                break
            else:
                self.ui.status.setText("Autoconnect not successful...")
        if not autoConnectState:
            if sys.platform.startswith("linux"):
                QtGui.QMessageBox.information(self, 'Autoconnect Not Successful', 'Verify that you are a member of the dialout group.  To add yourself to the dialout group, issue the following command in a terminal:\n"sudo adduser yourUserName dialout."\n\nYou may need to restart the Configurator.')
        self.manualConnect = True
    
    def updateBootUpDelay(self):
        '''Creates dialog box to ask user for desired boot up delay.
        This delay waits for Arduino based boards to finish booting up before sending commands.
        '''
        bootUpDelay = float(xml.find("./Settings/BootUpDelay").text)
        data, ok = QtGui.QInputDialog.getDouble(self, "Boot Up Delay", "Boot Up Delay:", bootUpDelay, 0, 60, 3)
        if ok:
            xml.find("./Settings/BootUpDelay").text = str(data)
            xml.write("AeroQuadConfigurator.xml")
 
    def updateCommTimeOut(self):
        '''Creates dialog box to ask user for desired comm timeout.
        This is timeout value used by serial drivers to wait for response from device
        '''
        commTimeOut = float(xml.find("./Settings/CommTimeOut").text)
        data, ok = QtGui.QInputDialog.getDouble(self, "Comm Time Out", "Comm Time Out:", commTimeOut, 0, 60, 3)
        if ok:
            xml.find("./Settings/CommTimeOut").text = str(data)
            xml.write("AeroQuadConfigurator.xml")

    def updateComPortSelection(self):
        '''Look for available comm ports and updates combo box'''
        self.ui.comPort.clear()
        for n in self.comm.detect_ports():
            self.ui.comPort.addItem(n)
        self.ui.comPort.insertSeparator(self.ui.comPort.count())
        self.ui.comPort.addItem("Autoconnect")
        self.ui.comPort.addItem("Refresh")
        
    def storeComPortSelection(self):
        '''Stores comm port selection to xml file for later recall'''
        xml.find("./Settings/DefaultBaudRate").text = str(self.ui.baudRate.currentText())
        xml.find("./Settings/DefaultComPort").text = str(self.ui.comPort.currentText())
        xml.write("AeroQuadConfigurator.xml")
               
    def updateBaudRates(self):
        '''Reads baud rates from xml and displays in combo box.
        Updates the xml file to display different baud rates
        '''
        defaultBaudRate = xml.find("./Settings/DefaultBaudRate").text
        baudRates = xml.find("./Settings/AvailableBaudRates").text
        baudRate = baudRates.split(',')
        for i in baudRate:
            self.ui.baudRate.addItem(i)
        self.ui.baudRate.setCurrentIndex(baudRate.index(defaultBaudRate))
        
    def autoSetup(self):
        # Load menu and autoconnect to board by default
        self.selectSubPanel("Home")


    ####### SubPanel Methods #######
    def configureSubPanelMenu(self):
        '''Dynamically add subpanels to View menu based on XML file configuration
        This also adds the subpanel to a stacked widget and stores object instances so that they can run when selected'''
        subPanels = xml.findall("./Subpanels/Subpanel")
        subPanelCount = 1
        self.subPanelList = [] # Stores subpanel names
        self.subPanelClasses = [] # Stores subpanel object instances
        for subPanel in subPanels:
            self.subPanelList.append(subPanel.get("Name"))
            pathName = xml.find("./Subpanels/Subpanel/[@Name='" + subPanel.get("Name") +"']/Path").text
            className = xml.find("./Subpanels/Subpanel/[@Name='" + subPanel.get("Name") +"']/Class").text
            packageList = pathName.split('.')
            packageList.insert(0, 'subpanel')
            packageString = packageList[0] + '.' + packageList[1] + '.' + packageList[2]
            module = __import__(packageString)
            for package in packageList[1:]: # In case the module is buried into a deep package folder, loop until module is reached
                module = getattr(module, package)
            module = getattr(module, className)
            tempSubPanel = module(self._vehicle_model,self._protocol_handler)          
            tempSubPanel.initialize(self.comm, xml, self.ui, self)
            self.ui.subPanel.addWidget(tempSubPanel)
            self.subPanelClasses.append(tempSubPanel)
            subPanelCount += 1
        self.subPanelMapper = QtCore.QSignalMapper(self)
        self.subPanelMenu = []
        for subPanelName in self.subPanelList:
            subPanel = self.ui.menuView.addAction(subPanelName)
            self.subPanelMenu.append(subPanel) # Need to store this separately because Python only binds stuff at runtime
            self.subPanelMapper.setMapping(subPanel, subPanelName)
            subPanel.triggered.connect(self.subPanelMapper.map)
            subPanel.setCheckable(True)
        self.subPanelMapper.mapped[str].connect(self.selectSubPanel)       
  
    def selectSubPanel(self, subPanelName):
        '''Places check mark beside selected subpanel name
        Menu item instances stored in dedicated list because Python only updates during runtime making everything point to the last item in the list
        '''
        if self.activeSubPanel != None:
            self.activeSubPanel.stop()
        types = len(self.subPanelList)
        for index in range(types):
            self.subPanelMenu[index].setChecked(False)
        selected = self.subPanelList.index(subPanelName)
        self.subPanelMenu[selected].setChecked(True)
        self.ui.subPanel.setCurrentIndex(selected+1) # index 0 is splash screen
        self.activeSubPanel = self.subPanelClasses[selected]
        self.activeSubPanelName = "./Subpanels/Subpanel/[@Name='" + str(subPanelName) + "']" 
        self.activeSubPanel.start()
        if subPanelName == "Menu":
            self.ui.status.setText("Choose Configurator Function")
        else:
            self.ui.status.setText(subPanelName)
        app.processEvents()

    def clearSubPanelMenu(self):
        ''' Clear subPanel menu and disconnect subPanel related signals'''
        self.ui.menuView.clear()
        self.subPanelMapper.mapped[str].disconnect(self.selectSubPanel)
        
    def restartSubPanel(self):
        if self.activeSubPanel != None: # Restart any running subpanels
            self.activeSubPanel.stop()
            self.activeSubPanel.start()
            app.processEvents()
            
    def checkRequirementsMatch(self, subPanelName):
        # Read requirements for the specified subpanel form the XML config file
        xmlRequirement = "./Subpanels/Subpanel/[@Name='" + subPanelName +"']/Requirement"
        subPanelRequirements = xml.findall(xmlRequirement)
        
        panelRequirements = {}
        booleanOperation = {}      
        for requirements in subPanelRequirements:
            requirement = requirements.text.split(':')
            if requirement[0] == "All": # Need element 1 populated if "All" detected
                requirement.append("All")
            panelRequirements[requirement[0]] = requirement[1].strip()
            booleanOperation[requirement[0]] = requirements.get("type")

        # Go through each subpanel requirement and check against board configuration
        # If no boolean type defined, assume AND
        requirementType = panelRequirements.keys()
        # If no Requirement found, assume ALL
        try:
            if (requirementType[0] == "All"):
                check = True
            else:
                check = any(panelRequirements[requirementType[0]] in s for s in self.boardConfiguration.values())
                for testRequirement in requirementType[1:]:
                    if (booleanOperation[testRequirement] == "or") or (booleanOperation[testRequirement] == "OR"):
                        check = check or any(panelRequirements[testRequirement] in s for s in self.boardConfiguration.values())
                    else:
                        check = check and any(panelRequirements[testRequirement] in s for s in self.boardConfiguration.values())
        except:
            check = True
        return check


    ####### Housekeeping Functions #######
        
    def exit(self):
        self.comm.disconnect()
        sys.exit(app.exec_())

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def return_home(self):
        self.selectSubPanel("Home") 
        
    def button_vehicle_status(self):
        self.selectSubPanel("Vehicle Status") 
    
    def button_vehicle_configuration(self):
        self.selectSubPanel("Vehicle Configuration")

    def button_vehicle_setup(self):
        self.selectSubPanel("Vehicle configuration")
        
    def button_sensors_calibration(self):
        self.selectSubPanel("Sensors calibration")
        
    def button_magnetometer_calibration(self):
        self.selectSubPanel("Magnetometer calibration")
        
    def button_RC_channels_detection(self):
        self.selectSubPanel("Receiver channels detection")
        
    def button_RC_calibration(self):
        self.selectSubPanel("Receiver Calibration")
        
    def button_motor_command(self):
        self.selectSubPanel("Motor Command")
    
    def button_PID_update(self):
        self.selectSubPanel("PID Update")
    
    def button_serial_monitor(self):
        self.selectSubPanel("Serial Monitor")
    
    def button_sensor_data(self):
        self.selectSubPanel("Sensor Data")
    
    def button_gyroscope_data(self):
        self.selectSubPanel("Gyroscope Data")
        
    def accelerometer_data(self):
        self.selectSubPanel("Accelerometer Data")
        
    def magnetometer_data(self):
        self.selectSubPanel("Magnetometer Data")
        
    def button_attitude_data(self):
        self.selectSubPanel("Attitude Data")
    
    def button_transmitter_data(self):
        self.selectSubPanel("Transmitter Data")
    
    def button_altitude_data(self):
        self.selectSubPanel("Altitude Data")

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
    MainWindow.autoSetup()
    sys.exit(app.exec_())