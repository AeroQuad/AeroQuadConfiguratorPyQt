'''
Created on Nov 6, 2012

@author: Ted Carancho
'''
import sys
from PyQt4 import QtGui #QtCore,
from mainWindow import Ui_MainWindow
from communication.serialCom import AQSerial

import xml.etree.ElementTree as ET
xml = ET.parse('AeroQuadConfigurator.xml')

from splashScreen import Ui_splashScreen
from subpanel.subCommMonitor.subCommMonitor import Ui_commMonitor

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
        
        # TODO: Dynamically load subpanel widgets
        self.subPanel = Ui_splashScreen()
        self.subPanel.setupUi(self.subPanel)
        self.ui.subPanel.addWidget(self.subPanel)
                
        # Connect GUI slots and signals
        self.ui.buttonConnect.clicked.connect(self.connect)
        self.ui.buttonDisconnect.clicked.connect(self.disconnect)
        self.ui.actionExit.triggered.connect(QtGui.qApp.quit)
        self.ui.comPort.currentIndexChanged.connect(self.updateDetectedPorts)
        self.ui.actionBootUpDelay.triggered.connect(self.updateBootUpDelay)
        self.ui.actionCommTimeout.triggered.connect(self.updateCommTimeOut)
                
    '''
    Methods which are used for slots
    '''
    def connect(self):
        # Setup GUI
        self.ui.status.setText("Connecting to the AeroQuad...")
        self.ui.buttonDisconnect.setEnabled(True)
        self.ui.buttonConnect.setEnabled(False)
        self.ui.comPort.setEnabled(False)
        self.ui.baudRate.setEnabled(False)
        # Update the GUI
        app.processEvents()
        
        # Setup serial port
        bootupDelay = float(xml.find("./Settings/BootUpDelay").text)
        commTimeOut = float(xml.find("./Settings/CommTimeOut").text)
        self.comm.connect(self.ui.comPort.currentText(), int(self.ui.baudRate.currentText()), bootupDelay, commTimeOut)
        self.comm.write("!")
        version = self.comm.read()
        if version != "":
            self.storeComPortSelection()
            self.ui.status.setText("Connected to the AeroQuad using Flight Software v" + version)
        else:
            self.disconnect()
            self.ui.status.setText("Not connected to AeroQuad")
        # TODO: Need to dynamically load subpanel
        if self.ui.subPanel.currentIndex() == 0:
            self.subPanel1 = Ui_commMonitor()
            self.subPanel1.setupUi(self.subPanel1, self.comm)
            self.ui.subPanel.addWidget(self.subPanel1)
            self.ui.subPanel.setCurrentIndex(1)
        
    def disconnect(self):
        # Setup GUI
        self.ui.buttonDisconnect.setEnabled(False)
        self.ui.buttonConnect.setEnabled(True)
        self.ui.comPort.setEnabled(True)
        self.ui.baudRate.setEnabled(True)
        self.ui.status.setText("Disconnected from AeroQuad")
        
        # TODO: Need to dynamically unload subpanel
        if self.ui.subPanel.currentIndex() == 1:
            self.subPanel1.stopReadData()
        self.comm.disconnect()

    def updateDetectedPorts(self):
        selection = self.ui.comPort.currentText()
        if selection == "Refresh":
            self.updateComPortSelection
            self.ui.status.setText("Updated list of available COM ports")
        elif selection == "Autoconnect":
            self.ui.comPort.setCurrentIndex(0)
            self.ui.status.setText("This feature still under construction")
        elif selection == "-------":
            self.ui.comPort.setCurrentIndex(0)
    
    def updateBootUpDelay(self):
        '''
        Creates dialog box to ask user for desired boot up delay.
        This delay wait for Arduino based boards to finish booting up before sending commands.
        '''
        bootUpDelay = float(xml.find("./Settings/BootUpDelay").text)
        data, ok = QtGui.QInputDialog.getDouble(self, "Boot Up Delay", "Boot Up Delay:", bootUpDelay, 0, 60, 3)
        if ok:
            xml.find("./Settings/BootUpDelay").text = str(data)
            xml.write("AeroQuadConfigurator.xml")
 
    def updateCommTimeOut(self):
        '''
        Creates dialog box to ask user for desired comm timeout.
        This is timeout value used by serial drivers to wait for response from device
        '''
        commTimeOut = float(xml.find("./Settings/CommTimeOut").text)
        data, ok = QtGui.QInputDialog.getDouble(self, "Comm Time Out", "Comm Time Out:", commTimeOut, 0, 60, 3)
        if ok:
            xml.find("./Settings/CommTimeOut").text = str(data)
            xml.write("AeroQuadConfigurator.xml")
           
    def exit(self):
        self.comm.disconnect()
        sys.exit(app.exec_())
 
    '''
    Methods for main window housekeeping
    '''         
    def updateComPortSelection(self):
        '''
        Look for available comm ports and updates combo box
        '''
        self.ui.comPort.clear()
        for n in AQSerial.detectPorts(self):
            self.ui.comPort.addItem(n)
        self.ui.comPort.addItem("-------")
        self.ui.comPort.addItem("Autoconnect")
        self.ui.comPort.addItem("Refresh", 1000)
        defaultComPort = xml.find("./Settings/DefaultComPort").text
        commIndex = self.ui.comPort.findText(defaultComPort)
        if commIndex == -1:
            commIndex = 0
        self.ui.comPort.setCurrentIndex(commIndex)
        
    def storeComPortSelection(self):
        '''
        Stores comm port selection to xml file for later recall
        '''
        xml.find("./Settings/DefaultBaudRate").text = self.ui.baudRate.currentText()
        xml.find("./Settings/DefaultComPort").text = self.ui.comPort.currentText()
        xml.write("AeroQuadConfigurator.xml")
               
    def updateBaudRates(self):
        '''
        Reads baud rates from xml and displays in combo box.
        Updates the xml file to display different baud rates
        '''
        defaultBaudRate = xml.find("./Settings/DefaultBaudRate").text
        baudRates = xml.find("./Settings/AvailableBaudRates").text
        baudRate = baudRates.split(',')
        for i in baudRate:
            self.ui.baudRate.addItem(i)
        self.ui.baudRate.setCurrentIndex(baudRate.index(defaultBaudRate))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setStyle("plastique")
    MainWindow = AQMain()
    MainWindow.show()
    sys.exit(app.exec_())