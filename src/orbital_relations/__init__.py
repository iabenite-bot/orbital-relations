
"""
Orbital relations package.

Provides closed form Keplerian orbital mechanics relations and simple
numerical utilities for educational use.
"""

from .kepler import (
    circular_velocity,
    escape_velocity,
    orbital_period,
    specific_orbital_energy,
)

__all__ = [
    "circular_velocity",
    "escape_velocity",
    "orbital_period",
    "specific_orbital_energy",
]
