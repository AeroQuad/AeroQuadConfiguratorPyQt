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
        if float(self._p) != float(pid_data.get_p()) :
            return False
        elif float(self._i) != float(pid_data.get_i()) :
            return False
        elif float(self._d) != float(pid_data.get_d()) :
            return False
        return True