"""
Numerical root-finding utilities for orbital mechanics relations.

Currently implements a bisection solver to compute orbital radius
corresponding to a target circular velocity.
"""
import math 

def solve_radius_for_circular_velocity(mu, v_target, r_min, r_max, tol=1e-10, max_iter=100):
    """
    Solve for orbital radius corresponding to a target circular velocity
    using the bisection method.

    Parameters
    mu : float
        Gravitational parameter [m^3/s^2].
    v_target : float
        Target circular velocity [m/s].
    r_min : float
        Lower bound on radius search interval [m].
    r_max : float
        Upper bound on radius search interval [m].
    tol : float, optional
        Convergence tolerance on the residual.
    max_iter : int, optional
        Maximum number of bisection iterations.

    Returns
    r : float
        Computed orbital radius [m].
    info : dict
        Dictionary containing iteration count and residual history.
    """
    # Type checks 
    for name, val in {
        "mu": mu,
        "v_target": v_target,
        "r_min": r_min,
        "r_max": r_max,
        "tol": tol,
    }.items():
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if not isinstance(max_iter, int):
        raise TypeError("max_iter must be an integer")

    # Domain checks
    if mu <= 0:
        raise ValueError("mu must be positive")

    if v_target <= 0:
        raise ValueError("v_target must be positive")

    if r_min <= 0 or r_max <= 0:
        raise ValueError("r_min and r_max must be positive")

    if r_max <= r_min:
        raise ValueError("r_max must be greater than r_min")

    if tol <= 0:
        raise ValueError("tol must be positive")

    # Define residual function 
    def residual(r):
        return math.sqrt(mu / r) - v_target

    f_min = residual(r_min)
    f_max = residual(r_max)

    if f_min * f_max > 0:
        raise ValueError("Root is not bracketed in [r_min, r_max]")

    residual_history = []

    # Bisection loop 
    for k in range(max_iter):
        r_mid = 0.5 * (r_min + r_max)
        f_mid = residual(r_mid)
        residual_history.append(f_mid)

        if abs(f_mid) < tol:
            return r_mid, {"iterations": k + 1, "residuals": residual_history}

        if f_min * f_mid < 0:
            r_max = r_mid
            f_max = f_mid
        else:
            r_min = r_mid
            f_min = f_mid

    # If we reach here, we did not converge
    return r_mid, {"iterations": max_iter, "residuals": residual_history}

