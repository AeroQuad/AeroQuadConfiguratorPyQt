'''
Created on Feb 24, 2013

@author: Ted Carancho
'''
   
from PyQt4 import QtGui, QtCore
from subpanel.subPanel import SubPanel
from subpanel.menu.menuWindow import Ui_Menu
from utilities.PictureButton import PictureButton

class menu(QtGui.QWidget, SubPanel):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        SubPanel.__init__(self)
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.buttonList = []
        
    def start(self, xmlSubPanel, boardConfiguration):
        self.subPanelName = xmlSubPanel
        self.boardConfiguration = boardConfiguration
        # Clear out all previous menu items
        self.stop()
        menuList = self.xml.findall(self.subPanelName + "/MenuItems/Menu")
        logo = QtGui.QLabel()
        logo.setMaximumSize(QtCore.QSize(800, 250))
        logo.setPixmap(QtGui.QPixmap("./resources/AQLogo.png"))
        logo.setScaledContents(True)
        self.ui.gridLayout.addWidget(logo, 0, 0, 1, 3, QtCore.Qt.AlignCenter)
        # Add menu items listed in XML file
        buttonColumn, buttonRow = 1, 0
        for menuItem in menuList:
            menuButton = PictureButton(self)
            menuButton.setPixmap(QtGui.QPixmap(menuItem.text))
            menuButton.setAlignment(QtCore.Qt.AlignCenter)
            self.buttonList.append(menuButton)
            #self.ui.formLayout.addWidget(menuButton)
            self.ui.gridLayout.addWidget(menuButton, buttonColumn, buttonRow, QtCore.Qt.AlignCenter)
            self.connect(menuButton, QtCore.SIGNAL('clicked()'), self.createMenu(menuItem.get("Name")))
            buttonRow += 1
            if buttonRow == 3:
                buttonRow = 0
                buttonColumn += 1
        
    def createMenu(self, name):
        def menuSelection():
            try:
                self.configurator.selectSubPanel(name)
            except:
                QtGui.QMessageBox.information(self, "Under Construction", "This feature under construction.")
                self.configurator.selectSubPanel("Menu")
        return menuSelection
    
    def stop(self):
        for remove in reversed(range(self.ui.gridLayout.count())):
            self.ui.gridLayout.itemAt(remove).widget().setParent(None)
            
