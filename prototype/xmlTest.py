'''
Created on Nov 12, 2012

@author: Ted Carancho
'''

import xml.etree.ElementTree as ET

tree = ET.parse('xmlTest.xml')
root = tree.getroot()

# Setup xml objects
subpanelRoot = root.find('Subpanels')
subpanelList = subpanelRoot.findall('Subpanel')

# Create list of subpanel names for menu
subpanelNames = [individualPanel.find('Name').text for individualPanel in subpanelList]

# When user selects subpanel name, lookup subpanel index to access path and class
selectedPanel = "Serial Monitor"
#selectedPanel = "Template"
subpanelIndex = subpanelNames.index(selectedPanel)
subpanel = subpanelList[subpanelIndex]

print(subpanel.find('Path').text)
print(subpanel.find('Class').text)

settings = root.find('Settings')
print(settings.find('DefaultComPort').text)
print(float(settings.find("BootUpDelay").text))
print(float(settings.find('CommTimeOut').text))