
from PyQt4 import QtGui
from ui.subpanel.pidparametersupdater.configsinglelinewidget.ConfigSingleLineWidgetUI import Ui_PIDSingleLineWidget

class ConfigSingleLineWidgetController(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        self.ui = Ui_PIDSingleLineWidget()
        self.ui.setupUi(self)
        
        self._min_bound = 0
        self._max_bound = 1000
        
        self.set_different()
        
        self.ui.slider.sliderReleased.connect(self._slider_released)
        self.ui.slider.sliderMoved.connect(self._slider_move)
        self.ui.edit_box.valueChanged.connect(self._edit_box_value_changed)
        self._change_listener = self.defaul_change_listener_notifier
        
    def set_different(self):
        self.ui.sync_feedback_label.setStyleSheet("background-color: rgb(255, 255, 0);")
        
    def set_same(self):
        self.ui.sync_feedback_label.setStyleSheet("background-color: rgb(0, 255, 0);")
        
    def set_title(self,title):
        self.ui.title_label.setText(title)
        
    def set_default(self, default):
        self.ui.default_label.setText(str(default))
        
    def set_bounds(self, min_value, max_value):
        self._min_bound = min_value
        self._max_bound = max_value
        self.ui.slider.setMinimum(self._min_bound)
        self.ui.slider.setMaximum(self._max_bound)
        self.ui.edit_box.setMinimum(self._min_bound)
        self.ui.edit_box.setMaximum(self._max_bound)
    
    def set_value(self,value):
        floatValue = float(value)
        self.ui.slider.setValue(floatValue)
        self.ui.edit_box.setValue(floatValue)
    
    def get_value(self):
        return self.ui.edit_box.value()
        
    def _slider_released(self):
        self.set_different()
        self._change_listener()
        
    def _slider_move(self):
        value = self.ui.slider.value()
        self.ui.edit_box.setValue(value)
        self.set_different()
        
    def _edit_box_value_changed(self):
        value = self.ui.edit_box.value()
        self.ui.slider.setValue(value)
        self._change_listener()
        
    def set_change_listener(self, change_listener):
        self._change_listener = change_listener
        
    def defaul_change_listener_notifier(self):
        print 'No listener set on this config line widget'
        
        
        