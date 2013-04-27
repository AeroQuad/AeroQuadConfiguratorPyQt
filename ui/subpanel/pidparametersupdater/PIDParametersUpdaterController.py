'''
Created on Nov 28, 2012

@author: Ted Carancho
'''

from PyQt4 import QtCore, QtGui
import time
from ui.subpanel.BasePanelController import BasePanelController
from ui.subpanel.pidparametersupdater.PIDParametersUpdaterPanel import Ui_PIDParametersUpdaterPanel

class PIDParametersUpdaterController(QtGui.QWidget, BasePanelController):
    
    def __init__(self, vehicle_model, message_sender):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        
        self.vehicle_model = vehicle_model
        self.message_sender = message_sender
        
        self.ui = Ui_PIDParametersUpdaterPanel()
        self.ui.setupUi(self)
        self.ui.parameterTable.verticalHeader().setVisible(False)
        self.ui.buttonLoad.setEnabled(False)
        self.ui.buttonSave.setEnabled(False)
        self.ui.buttonUpload.setEnabled(False)
        
        self.ui.listParameterType.clicked.connect(self.updateSelection)
        self.ui.buttonUpload.clicked.connect(self.updateParameters)
        self.ui.buttonSave.clicked.connect(self.underConstruction)
        self.ui.buttonLoad.clicked.connect(self.underConstruction)
        
    def start(self, xmlSubPanel, boardConfiguration):
        self.subPanelName = xmlSubPanel
        self.boardConfiguration = boardConfiguration
        parameterTypes = self.xml.findall(self.subPanelName + "/ParameterType")
        self.ui.listParameterType.clear()
        # Load parameter types
        for parameterType in parameterTypes:
            typeName = parameterType.get("Name")
            if self.checkRequirementsMatch(self.subPanelName + "/ParameterType/[@Name='" + typeName + "']/Requirement"):
                self.ui.listParameterType.addItem(typeName)
        self.ui.listParameterType.setCurrentRow(0)
        self.ui.listParameterType.setFocus()
        descriptionHeader = QtGui.QTableWidgetItem("   Description")
        descriptionHeader.setTextAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft)
        self.ui.parameterTable.setHorizontalHeaderItem(2, descriptionHeader)
        self.updateSelection()
        self.ui.buttonLoad.setEnabled(self.comm.isConnected())
        self.ui.buttonSave.setEnabled(self.comm.isConnected())
        self.ui.buttonUpload.setEnabled(self.comm.isConnected())        
        
    def getXmlLocation(self, value):
        selectedType = str(self.ui.listParameterType.currentItem().text())
        xmlLocation = self.subPanelName + "/ParameterType/[@Name='" + selectedType + "']/" + value
        return xmlLocation
                   
    def updateSelection(self):
        # Generate location of where subpanel values are in XML
        parameterNames = self.xml.findall(self.getXmlLocation("Parameter"))
        
        # If connected, query AeroQuad for parameter values        
        if self.comm.isConnected():
            telemetry = self.xml.find(self.getXmlLocation("Telemetry")).text
            self.comm.write(telemetry)
            time.sleep(0.100)
            response = self.comm.waitForRead()
            telemetryData = response.split(",")
        
        # Fill in each row of parameter table
        rowCount = len(parameterNames)
        self.ui.parameterTable.setRowCount(rowCount)
        for currentRow in range(rowCount):
            # Create a floating point widget for value column
            name = QtGui.QTableWidgetItem(parameterNames[currentRow].get("Name") + "   ")
            data = QtGui.QDoubleSpinBox()
            data.setMinimum(-5000.0)
            data.setMaximum(5000)
            data.setDecimals(2)
            data.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
            # If connected, fill in with telemetry response, otherwise fill in from XML file
            if self.comm.isConnected():
                data.setValue(float(telemetryData[currentRow]))
            else:
                data.setValue(float(parameterNames[currentRow].text))
            description = QtGui.QTableWidgetItem("   " + parameterNames[currentRow].get("Description"))
            self.ui.parameterTable.setItem(currentRow, 0, name)
            self.ui.parameterTable.setCellWidget(currentRow, 1, data)
            self.ui.parameterTable.setItem(currentRow, 2, description)
            
        self.ui.parameterTable.resizeColumnToContents(0)
        self.ui.parameterTable.resizeColumnToContents(1)
        self.ui.parameterTable.resizeColumnToContents(2)
        
    def updateParameters(self):
        parameterData = []
        for row in range(self.ui.parameterTable.rowCount()):
            #parameterData.append(str(self.ui.parameterTable.cellWidget(row, 1).text()))
            data = str(self.ui.parameterTable.cellWidget(row, 1).text())
            data = data.replace(',','.')
            parameterData.append(data)
        command = self.xml.find(self.getXmlLocation("Command")).text
        commandMessage = command + ";".join(parameterData) + ";"
        self.comm.write(commandMessage)
        time.sleep(0.100)
        telemetry = self.xml.find(self.getXmlLocation("Telemetry")).text
        self.comm.write(telemetry)
        time.sleep(0.100)
        response = self.comm.waitForRead()
        if response[-1] == ",":
            response = response[:-1]
        telemetryData = response.split(",")
        parameters = [float(x) for x in parameterData]
        telemetrys = [float(x) for x in telemetryData]
        if parameters == telemetrys:
            updateEEPROM = self.xml.find(self.getXmlLocation("UpdateEEPROM")).text
            self.comm.write(updateEEPROM)
            self.status("Parameter values successfully stored to the AeroQuad")
        else:
            parameterString = ", ".join(map(str, parameters))
            telemetryString = ", ".join(map(str,telemetrys))
            warningMessage = "Unable to verify parameters stored on the AeroQuad\n\nSent:         " + parameterString + "\nReceived: " + telemetryString
            msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Warning, "Verification Error", warningMessage, QtGui.QMessageBox.NoButton, self)
            msgBox.addButton("&Retry", QtGui.QMessageBox.AcceptRole)
            msgBox.addButton("&Abort", QtGui.QMessageBox.RejectRole)
            if msgBox.exec_() == QtGui.QMessageBox.AcceptRole:
                self.status("Retrying parameter storage to AeroQuad...")
                self.updateParameters()
            else:
                self.status("Aborted parameter storage to AeroQuad")

    def underConstruction(self):
        self.status("This feature still under construction")
