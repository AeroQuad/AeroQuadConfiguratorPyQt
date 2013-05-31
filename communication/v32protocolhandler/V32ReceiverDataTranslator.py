from model.VehicleEventDispatcher import VehicleEventDispatcher

class V32ReceiverDataTranslator(object):

    def __init__(self,serial_data, vehicle_event_dispatcher):
        
        splitted_data = serial_data.split(',')
        
        roll = int(splitted_data[0])
        vehicle_event_dispatcher.dispatch_event(VehicleEventDispatcher.RECEIVER_ROLL_PROPERTY_EVENT, roll)
        pitch = int(splitted_data[1])
        vehicle_event_dispatcher.dispatch_event(VehicleEventDispatcher.RECEIVER_PITCH_PROPERTY_EVENT, pitch)
        yaw = int(splitted_data[2])
        vehicle_event_dispatcher.dispatch_event(VehicleEventDispatcher.RECEIVER_YAW_PROPERTY_EVENT, yaw)
        throttle = int(splitted_data[3])
        vehicle_event_dispatcher.dispatch_event(VehicleEventDispatcher.RECEIVER_THROTTLE_PROPERTY_EVENT, throttle)
        mode = int(splitted_data[4])
        vehicle_event_dispatcher.dispatch_event(VehicleEventDispatcher.RECEIVER_MODE_PROPERTY_EVENT, mode)
        aux1 = int(splitted_data[5])
        vehicle_event_dispatcher.dispatch_event(VehicleEventDispatcher.RECEIVER_AUX1_PROPERTY_EVENT, aux1)
        aux2 = int(splitted_data[6])
        vehicle_event_dispatcher.dispatch_event(VehicleEventDispatcher.RECEIVER_AUX2_PROPERTY_EVENT, aux2)
        aux3 = int(splitted_data[7])
        vehicle_event_dispatcher.dispatch_event(VehicleEventDispatcher.RECEIVER_AUX3_PROPERTY_EVENT, aux3)
        
        
        
        