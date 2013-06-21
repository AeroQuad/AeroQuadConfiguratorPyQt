
from PyQt4 import QtGui
from ui.subpanel.pidparametersupdater.pidwidget.PIDWidgetUI import Ui_PIDWidget

class PIDWidgetController(QtGui.QWidget):


    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        self.ui = Ui_PIDWidget()
        self.ui.setupUi(self)
        
        self.set_edit_box_enabled(False)
        
    def show_i_line(self):
        self.ui.i_edit_box.show()
        self.ui.i_label.show()
        self.ui.i_slider.show()
        
    def hide_i_line(self):
        self.ui.i_edit_box.hide()
        self.ui.i_label.hide()
        self.ui.i_slider.hide()
        
    def show_d_line(self):
        self.ui.d_edit_box.show()
        self.ui.d_label.show()
        self.ui.d_slider.show()
        
    def hide_d_line(self):
        self.ui.d_edit_box.hide()
        self.ui.d_label.hide()
        self.ui.d_slider.hide()
        
    def set_edit_box_enabled(self,enabled):
        self.ui.p_edit_box.setEnabled(enabled)
        self.ui.i_edit_box.setEnabled(enabled)
        self.ui.d_edit_box.setEnabled(enabled)
        
        