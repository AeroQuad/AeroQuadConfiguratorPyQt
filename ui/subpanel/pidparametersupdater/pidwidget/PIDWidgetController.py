
from PyQt4 import QtCore, QtGui
from ui.subpanel.pidparametersupdater.pidwidget.PIDWidgetUI import Ui_PIDWidget

class PIDWidgetController(QtGui.QWidget):


    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        self.ui = Ui_PIDWidget()
        self.ui.setupUi(self)