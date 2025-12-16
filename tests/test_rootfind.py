import math
import pytest

from orbital_relations import solve_radius_for_circular_velocity

# Earth gravitational parameter (SI units)
MU_EARTH = 3.986004418e14  # m^3/s^2


def test_rootfind_matches_analytic_solution():
    """
    Numerical solution for radius should match the analytic
    circular-orbit relation r = mu / v^2.
    """
    v_target = 7.67e3  # m/s (LEO-scale)
    r_exact = MU_EARTH / v_target**2

    r_num, info = solve_radius_for_circular_velocity(
        MU_EARTH,
        v_target,
        r_min=6.0e6,
        r_max=8.0e6,
        tol=1e-8,
    )

    assert math.isclose(r_num, r_exact, rel_tol=1e-6)
    assert info["iterations"] > 0
    assert len(info["residuals"]) == info["iterations"]


def test_root_not_bracketed_raises():
    """
    Bisection should fail if the root is not bracketed.
    """
    with pytest.raises(ValueError):
        solve_radius_for_circular_velocity(
            MU_EARTH,
            7.67e3,
            r_min=1.0,
            r_max=2.0,
        )


def test_invalid_inputs_raise():
    """
    Invalid inputs should raise appropriate exceptions.
    """
    with pytest.raises(ValueError):
        solve_radius_for_circular_velocity(-1.0, 1.0, 1.0, 2.0)

    with pytest.raises(ValueError):
        solve_radius_for_circular_velocity(1.0, -1.0, 1.0, 2.0)

    with pytest.raises(TypeError):
        solve_radius_for_circular_velocity("mu", 1.0, 1.0, 2.0)
