
from utilities.observers.Observable import Observable

class UIEventDispatcher(Observable):

    CONNECTION_STATE_CHANGED_EVENT = 'CONNECTION_STATE_CHANGED_EVENT'
    PROTOCOL_HANDLER_EVENT = 'PROTOCOL_HANDLER_EVENT'
    DISPLAY_PANEL_EVENT = 'DISPLAY_PANEL_EVENT'
    
    
    def __init__(self):
        Observable.__init__(self)

    def dispatch_event(self, property_name, value):
        self.dispatch(property_name, value)
        