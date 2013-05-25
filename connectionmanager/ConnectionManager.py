
import sys
import logging

from serial import SerialException
from PyQt4 import QtGui
from model.VehicleEventDispatcher import VehicleEventDispatcher
from communication.v4protocolhandler.AQV4ProtocolHandler import AQV4ProtocolHandler
from communication.v32protocolhandler.AQV32ProtocolHandler import AQV32ProtocolHandler

class ConnectionManager(object):

#     too much argument mean... too much responsability
    def __init__(self, app, ui, xml, communicator, event_dispatcher):
        self._app = app
        self._ui = ui
        self._xml = xml
        self._communicator = communicator
        self._event_dispatcher = event_dispatcher 
        
        self._setup_default_COM_port()
        self.update_COM_port_selection()
        self.update_baud_rate()
        
#        self.protocol_handler = ProtocolHandler(communicator, event_dispatcher)
        self.protocol_handler = AQV32ProtocolHandler(communicator, event_dispatcher)
        

    def _setup_default_COM_port(self):
        defaultComPort = self._xml.find("./Settings/DefaultComPort").text
        commIndex = self._ui.comPort.findText(defaultComPort)
        if commIndex == -1:
            commIndex = 0
        self._ui.comPort.setCurrentIndex(commIndex)

    
    
    def connect_to_aeroquad(self):

        self._ui.status.setText("Connecting...")
        self._ui.buttonDisconnect.setEnabled(True)
        self._ui.buttonConnect.setEnabled(False)
        self._ui.comPort.setEnabled(False)
        self._ui.baudRate.setEnabled(False)
        
        self._app.processEvents()
        
        bootupDelay = float(self._xml.find("./Settings/BootUpDelay").text)
        commTimeOut = float(self._xml.find("./Settings/CommTimeOut").text)
        try:
            self._communicator.connect(str(self._ui.comPort.currentText()), int(self._ui.baudRate.currentText()), bootupDelay, commTimeOut)

            self.protocol_handler.unsubscribe_command()
            version = self.protocol_handler.get_flight_software_version()

            if version != "":
                self.save_COM_port_selection()
                self._ui.status.setText("Connected to AeroQuad Flight Software v" + version)
                self._event_dispatcher.dispatch_event(EventDispatcher.CONNECTION_STATE_CHANGED_EVENT, True)
                
                if version == '4.0' :
                    self.protocol_handler = AQV4ProtocolHandler(self._communicator, self._event_dispatcher) 
                    self.protocol_handler.request_board_configuration()

                elif version == '3.2' :
                    self.protocol_handler = AQV32ProtocolHandler(self._communicator, self._event_dispatcher)
                    self.protocol_handler.request_board_configuration()

                else :
                    logging.error("Flight software version " + version + " unsuported")
                    self.disconnectBoard()
                    self._ui.status.setText("Not connected to the AeroQuad")
                
                
                return True
            else:
                self.disconnect_from_aeroquad()
                self._ui.status.setText("Not connected to the AeroQuad")
                if self.manualConnect:
                    QtGui.QMessageBox.information(self, "Connection Error", "Unable to connect to the AeroQuad.  Verify the board is plugged in.\n\nIf it is, try increasing the Boot Up Delay.\nThis is found under File->Preferences->Boot Up Delay.")
                return False
            
        except SerialException:
            self._ui.buttonDisconnect.setEnabled(False)
            self._ui.buttonConnect.setEnabled(True)
            self._ui.comPort.setEnabled(True)
            self._ui.baudRate.setEnabled(True)
            self._ui.status.setText("Connection Failed")
            return False
        
    def disconnect_from_aeroquad(self):
        self._communicator.write(self._xml.find("./Settings/StopTelemetry").text)
        self._communicator.disconnect()
        self._ui.buttonDisconnect.setEnabled(False)
        self._ui.buttonConnect.setEnabled(True)
        self._ui.comPort.setEnabled(True)
        self._ui.baudRate.setEnabled(True)
        self._ui.status.setText("Disconnected from the AeroQuad")
        self._event_dispatcher.dispatch_event(EventDispatcher.CONNECTION_STATE_CHANGED_EVENT, False)

    def search_for_available_COM_port(self):
        selection = self._ui.comPort.currentText()
        if selection == "Refresh":
            self.update_COM_port_selection()
            self._ui.comPort.setCurrentIndex(0)
            self._ui.status.setText("Updated list of available COM ports")
        elif selection == "Autoconnect":
            self.update_COM_port_selection()
            self._ui.comPort.setCurrentIndex(0)
            self._ui.status.setText("Beginning autoconnect...")
            self.try_to_autoconnect()
            
    def try_to_autoconnect(self):
        self.manualConnect = False
        autoConnectState = False
        self.update_COM_port_selection()
        self._ui.comPort.setCurrentIndex(0)
        for port in xrange(self._ui.comPort.count() - 2):
            self._ui.comPort.setCurrentIndex(port)
            self._ui.status.setText("Attempting to connect to " + self._ui.comPort.currentText() + "...")
            if self.connect_to_aeroquad():
                self._ui.status.setText("Autoconnect successful!")
                autoConnectState = True
                break
            else:
                self._ui.status.setText("Autoconnect not successful...")
        if not autoConnectState:
            if sys.platform.startswith("linux"):
                QtGui.QMessageBox.information(self, 'Autoconnect Not Successful', 'Verify that you are a member of the dialout group.  To add yourself to the dialout group, issue the following command in a terminal:\n"sudo adduser yourUserName dialout."\n\nYou may need to restart the Configurator.')
        self.manualConnect = True
    
    def save_boot_delay(self):
        bootUpDelay = float(self._xml.find("./Settings/BootUpDelay").text)
        data, ok = QtGui.QInputDialog.getDouble(self, "Boot Up Delay", "Boot Up Delay:", bootUpDelay, 0, 60, 3)
        if ok:
            self._xml.find("./Settings/BootUpDelay").text = str(data)
            self._xml.write("AeroQuadConfigurator.xml")
 
    def save_connection_timeout_delay(self):
        commTimeOut = float(self._xml.find("./Settings/CommTimeOut").text)
        data, ok = QtGui.QInputDialog.getDouble(self, "Comm Time Out", "Comm Time Out:", commTimeOut, 0, 60, 3)
        if ok:
            self._xml.find("./Settings/CommTimeOut").text = str(data)
            self._xml.write("AeroQuadConfigurator.xml")

    def update_COM_port_selection(self):
        self._ui.comPort.clear()
        for n in self._communicator.detect_ports():
            self._ui.comPort.addItem(n)
        self._ui.comPort.insertSeparator(self._ui.comPort.count())
        self._ui.comPort.addItem("Autoconnect")
        self._ui.comPort.addItem("Refresh")
        
    def save_COM_port_selection(self):
        self._xml.find("./Settings/DefaultBaudRate").text = str(self._ui.baudRate.currentText())
        self._xml.find("./Settings/DefaultComPort").text = str(self._ui.comPort.currentText())
        self._xml.write("AeroQuadConfigurator.xml")
               
    def update_baud_rate(self):
        defaultBaudRate = self._xml.find("./Settings/DefaultBaudRate").text
        baudRates = self._xml.find("./Settings/AvailableBaudRates").text
        baudRate = baudRates.split(',')
        for i in baudRate:
            self._ui.baudRate.addItem(i)
        self._ui.baudRate.setCurrentIndex(baudRate.index(defaultBaudRate))
        
        