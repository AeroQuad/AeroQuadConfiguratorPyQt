'''
Created on Nov 6, 2012

@author: Ted Carancho
'''
import sys

     
from PyQt4 import QtGui #QtCore,
from mainWindow import Ui_MainWindow
from communication.serialCom import AQSerial

from splashScreen import Ui_splashScreen
from subpanel.subCommMonitor.subCommMonitor import Ui_commMonitor

class AQMain(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # TODO: figure out way to configure for different comm types (TCP, MAVLINK, etc) 
        self.comm = AQSerial()
        
        # Connect GUI slots and signals
        self.ui.buttonConnect.clicked.connect(self.connect)
        self.ui.buttonDisconnect.clicked.connect(self.disconnect)
        self.ui.actionExit.triggered.connect(QtGui.qApp.quit)
        self.ui.comPort.currentIndexChanged.connect(self.updateDetectedPorts)
        
        # Default main window conditions
        self.ui.buttonDisconnect.setEnabled(False)
        self.ui.buttonConnect.setEnabled(True)
        self.ui.comPort.setEnabled(True)
        self.ui.baudRate.setEnabled(True)
        self.ui.status.setText("Not connected to AeroQuad")
        self.availablePorts = []
        self.updateComPortSelection()
        self.updateBaudRates()
        
        # TODO: Dynamically load subpanel widget
        self.subPanel = Ui_splashScreen()
        self.subPanel.setupUi(self.subPanel)
        self.ui.subPanel.addWidget(self.subPanel)
        
    """
    Methods which are used for slots
    """
    def connect(self):
        # Setup GUI
        self.ui.buttonDisconnect.setEnabled(True)
        self.ui.buttonConnect.setEnabled(False)
        self.ui.comPort.setEnabled(False)
        self.ui.baudRate.setEnabled(False)
        self.ui.status.setText("Connecting to AeroQuad...")
        # Setup serial port
        self.comm.connect(self.ui.comPort.currentText(), int(self.ui.baudRate.currentText()))
        self.comm.write("!")
        version = self.comm.read()
        if version != "":
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
            self.ui.comPort.setCurrentIndex(0)
            self.ui.status.setText("Updated list of available COM ports")
        elif selection == "Autoconnect":
            self.ui.comPort.setCurrentIndex(0)
            self.ui.status.setText("This feature still under construction")
        elif selection == "-------":
            self.ui.comPort.setCurrentIndex(0)
            
    def exit(self):
        self.comm.disconnect()
        sys.exit(app.exec_())
        
    """
    Methods for main window housekeeping
    """         
    def updateComPortSelection(self):
        self.ui.comPort.clear()
        for n,s in AQSerial.detectPorts(self):
            self.ui.comPort.addItem(s, n)
        self.ui.comPort.addItem("-------")
        self.ui.comPort.addItem("Autoconnect")
        self.ui.comPort.addItem("Refresh", 1000)
        
    def updateBaudRates(self):
        #TODO: Get this from XML config file
        baudRate = ["1200", "9600", "38400", "57600", "111111", "115200"]
        for i in baudRate:
            self.ui.baudRate.addItem(i)
        self.ui.baudRate.setCurrentIndex(baudRate.index("115200"))

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setStyle("plastique")
    MainWindow = AQMain()
    MainWindow.show()
    sys.exit(app.exec_())