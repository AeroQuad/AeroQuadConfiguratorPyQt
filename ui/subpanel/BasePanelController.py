'''
Created on Nov 19, 2012

@author: Ted Carancho
'''
#import time
#import threading

from abc import abstractmethod
#from abc import ABCMeta


class BasePanelController(object):
    
#    __metaclass__ = ABCMeta

    def __init__(self):
        pass
               
    @abstractmethod
    def initialize(self):
        pass
                
    @abstractmethod                
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def status(self, message):
        '''Send a message to the status bar on the main window'''
        self.mainUi.status.setText(message)
    
#    def checkRequirementsMatch(self, xmlRequirementPath):
#        '''Read requirements for the specified subpanel form the XML config file'''
#        subPanelRequirements = self.xml.findall(xmlRequirementPath)
#        panelRequirements = {}
#        booleanOperation = {}      
#        for requirements in subPanelRequirements:
#            requirement = requirements.text.split(':')
#            if requirement[0] == "All": # Need element 1 populated if "All" detected
#                requirement.append("All")
#            panelRequirements[requirement[0]] = requirement[1].strip()
#            booleanOperation[requirement[0]] = requirements.get("type")
#
#        # Go through each subpanel requirement and check against board configuration
#        # If no boolean type defined, assume AND
#        requirementType = panelRequirements.keys()
#        # If no Requirement found, assume ALL
#        try:
#            if (requirementType[0] == "All"):
#                check = True
#            else:
#                check = any(panelRequirements[requirementType[0]] in s for s in self.boardConfiguration.values())
#                for testRequirement in requirementType[1:]:
#                    if (booleanOperation[testRequirement] == "or") or (booleanOperation[testRequirement] == "OR"):
#                        check = check or any(panelRequirements[testRequirement] in s for s in self.boardConfiguration.values())
#                    else:
#                        check = check and any(panelRequirements[testRequirement] in s for s in self.boardConfiguration.values())
#        except:
#            check = True
#        return check