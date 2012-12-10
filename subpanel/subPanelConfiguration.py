'''
Created on Dec 9, 2012

@author: Ted Carancho
'''

# Add list of subpanel classes here
from subpanel.commMonitor.commMonitor import commMonitor
from dataPlot.dataPlot import dataPlot
#from subpanel.vehicleConfiguration.vehicleConfiguration import vehicleConfiguration
#from subpanel.vehicleStatus.vehicleStatus import vehicleStatus
#from subpanel.updateParameters.updateParameters import updateParameters

class subPanelConfiguration(object):
    def __init__(self):
        # Append subpanels to subPanelList
        self.subPanelList = []
        commMonitor = commMonitorSubPanel()
        self.subPanelList.append(commMonitor)
       
        gyroData = gyroDataSubPanel()
        self.subPanelList.append(gyroData)
        
# Define a class for your subpanel to store configuration values

class commMonitorSubPanel(object):
    def __init__(self):
        self.name = "Serial Monitor"
        self.module = commMonitor()
        
class gyroDataSubPanel(subPanelConfiguration):
    def __init__(self):
        self.name = "Gyroscope Data"
        self.module = dataPlot()
        self.telemetry = "i"
        self.index = 0
        self.plotsize = 128
        self.plotName = ["Gyro X Axis", "Gyro Y Axis", "Gyro Z Axis"]