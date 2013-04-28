'''
Created on Apr 22, 2013

@author: Kenny
'''
import logging
import types

class Observable(object):
    def __init__(self):
        self._listeners = {}
         
    def register(self, listener, events=None):
        if events is not None and type(events) not in (types.TupleType,types.ListType):
            events = (events,)
              
        self._listeners[listener] = events
         
    def dispatch(self, event=None, msg=None):
        for listener,events in self._listeners.items():
            if events is None or event is None or event in events:
                try:
                    listener(self,event,msg)
                except (Exception,):
                    self.unregister(listener)
                    errmsg = "Exception in message dispatch: Handler '{0}' unregistered for event '{1}'  ".format(listener.func_name,event)
                    logging.exception(errmsg)
             
    def unregister(self,listener):
        del self._listeners[listener]


