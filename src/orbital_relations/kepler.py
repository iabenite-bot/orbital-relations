"""
Closed form orbital mechanics relations under the two-body assumption.

All relations assume a point-mass central body and neglect perturbations
such as drag, oblateness, and third-body effects. Units are in SI unless
otherwise specified.
"""
import math 

def circular_velocity(mu, r):
    """
    Calculate the circular orbital velocity.

    Parameters:
    mu : float
        Standard gravitational parameter of the central body (m^3/s^2).
    r : float
        Orbital radius from the center of the central body (m).

    Returns:
    float
        Circular orbital velocity (m/s).
    """
    if not isinstance(mu, (int, float)) or not isinstance(r, (int, float)):
        raise TypeError("Inputs must be numeric values.")
    
    if mu <= 0:
        raise ValueError("Mu must be a positive value.")
    
    if r <= 0:
        raise ValueError("Radius must be a positive value.")
    return math.sqrt(mu / r)

def escape_velocity(mu, r):
    """
    Calculate the escape velocity from a given radius.
    
    Parameters:
    mu : float
        Standard gravitational parameter of the central body (m^3/s^2).
    r : float
        Distance from the center of the central body (m).
        
    Returns:
    float
        Escape velocity (m/s).
    """
    if not isinstance(mu, (int, float)) or not isinstance(r, (int, float)):
        raise TypeError("Inputs must be numeric values.")
    
    if mu <= 0:
        raise ValueError("Mu must be a positive value.")
    
    if r <= 0:
        raise ValueError("Radius must be a positive value.")
    return math.sqrt(2 * mu / r)

def orbital_period(mu, a):
    """
    Calculate the orbital period of a Keplerian orbit.
    
    Parameters:
    mu : float
        Standard gravitational parameter of the central body (m^3/s^2).
    a : float
        Semi-major axis of the orbit (m).
        
    Returns:
    float
        Orbital period (s).
    """
    if not isinstance(mu, (int, float)) or not isinstance(a, (int, float)):
        raise TypeError("Inputs must be numeric values.")
    
    if mu <= 0:
        raise ValueError("Mu must be a positive value.")
    
    if a <= 0:
        raise ValueError("Semi-major axis must be a positive value.")
    return 2 * math.pi * math.sqrt(a**3 / mu)

def specific_orbital_energy(mu, a):
    """
    Calculate the specific orbital energy of a Keplerian orbit.
    
    Parameters:
    mu : float
        Standard gravitational parameter of the central body (m^3/s^2).
    a : float
        Semi-major axis of the orbit (m).
        
    Returns:
    float
        Specific orbital energy (J/kg).
    """
    if not isinstance(mu, (int, float)) or not isinstance(a, (int, float)):
        raise TypeError("Inputs must be numeric values.")
    
    if mu <= 0:
        raise ValueError("Mu must be a positive value.")
    
    if a <= 0:
        raise ValueError("Semi-major axis must be a positive value.")
    return -mu / (2 * a)
