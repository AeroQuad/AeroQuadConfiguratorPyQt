
from ui.subpanel.vehicleconfiguration.VehicleConfigurationController import VehicleConfigurationController
from ui.subpanel.vehicleoverallstatus.VehicleOverallStatusController import VehicleOverallStatusController


class PanelsContextBuilder(object):

    VEHICLE_CONFIGURATIONS_PANEL_ID = "VEHICLE_CONFIGURATIONS_PANEL_ID"
    VEHICLE_OVERALL_STATUS_PANEL_ID = "VEHICLE_OVERALL_STATUS_PANEL_ID"
    
    PANELS_DICTIONNARY = {'' : ''}

    def __init__(self, ui_event_dispatcher, vehicle_event_dispatcher):
        
        PanelsContextBuilder.PANELS_DICTIONNARY[PanelsContextBuilder.VEHICLE_CONFIGURATIONS_PANEL_ID] = \
                        VehicleConfigurationController(vehicle_event_dispatcher, ui_event_dispatcher)
                        
        PanelsContextBuilder.PANELS_DICTIONNARY[PanelsContextBuilder.VEHICLE_OVERALL_STATUS_PANEL_ID] = \
                        VehicleOverallStatusController(vehicle_event_dispatcher, ui_event_dispatcher)
        
        