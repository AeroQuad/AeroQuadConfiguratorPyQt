
from ui.subpanel.dataplot.DataPlotController import DataPlotController

class ReceiverDataPlotContoller(DataPlotController):


    def __init__(self, vehicle_event_dispatcher, ui_event_dispatcher):
        DataPlotController.__init__(self)
        