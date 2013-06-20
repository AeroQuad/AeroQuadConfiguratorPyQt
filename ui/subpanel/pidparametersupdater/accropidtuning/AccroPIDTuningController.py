
from ui.subpanel.BasePanelController import BasePanelController

from PyQt4 import QtGui
from ui.subpanel.pidparametersupdater.accropidtuning.AccroPIDTuningPanel import Ui_AccroPIDTuningPanel
from ui.subpanel.pidparametersupdater.pidwidget.PIDWidgetController import PIDWidgetController



class AccroPIDTuningController(QtGui.QWidget, BasePanelController):
    
    def __init__(self, vehicle_event_dispatcher, ui_event_dispatcher):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        
        self.ui = Ui_AccroPIDTuningPanel()
        self.ui.setupUi(self)
        
        self._roll_pid_controller = PIDWidgetController()
        self.ui.main_layout.addWidget(self._roll_pid_controller)
        
        self._picth_pid_controller = PIDWidgetController()
        self.ui.main_layout.addWidget(self._picth_pid_controller)
        
        
#        self.ui.main_layout.addWidget(self._roll_pid_widget,0,0,1,1)
        
    def start(self):
        pass

