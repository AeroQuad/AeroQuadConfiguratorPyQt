

from PyQt4 import  QtGui
from ui.subpanel.BasePanelController import BasePanelController
from ui.subpanel.pidparametersupdater.PIDParametersUpdaterPanel import Ui_PIDParametersUpdaterPanel
from ui.subpanel.pidparametersupdater.accropidtuning.AccroPIDTuningController import AccroPIDTuningController
from ui.subpanel.pidparametersupdater.stablepidtuning.StablePIDTuningController import StablePIDTuningController

class PIDParametersUpdaterController(QtGui.QWidget, BasePanelController):
    
    BEGINNER_MODE = 'BEGINNER_MODE'
    INTERMEDIATE_MODE = 'INTERMEDIATE_MODE'
    ADVANCED_MODE = 'ADVANCED_MODE'
    
    def __init__(self, vehicle_event_dispatcher, ui_event_dispatcher):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        
        self.ui = Ui_PIDParametersUpdaterPanel()
        self.ui.setupUi(self)
        
        self.ui.pid_type_list.addItem("ACCRO")
        self.ui.pid_type_list.addItem("STABLE")
        self.ui.pid_type_list.clicked.connect(self._pid_list_selection_clicked)
        self.ui.pid_type_list.setCurrentRow(0)
        
        self._accro_pid_tuning_controller = AccroPIDTuningController(vehicle_event_dispatcher, ui_event_dispatcher)
        self.ui.panel_container.addWidget(self._accro_pid_tuning_controller)
        self.ui.panel_container.setCurrentIndex(0)
        
        self._stable_pid_tuning_controller = StablePIDTuningController(vehicle_event_dispatcher, ui_event_dispatcher)
        self.ui.panel_container.addWidget(self._stable_pid_tuning_controller)
        
        self.ui.beginner_radio_button.clicked.connect(self._beginner_radio_button_pressed)
        self.ui.intermediate_radio_button.clicked.connect(self._intermediate_radio_button_pressed)
        self.ui.advance_radio_button.clicked.connect(self._advanced_radio_button_pressed)
        self.ui.beginner_radio_button.setChecked(True)
        
        self._current_pid_tuning_controller = self._accro_pid_tuning_controller
        self._user_level_mode = PIDParametersUpdaterController.BEGINNER_MODE
        
    def _pid_list_selection_clicked(self):
        if (self.ui.pid_type_list.currentItem().text() == 'ACCRO'):
            self._current_pid_tuning_controller = self._accro_pid_tuning_controller
        else:
            self._current_pid_tuning_controller = self._stable_pid_tuning_controller
        
        self.ui.panel_container.setCurrentWidget(self._current_pid_tuning_controller)
        if (self._user_level_mode == PIDParametersUpdaterController.BEGINNER_MODE) :
            self._current_pid_tuning_controller.setBeginnerMode()
        elif (self._user_level_mode == PIDParametersUpdaterController.INTERMEDIATE_MODE) :
            self._current_pid_tuning_controller.setIntermediateMode()
        else :
            self._current_pid_tuning_controller.setAdvancedMode()
        self._current_pid_tuning_controller.start()
        
    def _beginner_radio_button_pressed(self):
        self._user_level_mode = PIDParametersUpdaterController.BEGINNER_MODE
        self._current_pid_tuning_controller.setBeginnerMode()
        
    def _intermediate_radio_button_pressed(self):
        self._user_level_mode = PIDParametersUpdaterController.INTERMEDIATE_MODE
        self._current_pid_tuning_controller.setIntermediateMode()
    
    def _advanced_radio_button_pressed(self):
        self._user_level_mode = PIDParametersUpdaterController.ADVANCED_MODE
        self._current_pid_tuning_controller.setAdvancedMode()

        
    def start(self):
        self._current_pid_tuning_controller.start()

