
from PyQt4 import QtGui
from ui.subpanel.pidparametersupdater.configsinglelinewidget.ConfigSingleLineWidgetUI import Ui_PIDSingleLineWidget

class ConfigSingleLineWidgetController(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        self.ui = Ui_PIDSingleLineWidget()
        self.ui.setupUi(self)