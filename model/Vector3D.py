'''
Created on Apr 30, 2013

@author: Kenny
'''

class Vector3D:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
        
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_z(self):
        return self._z
        