
from ui.subpanel.vehicleconfiguration.VehicleConfigurationController import VehicleConfigurationController
from ui.subpanel.vehicleoverallstatus.VehicleOverallStatusController import VehicleOverallStatusController
from ui.subpanel.accelcalibration.AccelCalibrationController import AccelCalibrationController
from ui.subpanel.receivercalibration.ReceiverCalibrationController import ReceiverCalibrationController
from ui.subpanel.pidparametersupdater.PIDParametersUpdaterController import PIDParametersUpdaterController
from ui.subpanel.motorcommand.MotorCommandController import MotorCommandController
from ui.subpanel.dataplot.DataPlotController import DataPlotController


class PanelsContextBuilder(object):

    VEHICLE_INFORMATION_PANEL_ID = "VEHICLE_INFORMATION_PANEL_ID"
    VEHICLE_STATUS_PANEL_ID = "VEHICLE_STATUS_PANEL_ID"
    ACCEL_CALIBRATION_PANEL_ID = "ACCEL_CALIBRATION_PANEL_ID"
    RECEIVER_CALIBRATION_PANEL_ID = "RECEIVER_CALIBRATION_PANEL_ID"
    PID_TUNING_PANEL_ID = "PID_TUNING_PANEL_ID"
    MOTOR_COMMAND_PANEL_ID = "MOTOR_COMMAND_PANEL_ID"
    SENSOR_PLOT_PANEL_ID = "SENSOR_PLOT_PANEL_ID"
    RECEIVER_PLOT_PANEL_ID = "RECEIVER_PLOT_PANEL_ID"
    
    PANELS_DICTIONNARY = {'' : ''}

    def __init__(self, ui_event_dispatcher, vehicle_event_dispatcher):
        
        PanelsContextBuilder.PANELS_DICTIONNARY[PanelsContextBuilder.VEHICLE_INFORMATION_PANEL_ID] = \
                        VehicleConfigurationController(vehicle_event_dispatcher, ui_event_dispatcher)
        PanelsContextBuilder.PANELS_DICTIONNARY[PanelsContextBuilder.VEHICLE_STATUS_PANEL_ID] = \
                        VehicleOverallStatusController(vehicle_event_dispatcher, ui_event_dispatcher)
                        
        PanelsContextBuilder.PANELS_DICTIONNARY[PanelsContextBuilder.ACCEL_CALIBRATION_PANEL_ID] = \
                        AccelCalibrationController(vehicle_event_dispatcher, ui_event_dispatcher)
        PanelsContextBuilder.PANELS_DICTIONNARY[PanelsContextBuilder.RECEIVER_CALIBRATION_PANEL_ID] = \
                        ReceiverCalibrationController(vehicle_event_dispatcher, ui_event_dispatcher)                        
        PanelsContextBuilder.PANELS_DICTIONNARY[PanelsContextBuilder.PID_TUNING_PANEL_ID] = \
                        PIDParametersUpdaterController(vehicle_event_dispatcher, ui_event_dispatcher)                        
        PanelsContextBuilder.PANELS_DICTIONNARY[PanelsContextBuilder.MOTOR_COMMAND_PANEL_ID] = \
                        MotorCommandController(vehicle_event_dispatcher, ui_event_dispatcher)
        
        PanelsContextBuilder.PANELS_DICTIONNARY[PanelsContextBuilder.SENSOR_PLOT_PANEL_ID] = \
                        DataPlotController(vehicle_event_dispatcher, ui_event_dispatcher)
        PanelsContextBuilder.PANELS_DICTIONNARY[PanelsContextBuilder.RECEIVER_PLOT_PANEL_ID] = \
                        DataPlotController(vehicle_event_dispatcher, ui_event_dispatcher)
        