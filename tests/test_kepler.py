import math
import pytest

from orbital_relations import (
    circular_velocity,
    escape_velocity,
    orbital_period,
    specific_orbital_energy,
)

# Earth constants (SI units)
MU_EARTH = 3.986004418e14  # m^3/s^2
R_EARTH = 6.371e6         # m


def test_circular_velocity_value():
    """Sanity check circular velocity at LEO altitude."""
    r = R_EARTH + 400e3
    v = circular_velocity(MU_EARTH, r)
    # Expected value ~7.67 km/s
    assert math.isclose(v, 7.67e3, rel_tol=1e-2)


def test_escape_velocity_relation():
    """Escape velocity should be sqrt(2) times circular velocity."""
    r = R_EARTH + 400e3
    v_c = circular_velocity(MU_EARTH, r)
    v_e = escape_velocity(MU_EARTH, r)
    assert math.isclose(v_e, math.sqrt(2) * v_c)


def test_orbital_period_positive():
    """Orbital period should be positive for valid inputs."""
    a = R_EARTH + 400e3
    T = orbital_period(MU_EARTH, a)
    assert T > 0


def test_specific_orbital_energy_negative():
    """Bound Keplerian orbits should have negative specific energy."""
    a = R_EARTH + 400e3
    eps = specific_orbital_energy(MU_EARTH, a)
    assert eps < 0


def test_invalid_inputs_raise():
    """Invalid inputs should raise appropriate exceptions."""
    with pytest.raises(ValueError):
        circular_velocity(-1.0, 1.0)

    with pytest.raises(ValueError):
        escape_velocity(1.0, -1.0)

    with pytest.raises(TypeError):
        orbital_period("mu", 1.0)
