import numpy as np
from numpy.typing import NDArray


def format_value_with_uncertainty(
    value: float,
    uncertainty: float,
    unit: str = "",
) -> str:
    value = 0.0 if abs(value) < 0.005 else value
    formatted = f"({value:.2f} +/- {uncertainty:.2f})"
    return f"{formatted} {unit}" if unit else formatted


def inverse_wavelength_uncertainty(
    lambda_m: NDArray[np.float64],
    delta_lambda_m: NDArray[np.float64],
) -> NDArray[np.float64]:
    return delta_lambda_m / lambda_m**2


def tension_uncertainty(
    delta_mass_kg: NDArray[np.float64],
    g: float = 9.8,
) -> NDArray[np.float64]:
    return g * delta_mass_kg


def sqrt_tension_uncertainty(
    tension_n: NDArray[np.float64],
    delta_tension_n: NDArray[np.float64],
) -> NDArray[np.float64]:
    return delta_tension_n / (2 * np.sqrt(tension_n))


def wave_speed_uncertainty(
    lambda_m: NDArray[np.float64],
    frequency_hz: NDArray[np.float64],
    delta_lambda_m: NDArray[np.float64],
    delta_frequency_hz: NDArray[np.float64],
) -> NDArray[np.float64]:
    speed = lambda_m * frequency_hz
    relative_uncertainty = np.sqrt(
        (delta_lambda_m / lambda_m) ** 2
        + (delta_frequency_hz / frequency_hz) ** 2
    )
    return speed * relative_uncertainty
