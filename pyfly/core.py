# -*- encoding: utf-8 -*-
""" Models used within PyFly.

Within these module, the main models used within PyFly are defined and described.
"""
import math

from enum import Enum

gravity = 9.8
"""float: Gravity value, in meters per square second."""
air_density = 1.0
"""float: Air density value."""


class SpinDirections(Enum):
    """ Possible spinning direction for each rotor.
    """
    CLOCKWISE = 0
    COUNTER_CLOCKWISE = 1


class Frame(object):
    """ A generic reference frame.

    A reference frame represents a three-dimensional space which can be used 
    to model the position of an object.
    """
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z
    
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


class Rotor(object):
    """ Models a single rotor in a UAV.
    """
    def __init__(self, speed, area, spin_direction):
        self._speed = speed
        self._area = area
        self._spin_direction = spin_direction
    
    @property
    def speed(self):
        """ float: Rotor's speed, expressed in meters per second.
        """
        return self._speed
    
    @speed.setter
    def speed(self, value):
        self._speed = value
    
    @property
    def area(self):
        """ float: Rotor's cross-sectional area, expressed in square meters.
        """
        return self._area
    
    @area.setter
    def area(self, value):
        if value < 0:
            raise ValueError('Invalid value for the area of the rotor.')
        else:
            self._area = value
    
    @property
    def spin_direction(self):
        """ :obj: Rotor's spin direction. It can be either clockwise or counter-clockwise.
        """
        return self._spin_direction
    
    @spin_direction.setter
    def spin_direction(self, value):
        self._spin_direction = value
    
    def compute_thrust(self):
        """ Compute thrust for the specified rotor.
        
        Returns:
            A float value which reprents rotor's thrust.
        """
        return (float(air_density) * float(self.area) * float(self.speed**2))
    
    def takeoff(self):
        """ Take-off method.

        In take-off mode, the rotor spins in clockwise direction.
        """
        self.spin_direction = SpinDirections.CLOCKWISE
    
    def land(self):
        """ Land method.

        In landing mode, the rotor spins in counter-clockwise direction.
        """
        self.spin_direction = SpinDirections.COUNTER_CLOCKWISE


class Drone(object):
    """ Class representing a drone.
    """
    def __init__(self, rotors, pitch, roll, mass, current_height=0):
        self._rotors = rotors
        self._pitch = pitch
        self._roll = roll
        self._mass = mass
        self._body_frame = Frame(y=current_height)
    
    @property
    def rotors(self):
        """ :obj:`list` of `Rotor`: The list of drone's rotors. """
        return self._rotors
    
    @rotors.setter
    def rotors(self, value):
        self._rotors = value
    
    @property
    def pitch(self):
        """ float: The pitch angle of the drone. """
        return self._pitch
    
    @pitch.setter
    def pitch(self, value):
        self._pitch = value
    
    @property
    def roll(self):
        """ float: The roll angle of the drone. """
        return self._roll
    
    @roll.setter
    def roll(self, value):
        self._roll = value
    
    @property
    def mass(self):
        """ float: The mass of the drone. """
        return self._mass
    
    @mass.setter
    def mass(self, value):
        if value <= 0:
            raise ValueError('Mass may not be less or equal than zero.')
        else:
            self._mass = value

    @property
    def body_frame(self):
        return self._body_frame
    
    @body_frame.setter
    def body_frame(self, value):
        self._body_frame = value
    
    # TODO model the relationship between the body_frame and the inertial_frame

    def compute_orientation(self):
        """ Computes the orientation of the UAV.
        """
        if self.roll == 0 and self.pitch == 0:
            return 'hovering'
        elif self.roll == 0 and self.pitch in range(1, 90):
            return 'forward'
        elif self.roll == 0 and self.pitch in range(-90, -1):
            return 'backward'
        elif self.roll in range(1, 90) and self.pitch == 0:
            return 'left'
        elif self.roll in range(-90, -1) and self.pitch == 0:
            return 'right'
        elif self.roll in range(1, 90) and self.pitch in range(1, 90):
            return 'positive pitch and roll'
        elif self.roll in range(-90, -1) and self.pitch in range(-90, -1):
            return 'negative pitch and roll'
    
    def compute_required_speed(self, target_height):
        """ Computes the speed required to climb to target height.

        Args:
            target_height: Target height, expressed in meters.
        Returns:
            A float representing the required speed. 
        """
        return math.sqrt(4*gravity*(target_height - self.body_frame.y))
    
    def compute_total_generated_thrust(self, target_height):
        """ Computes the thrust generated to keep the UAV at a certain height.

        NOTE: the '4' constant in the expression is probably referred to 
        the fact that the four rotors have the same area.

        Args:
            target_height: Target height, expressed in meters.

        Returns:
            A float representing the generated thrust.
        """
        return (air_density * sum([rotor.area for rotor in self.rotors]) * (target_height - self.current_height)) \
            + (self.mass * gravity) / (math.cos(self.roll) * math.cos(self.pitch))
    
    def compute_x_generated_thrust(self, target_height):
        """ Computes the thrust generated along the X-axis.

        Args:
            target_height: Target height, expressed in meters.
        
        Returns:
            A float representing thrust generated along the X-axis.
        """
        return math.sqrt(-(self.compute_total_generated_thrust(target_height))**2 
            * math.cos(self.pitch)**2 
            * (1 - 1/cos(self.pitch)**2))
    
    def y_thrusth(self, target_height):
        """ Computes the thrust generated along the Y-axis.

        Args:
            target_height: Target height, expressed in meters.
        
        Returns:
            A float representing thrust generated along the Y-axis.
        """
        return self.required_thrust(target_height) * math.cos(self.pitch) * math.sin(self.roll)
    
    def z_thrust(self, target_height):
        """ Computes the thrust generated along the Z-axis.

        Args:
            target_height: Target height, expressed in meters.
        
        Returns:
            A float representing thrust generated along the Z-axis.
        """
        return self.required_thrust(target_height) * math.cos(self.pitch) * math.cos(self.roll)