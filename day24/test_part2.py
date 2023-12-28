import pytest
from day24.part2 import Particle, solve_given_vr_wr, check_collides

# In the example above, you can achieve this by moving to position 24, 13, 10
# and throwing the rock at velocity -3, 1, 2. If you do this, you will hit
# every hailstone as follows:

# Hailstone: 19, 13, 30 @ -2, 1, -2
# Collision time: 5
# Collision position: 9, 18, 20

# Hailstone: 18, 19, 22 @ -1, -1, -2
# Collision time: 3
# Collision position: 15, 16, 16

# Hailstone: 20, 25, 34 @ -2, -2, -4
# Collision time: 4
# Collision position: 12, 17, 18

# Hailstone: 12, 31, 28 @ -1, -2, -1
# Collision time: 6
# Collision position: 6, 19, 22

# Hailstone: 20, 19, 15 @ 1, -5, -3
# Collision time: 1
# Collision position: 21, 14, 12


def test_solver_1():
    hail_1 = Particle((20, 19, 15), (1, -5, -3))
    hail_2 = Particle((18, 19, 22), (-1, -1, -2))
    v_r = 1
    w_r = 2
    solved, t, delta_1, u_r = solve_given_vr_wr(hail_1, hail_2, v_r, w_r)
    assert solved
    assert t == 1
    assert delta_1 == 2
    assert u_r == -3


def test_solver_2():
    hail_1 = Particle((19, 13, 30), (-2, 1, -2))
    hail_2 = Particle((18, 19, 22), (-1, -1, -2))
    v_r = 1
    w_r = 2
    solved, t, delta_1, u_r = solve_given_vr_wr(hail_1, hail_2, v_r, w_r)
    assert solved
    assert t == 5
    assert delta_1 == -2
    assert u_r == -3


@pytest.mark.parametrize(
    "hailstone, expected",
    [
        (Particle((19, 13, 30), (-2, 1, -2)), True),
        (Particle((18, 19, 22), (-1, -1, -2)), True),
        (Particle((20, 19, 15), (1, -5, -3)), True),
        (Particle((20, 25, 34), (-2, -2, -4)), True),
        (Particle((12, 31, 28), (-1, -2, -1)), True),
        (Particle((24, 13, 10), (-3, 1, 2)), True),
    ],
)
def test_check_collides(hailstone, expected):
    rock = Particle((24, 13, 10), (-3, 1, 2))
    assert check_collides(rock, hailstone) == expected
