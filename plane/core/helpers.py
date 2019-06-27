from enum import Enum


class SpinDirections(Enum):
    """ Allowed spinning directions for each rotor.
    """
    CLOCKWISE = 0
    COUNTER_CLOCKWISE = 1


class Frame(object):
    """ A generic reference frame.

    A reference frame represents a three-dimensional space which can be used 
    to model the position of an object.
    """
    def __init__(self, x: float = 0., y: float = 0., z:float = 0) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    @property
    def x(self):
        """ float: The X-position within the frame. """
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
    
    @property
    def y(self):
        """ float: the Y-position within the frame. """
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value
    
    @property
    def z(self):
        """ float: the Z-position within the frame. """
        return self._z
    
    @z.setter
    def z(self, value):
        self._z = value