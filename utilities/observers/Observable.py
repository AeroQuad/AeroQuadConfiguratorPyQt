
class Observable(object):
    def __init__(self):
        self._listeners = {}
         
    def register(self, listener, property_key):
        self._listeners.setdefault(property_key, []).append(listener)
         
    def dispatch(self, property_key, msg):
        if property_key in self._listeners: 
            for function in self._listeners[property_key] :
                function(property_key, msg)


