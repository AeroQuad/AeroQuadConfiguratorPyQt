
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
        
    def set_title(self, title):
        self.ui.title_label.setText(title)

    def set_line_description(self, description):
        self._line.set_title(description)
                
    def set_bounds(self,min_value, max_value):
        self._line.set_bounds(min_value, max_value)
        
    def set_default(self, default):
        self._line.set_default(default)
        
    def get_value(self):
        return self._line.get_value()