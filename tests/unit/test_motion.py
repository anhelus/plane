import pytest

from plane.core.motion import UniformAcceleratedMotion


class TestUniformAcceleratedMotion(object):

    def test_1d_compute_new_position(self):
        uniform_accelerated_motion = UniformAcceleratedMotion(2)
        uniform_accelerated_motion.update_position(2)
        assert uniform_accelerated_motion.pos_i == 4