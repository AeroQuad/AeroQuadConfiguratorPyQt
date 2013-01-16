'''
AeroQuad Configurator v4.0
Created on Nov 6, 2012

@author: Ted Carancho
'''
import sys

from PyQt4 import QtCore, QtGui
from serial import SerialException
from ui.mainWindow import Ui_MainWindow
from communication.serialCom import AQSerial
from ui.splashScreen import Ui_splashScreen
import xml.etree.ElementTree as ET
xml = ET.parse('AeroQuadConfigurator.xml')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class AQMain(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # TODO: figure out way to configure for different comm types (TCP, MAVLINK, etc) 
        self.comm = AQSerial()
        
        # Default main window conditions
        self.ui.buttonDisconnect.setEnabled(False)
        self.ui.buttonConnect.setEnabled(True)
        self.ui.comPort.setEnabled(True)
        self.ui.baudRate.setEnabled(True)
        self.ui.status.setText("Not connected to the AeroQuad")
        self.availablePorts = []
        self.updateComPortSelection()
        self.updateBaudRates()
        self.boardConfiguration = []
        
        # Update comm port combo box to use last used comm port
        defaultComPort = xml.find("./Settings/DefaultComPort").text
        commIndex = self.ui.comPort.findText(defaultComPort)
        if commIndex == -1:
            commIndex = 0
        self.ui.comPort.setCurrentIndex(commIndex)
        
        # Load splash screen
        splash = Ui_splashScreen()
        splash.setupUi(splash)
        self.ui.subPanel.addWidget(splash)
        
        # Dynamically configure board type menu and subPanel menu from XML configuration file
        self.configureSubPanelMenu()
        self.activeSubPanel = None
        self.activeSubPanelName = ""

        # Connect GUI slots and signals
        self.ui.comPort.return_handler = self.connect
        self.ui.buttonConnect.clicked.connect(self.connect)
        self.ui.buttonDisconnect.clicked.connect(self.disconnect)
        self.ui.actionExit.triggered.connect(QtGui.qApp.quit)
        self.ui.comPort.currentIndexChanged.connect(self.updateDetectedPorts)
        self.ui.actionBootUpDelay.triggered.connect(self.updateBootUpDelay)
        self.ui.actionCommTimeout.triggered.connect(self.updateCommTimeOut)

    ####### Communication Methods #######       
    def connect(self):
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
            # Stop and flush any previous telemetry being streamed
            stopTelemetry = xml.find("./Settings/StopTelemetry").text
            self.comm.write(stopTelemetry)
            self.comm.flushResponse()
            # Request version number to identify AeroQuad board
            versionRequest = xml.find("./Settings/SoftwareVersion").text
            self.comm.write(versionRequest)
            version = self.comm.waitForRead()

            if version != "":
                self.storeComPortSelection()
                self.ui.status.setText("Connected to AeroQuad Flight Software v" + version)
                # Read board configuration
                config = xml.find("./Settings/BoardConfiguration").text
                self.comm.write(config)
                size = int(self.comm.waitForRead())
                for index in range(size):
                    response = self.comm.waitForRead()
                    self.boardConfiguration.append(response)
                # Hide menu items that don't match board configuration
                for index in range(len(self.subPanelMenu)):
                    hide = self.checkRequirementsMatch(self.subPanelList[index])
                    self.subPanelMenu[index].setVisible(hide)
                # Load configuration screen
                self.selectSubPanel("Vehicle Configuration")
                self.restartSubPanel()
            else:
                self.disconnect()
                self.ui.status.setText("Not connected to the AeroQuad")
                QtGui.QMessageBox.information(self, "Connection Error", "Unable to connect to the AeroQuad.  Try increasing the Boot Up Delay.\nThis is found under File->Preferences->Boot Up Delay.")
        except SerialException, se:
            self.ui.buttonDisconnect.setEnabled(False)
            self.ui.buttonConnect.setEnabled(True)
            self.ui.comPort.setEnabled(True)
            self.ui.baudRate.setEnabled(True)
            self.ui.status.setText("Connection Failed")
            self.boardConfiguration = []
        
    def disconnect(self):
        '''Disconnect from the AeroQuad'''
        self.comm.write(xml.find("./Settings/StopTelemetry").text)
        self.comm.disconnect()
        # Update GUI
        self.ui.buttonDisconnect.setEnabled(False)
        self.ui.buttonConnect.setEnabled(True)
        self.ui.comPort.setEnabled(True)
        self.ui.baudRate.setEnabled(True)
        self.ui.status.setText("Disconnected from the AeroQuad")
        self.boardConfiguration = []
        self.restartSubPanel()

    def updateDetectedPorts(self):
        '''Cycles through 256 ports and checks if there is a response from them.'''
        selection = self.ui.comPort.currentText()
        if selection == "Refresh":
            self.updateComPortSelection()
            self.ui.comPort.setCurrentIndex(0)
            self.ui.status.setText("Updated list of available COM ports")
        elif selection == "Autoconnect":
            self.ui.comPort.setCurrentIndex(0)
            self.ui.status.setText("This feature still under construction")
            
    def autoConnect(self):
        pass
    
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
        for n in self.comm.detectPorts():
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
            tempSubPanel = module()          
            tempSubPanel.initialize(self.comm, xml, self.ui)
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
        self.activeSubPanel.start(self.activeSubPanelName, self.boardConfiguration)
        self.ui.status.setText(subPanelName)
        app.processEvents()

    def clearSubPanelMenu(self):
        ''' Clear subPanel menu and disconnect subPanel related signals'''
        self.ui.menuView.clear()
        self.subPanelMapper.mapped[str].disconnect(self.selectSubPanel)
        
    def restartSubPanel(self):
        if self.activeSubPanel != None: # Restart any running subpanels
            self.activeSubPanel.stop()
            self.activeSubPanel.start(self.activeSubPanelName, self.boardConfiguration)
            app.processEvents()
            
    def checkRequirementsMatch(self, subPanelName):
        # Read requirements for the specified subpanel form the XML config file
        xmlRequirement = "./Subpanels/Subpanel/[@Name='" + subPanelName +"']/Requirement"
        subPanelRequirements = xml.findall(xmlRequirement)
        panelRequirements = [] # Holds the requirements as a list of strings
        for requirement in subPanelRequirements:
            panelRequirements.append(requirement.text)
        check = True
        # Go through each subpanel requirement and check against board configuration
        for testRequirement in panelRequirements:
            if (testRequirement == "All"):
                check = True
                break;
            check = check and (testRequirement in self.boardConfiguration)
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

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #app.setStyle("plastique")
    
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