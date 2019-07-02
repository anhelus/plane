import numpy as np


# TODO points (e.g. a and b) should be modeled by a simple class


class BaseMotion(object):
    """ Base class for motion.
    """
    def __init__(self, time_i=0, pos_i=0):
        self._time_i = time_i
        self._pos_i = pos_i
    
    @property
    def time_i(self):
        """ initial time """
        return self._time_i
    
    @time_i.setter
    def time_i(self, value):
        self._time_i = value
    
    @property
    def pos_i(self):
        """ initial position """
        return self._pos_i
    
    @pos_i.setter
    def pos_i(self, value):
        self._pos_i = value

    # NOTE can be an abstractmethod
    def update_position(self, t):
        pass
    
    # NOTE can be an abstractmethod
    def compute_trajectory(self, a, b):
        pass


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class UniformAcceleratedMotion(BaseMotion):
    def __init__(self, acc, speed_i=0, time_i=0, pos_i=0):
        super().__init__(time_i, pos_i)
        self._speed_i = speed_i
        self._acc = acc
    
    @property
    def speed_i(self):
        return self._speed_i
    
    @speed_i.setter
    def speed_i(self, value):
        self._speed_i = value
    
    @property
    def acc(self):
        return self._acc
    
    @acc.setter
    def acc(self, value):
        self._acc = value

    def update_position(self, t):
        # TODO implement equation
        # TODO test
        # NOTE this should be extended to three dimensions (i.e. to the whole frame)
        self.pos_i += self.speed_i * (t - self.time_i) + 1 / 2 * self.acc * ((t - self.time_i) ** 2)
    
    def compute_direction(self, a, b):
        """ computes the direction (straight line) to go from a to b"""
        # line direction
        return (b.x - a.x, b.y - a.y, b.z - a.z)

    def compute_trajectory_points(self, a, b, num_points_between=50):
        # NOTE requires refactoring
        v = self.compute_direction(a, b)
        # get a linspace between a.x and b.y
        # TODO modify granularity (steps in linspace)
        x_points = np.linspace(a.x, b.x, num=num_points_between)
        y_points = np.linspace(a.y, b.y, num=num_points_between)
        z_points = np.linspace(a.z, b.z, num=num_points_between)
        # NOTE supposed equals
        # TODO use list comprehension, remove this ugly for
        out_vec = []
        for x in x_points:
            y = (x - a.x) * v[1] / v[2]
            z = ((y - a.y) * v[2] / v[1]) + a.z
            out_vec.append(Point(x, y, z))
        return out_vec


class ConstantMotion(BaseMotion):
    pass


class RandomMotion(BaseMotion):
    pass