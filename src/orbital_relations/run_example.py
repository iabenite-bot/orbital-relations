from orbital_relations import (
    circular_velocity,
    escape_velocity,
    orbital_period,
    specific_orbital_energy,
    solve_radius_for_circular_velocity,
)

mu_earth = 3.986004418e14  # m^3/s^2
r = 6.371e6 + 400e3        # m

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

print("Circular velocity [m/s]:", v_c)
print("Escape velocity  [m/s]:", v_e)
print("Orbital period   [s]:", T)
print("Specific energy  [J/kg]:", eps)
print("Recovered radius [m]:", r_num)
print("Iterations:", info["iterations"])
