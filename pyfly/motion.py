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

    def compute_new_position(self, t):
        pass


class UniformAcceleratedMotion(BaseMotion):
    def __init__(self, acc, speed_i=0):
        super().__init__(self)
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

    def compute_new_position(self, t):
        # TODO implement equation
        # TODO test
        # NOTE this should be extended to three dimensions (i.e. to the whole frame
        return [(pos + self._speed_i * (t - self.time_i) + 1 / 2 * self.acc(t - self.time_i)) for pos in self.pos_i]