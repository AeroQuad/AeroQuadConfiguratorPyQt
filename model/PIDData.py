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
    
    def is_equals(self, pid_data):

        p1 = int(float(self._p) * 100)        
        p2 = int(float(pid_data.get_p()) * 100)
        if p1 != p2 :
            return False
        
        i1 = int(float(self._i) * 100)        
        i2 = int(float(pid_data.get_i()) * 100)
        if i1 != i2:
            return False
        
        d1 = int(float(self._d) * 100)        
        d2 = int(float(pid_data.get_d()) * 100)
        if d1 != d2:
            return False
        
        return True
    