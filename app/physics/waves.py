import numpy as np
from numpy.typing import NDArray


def inverse_wavelength(lambda_m: NDArray[np.float64]) -> NDArray[np.float64]:
    return 1 / lambda_m


def wave_speed(
    lambda_m: NDArray[np.float64],
    frequency_hz: NDArray[np.float64],
) -> NDArray[np.float64]:
    return lambda_m * frequency_hz


def tension_from_mass(
    mass_kg: NDArray[np.float64],
    g: float = 9.8,
) -> NDArray[np.float64]:
    return mass_kg * g


def sqrt_tension(tension_n: NDArray[np.float64]) -> NDArray[np.float64]:
    return np.sqrt(tension_n)


def inverse_harmonic(n: NDArray[np.float64]) -> NDArray[np.float64]:
    return 1 / n

