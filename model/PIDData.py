class PIDData:

    def __init__(self, p, i, d):
        self._p = p
        self._i = i
        self._d = d
        
    def get_p(self):
        return self._p
    
    def get_i(self):
        return self._i
    
    def get_d(self):
        return self._d