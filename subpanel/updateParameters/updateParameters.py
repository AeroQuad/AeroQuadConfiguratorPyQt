'''
Created on Nov 28, 2012

@author: Ted Carancho
'''

from PyQt4 import QtCore, QtGui
from subpanel.subPanelTemplate import subpanel
from subpanel.updateParameters.updateParametersWindow import Ui_parameterUpdate

class updateParameters(QtGui.QWidget, subpanel):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        subpanel.__init__(self)
        self.ui = Ui_parameterUpdate()
        self.ui.setupUi(self)
        self.ui.parameterTable.verticalHeader().setVisible(False)
        
        self.ui.listParameterType.clicked.connect(self.updateSelection)

    def start(self, xmlSubPanel):
        self.subPanelName = xmlSubPanel
        parameterTypes = self.xml.findall(self.subPanelName + "/ParameterType")
        self.ui.listParameterType.clear()
        for parameterType in parameterTypes:
            typeName = parameterType.get("Name")
            self.ui.listParameterType.addItem(typeName)
        self.ui.listParameterType.setCurrentRow(0)
        self.ui.listParameterType.setFocus()
        self.updateSelection()
            

    def updateSelection(self):
        selectedType = str(self.ui.listParameterType.currentItem().text())
        xmlLocation = self.subPanelName + "/ParameterType/[@Name='" + selectedType + "']/Parameter"
        parameterNames = self.xml.findall(xmlLocation)
        rowCount = len(parameterNames)
        self.ui.parameterTable.setRowCount(rowCount)
        for currentRow in range(rowCount):
            name = QtGui.QTableWidgetItem(parameterNames[currentRow].get("Name") + "   ")
            data = QtGui.QDoubleSpinBox()
            data.setMinimum(-5000.0)
            data.setMaximum(5000)
            data.setDecimals(1)
            data.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
            data.setValue(float(parameterNames[currentRow].text))
            description = QtGui.QTableWidgetItem("   " + parameterNames[currentRow].get("Description"))
            self.ui.parameterTable.setItem(currentRow, 0, name)
            self.ui.parameterTable.setCellWidget(currentRow, 1, data)
            self.ui.parameterTable.setItem(currentRow, 2, description)
        self.ui.parameterTable.resizeColumnToContents(0)
        self.ui.parameterTable.resizeColumnToContents(1)