
import math


class Circle:
    def __init__(self, radius):
        self._radius = radius
        
    @property
    def area(self):
        return 2 * self.radius * math.pi
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @radius.deleter
    def radius(self):
        del self._radius
        
    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter / 2 
