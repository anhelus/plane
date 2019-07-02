import pytest

from plane.core.motion import UniformAcceleratedMotion, Point


class TestUniformAcceleratedMotion(object):

    def test_1d_compute_new_position(self):
        uniform_accelerated_motion = UniformAcceleratedMotion(2)
        uniform_accelerated_motion.update_position(2)
        assert uniform_accelerated_motion.pos_i == 4
    
    def test_get_trajectory(self):
        point_a = Point(1, 1, 1)
        point_b = Point(2, 2, 2)
        uniform_accelerated_motion = UniformAcceleratedMotion(2)
        assert uniform_accelerated_motion.compute_direction(point_a, point_b) == (1, 1, 1)
        assert len(uniform_accelerated_motion.compute_trajectory_points(point_a, point_b)) == 50