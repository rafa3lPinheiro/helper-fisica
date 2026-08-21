"""Physics calculation package."""

from app.physics.waves import (
    inverse_harmonic,
    inverse_wavelength,
    sqrt_tension,
    tension_from_mass,
    wave_speed,
)

__all__ = [
    "inverse_harmonic",
    "inverse_wavelength",
    "sqrt_tension",
    "tension_from_mass",
    "wave_speed",
]
