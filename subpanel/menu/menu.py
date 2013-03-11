'''
Created on Feb 24, 2013

@author: Ted Carancho
'''
   
from PyQt4 import QtGui, QtCore
from subpanel.subPanelTemplate import subpanel
from subpanel.menu.menuWindow import Ui_Menu
from utilities.PictureButton import PictureButton

class menu(QtGui.QWidget, subpanel):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        subpanel.__init__(self)
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.buttonList = []
        
    def start(self, xmlSubPanel, boardConfiguration):
        self.subPanelName = xmlSubPanel
        self.boardConfiguration = boardConfiguration
        menuList = self.xml.findall(self.subPanelName + "/MenuItems/Menu")
        self.menu = {}
        # Clear out all previous menu items
        for remove in reversed(range(self.ui.formLayout.count())):
            self.ui.formLayout.itemAt(remove).widget().setParent(None)
        # Add menu items listed in XML file
        for menuItem in menuList:
            self.menu[menuItem.get("Name")] = menuItem.text
            menuButton = PictureButton(self)
            menuButton.setPixmap(QtGui.QPixmap(menuItem.text))
            menuButton.setAlignment(QtCore.Qt.AlignCenter)
            self.buttonList.append(menuButton)
            self.ui.formLayout.addWidget(menuButton)
            self.connect(menuButton, QtCore.SIGNAL('clicked()'), self.createMenu(menuItem.get("Name")))
        
    def createMenu(self, name):
        def menuSelection():
            self.configurator.selectSubPanel(name)
        return menuSelection
    
    def stop(self):
        for remove in reversed(range(self.ui.formLayout.count())):
            self.ui.formLayout.itemAt(remove).widget().setParent(None)
            
