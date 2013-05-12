
from PyQt4 import QtGui
from ui.subpanel.BasePanelController import BasePanelController
from ui.subpanel.home.HomePanel import Ui_HomePanel

class HomeController(QtGui.QWidget, BasePanelController):

    def __init__(self, event_dispatcher, protocol_handler):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        self.ui = Ui_HomePanel()
        self.ui.setupUi(self)
        
        self.ui.button_vehicle_status.clicked.connect(self.load_vehicle_status)
        self.ui.button_vehicle_configuration.clicked.connect(self.load_vehicle_configuration)
        self.ui.button_serial_monitor.clicked.connect(self.load_serial_monitor)
        self.ui.button_firmware_download.clicked.connect(self.load_firmware_download)
        self.ui.button_vehicle_setup.clicked.connect(self.load_vehicle_setup)
        
    def load_vehicle_status(self):
        pass
        #self.mainUi.selectSubPanel("Vehicle Status")

    def load_vehicle_configuration(self):
        pass
        #self.mainUi.selectSubPanel("Vehicle Status")
    
    def load_serial_monitor(self):
        pass
        #self.mainUi.selectSubPanel("Vehicle Status")
        
    def load_firmware_download(self):
        pass
    
    def load_vehicle_setup(self):
        pass