import pytest

from plane.core.helpers import SpinDirections
from plane.core.models import eps, Rotor


def test_rotor():
    rotor = Rotor(1., -5, SpinDirections.CLOCKWISE)
    assert rotor.area == eps


class TestDrone(object):
    pass


class TestStorm(object):
    pass