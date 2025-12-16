# orbital-relations

A lightweight Python package providing closed-form orbital mechanics relations
and a simple numerical root-finding utility for educational use.

The package assumes two-body Keplerian motion and neglects perturbations such
as drag, oblateness, and third-body effects.


## Installation

Clone the repository and install the package in editable mode from the project
root directory:

```bash
pip install -e .
``` 
## Quickstart

```python
from orbital_relations import (
    circular_velocity,
    escape_velocity,
    orbital_period,
    specific_orbital_energy,
    solve_radius_for_circular_velocity,
)

# Earth gravitational parameter (SI units)
mu_earth = 3.986004418e14  # m^3/s^2
r = 6.371e6 + 400e3        # m (LEO altitude)

v_c = circular_velocity(mu_earth, r)
v_e = escape_velocity(mu_earth, r)
T = orbital_period(mu_earth, r)
eps = specific_orbital_energy(mu_earth, r)

r_num, info = solve_radius_for_circular_velocity(
    mu_earth,
    v_target=v_c,
    r_min=6.0e6,
    r_max=8.0e6,
)

print(v_c, v_e, T, eps, r_num)
```
## Documentation

Detailed documentation for each function is provided in the package and module docstrings.

Use Python's built in help system to view documentation, for example:

```python 
help(orbital_relations.circular_velocity)
``` 

## Tests

To execute the tests, run:

```bash
pytest -q
```

A successful test run will report all tests passing with no failures. 