from model.VehicleEventDispatcher import VehicleEventDispatcher
from model.Vector3D import Vector3D

class V32VehicleSensorsDataTranslator(object):

    def __init__(self, serial_data, vehicle_event_dispatcher):
        
        splitted_data = serial_data.split(',')
        
        gyro_data = Vector3D(splitted_data[0],splitted_data[1],splitted_data[2])
        vehicle_event_dispatcher.dispatch_event(VehicleEventDispatcher.GYRO_DATA_EVENT, gyro_data)
        
        accel_data = Vector3D(splitted_data[3],splitted_data[4],splitted_data[5])
        vehicle_event_dispatcher.dispatch_event(VehicleEventDispatcher.ACCEL_DATA_EVENT, accel_data)
        
        mag_data = Vector3D(splitted_data[6],splitted_data[7],splitted_data[8])
        vehicle_event_dispatcher.dispatch_event(VehicleEventDispatcher.MAGNETOMETER_DATA_EVENT, mag_data)
        