
from PyQt4 import QtGui
from ui.subpanel.pidparametersupdater.pidwidget.PIDWidgetUI import Ui_PIDWidget
from ui.subpanel.pidparametersupdater.configsinglelinewidget.ConfigSingleLineWidgetController import ConfigSingleLineWidgetController

class PIDWidgetController(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        self.ui = Ui_PIDWidget()
        self.ui.setupUi(self)
        
        self.p_line = ConfigSingleLineWidgetController()
        self.ui.main_layout.addWidget(self.p_line)
        self.i_line = ConfigSingleLineWidgetController()
        self.ui.main_layout.addWidget(self.i_line)
        self.d_line = ConfigSingleLineWidgetController()
        self.ui.main_layout.addWidget(self.d_line)
        
        self.set_edit_box_enabled(False)
        
    def show_i_line(self):
        self.i_line.show()
        
    def hide_i_line(self):
        self.i_line.hide()
        
    def show_d_line(self):
        self.d_line.show()
        
    def hide_d_line(self):
        self.d_line.hide()
        
    def set_edit_box_enabled(self,enabled):
        self.p_line.ui.edit_box.setEnabled(enabled)
        self.i_line.ui.edit_box.setEnabled(enabled)
        self.d_line.ui.edit_box.setEnabled(enabled)
        
    def set_title(self, title):
        self.ui.title_label.setText(title)
        
    def set_p_different(self):
        self.p_line.set_different()
        
    def set_i_different(self):
        self.i_line.set_different()

    def set_d_different(self):
        self.d_line.set_different()
        
    def set_p_bounds(self, min_value, max_value):
        self.p_line.set_bounds(min_value,max_value)
        
    def set_i_bounds(self, min_value, max_value):
        self.i_line.set_bounds(min_value,max_value)
        
    def set_d_bounds(self, min_value, max_value):
        self.d_line.set_bounds(min_value,max_value)
        
    def set_current_p_value(self,value):
        self.p_line.set_value(value)
        
    def set_current_i_value(self,value):
        self.i_line.set_value(value)
        
    def set_current_d_value(self,value):
        self.d_line.set_value(value)
        
        

        
