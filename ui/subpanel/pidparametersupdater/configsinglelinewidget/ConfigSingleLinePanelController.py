
from PyQt4 import QtGui
from ui.subpanel.pidparametersupdater.pidwidget.PIDWidgetUI import Ui_PIDWidget
from ui.subpanel.pidparametersupdater.configsinglelinewidget.ConfigSingleLineWidgetController import ConfigSingleLineWidgetController

class ConfigSingleLinePanelController(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        self.ui = Ui_PIDWidget()
        self.ui.setupUi(self)
        
        self._line = ConfigSingleLineWidgetController()
        self.ui.main_layout.addWidget(self._line)
        
    def set_different(self):
        self._line.set_different()
         
    def set_same(self):
        self._line.set_same()
        
    def set_value(self, value):
        self._line.set_value(value)