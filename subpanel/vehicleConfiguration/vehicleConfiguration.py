'''
Created on Dec 5, 2012

@author: Ted Carancho
'''

from PyQt4 import QtCore, QtGui
from subpanel.subPanelTemplate import subpanel
from subpanel.vehicleConfiguration.vehicleConfigurationWindow import Ui_vehicleConfiguration

class vehicleConfiguration(QtGui.QWidget, subpanel):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        subpanel.__init__(self)
        self.ui = Ui_vehicleConfiguration()
        self.ui.setupUi(self)
        self.image = QtGui.QPixmap("./resources/Quad+.png")
        
        self.ui.updateButton.clicked.connect(self.updateConfiguration)

    def resizeEvent(self, event):
        self.displayVehicle()
        
    def displayVehicle(self):
        width = self.ui.configView.width() - 50
        height = self.ui.configView.height() - 50
        scaledImage = self.image.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.ui.configView.setPixmap(scaledImage)
        self.ui.configView.setAlignment(QtCore.Qt.AlignCenter)
        
    def start(self, xmlSubPanel, boardConfiguration):
        self.boardConfiguration = boardConfiguration
        if self.comm.isConnected():       
            for spec in self.boardConfiguration:
                if "Flight Config: " in spec:
                    vehicle = spec.split("Flight Config: ")
                    vehicleFile = self.xml.find(xmlSubPanel + "/VehicleGraphics/Vehicle/[@Name='" + vehicle[1] + "']")
                    self.image = QtGui.QPixmap(vehicleFile.text)
                    self.displayVehicle()
                    break
            
            # Populate configuration list
            rowCount = len(self.boardConfiguration)
            self.ui.configSpecs.clear()
            self.ui.configSpecs.setRowCount(rowCount)
            self.ui.configSpecs.setColumnCount(1)
            
            for currentRow in range(rowCount):
                spec = QtGui.QTableWidgetItem("   " + self.boardConfiguration[currentRow])
                spec.setTextColor(QtCore.Qt.white)
                spec.setFlags(QtCore.Qt.ItemIsTristate)
                self.ui.configSpecs.setItem(currentRow, 0, spec)
            self.ui.configSpecs.resizeColumnToContents(0)
        else:
            self.ui.configSpecs.clear()
            self.ui.configSpecs.setRowCount(2)
            self.ui.configSpecs.setColumnCount(1)
            messageList = ["Connect AeroQuad to Retrieve", "Vehicle Configuration..."]
            for row in range(len(messageList)):
                message = QtGui.QTableWidgetItem(messageList[row])                           
                message.setTextColor(QtCore.Qt.white)
                message.setTextAlignment(QtCore.Qt.AlignCenter)
                message.setFlags(QtCore.Qt.ItemIsTristate)
                self.ui.configSpecs.setItem(row, 0, message)
                self.ui.configSpecs.resizeColumnToContents(0)
        
    def updateConfiguration(self):
        if self.comm.isConnected():
            self.status("Updating Vehicle Status...")
            configCommand = self.xml.find(".Settings/BoardConfiguration").text
            self.comm.write(configCommand)
            rowCount = int(self.comm.waitForRead())
            self.ui.configSpecs.clear()
            self.ui.configSpecs.setRowCount(rowCount)
            self.ui.configSpecs.setColumnCount(1)
            for currentRow in range(rowCount):
                config = self.comm.waitForRead()
                spec = QtGui.QTableWidgetItem("   " + config)
                spec.setTextColor(QtCore.Qt.white)
                spec.setFlags(QtCore.Qt.ItemIsTristate)
                self.ui.configSpecs.setItem(currentRow, 0, spec)
            self.ui.configSpecs.resizeColumnToContents(0)
            self.status("Vehicle Status Updated")
        else:
            self.status("Connect to the AeroQuad first to update status.")
