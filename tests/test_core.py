import pytest

from plane.core import Drone, Rotor, SpinDirections, Frame
from plane.motion import UniformAcceleratedMotion


class TestDrone(object):

    def test_takeoff(self):
        """ Test whether, after takeoff, the Y axis of the body frame effectively moves within the inertial frame. """
        rotor_one = Rotor(1., 1., SpinDirections.CLOCKWISE)
        rotor_two = Rotor(1., 1., SpinDirections.CLOCKWISE)
        rotor_three = Rotor(1., 1., SpinDirections.CLOCKWISE)
        rotor_four = Rotor(1., 1., SpinDirections.CLOCKWISE)
        inertial_frame = Frame()
        rotors = [
            rotor_one,
            rotor_two,
            rotor_three,
            rotor_four
        ]
        # Drone is supposed to be at zero height.
        drone = Drone(rotors, 1., 1., 1.)
        assert True
    
    def test_required_speed(self):
        rotors = [
            Rotor(1., 1., SpinDirections.CLOCKWISE),
            Rotor(1., 1., SpinDirections.CLOCKWISE),
            Rotor(1., 1., SpinDirections.CLOCKWISE),
            Rotor(1., 1., SpinDirections.CLOCKWISE)
        ]
        drone = Drone(rotors, 0., 0., 1.)
        assert round(drone.compute_required_speed(10.), 2) == 19.80

    def test_compute_total_generated_thrust(self):
        """  """
        pass