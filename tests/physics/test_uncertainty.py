import numpy as np

from app.physics import (
    inverse_wavelength_uncertainty,
    sqrt_tension_uncertainty,
    tension_uncertainty,
    wave_speed_uncertainty,
)


def test_inverse_wavelength_uncertainty_uses_derivative_formula() -> None:
    result = inverse_wavelength_uncertainty(
        lambda_m=np.array([0.5, 1.0]),
        delta_lambda_m=np.array([0.01, 0.02]),
    )

    np.testing.assert_allclose(result, np.array([0.04, 0.02]))


def test_tension_uncertainty_uses_default_gravity() -> None:
    result = tension_uncertainty(np.array([0.01, 0.02]))

    np.testing.assert_allclose(result, np.array([0.098, 0.196]))


def test_tension_uncertainty_accepts_custom_gravity() -> None:
    result = tension_uncertainty(np.array([0.01, 0.02]), g=10.0)

    np.testing.assert_allclose(result, np.array([0.1, 0.2]))


def test_sqrt_tension_uncertainty_uses_derivative_formula() -> None:
    result = sqrt_tension_uncertainty(
        tension_n=np.array([1.0, 4.0]),
        delta_tension_n=np.array([0.1, 0.2]),
    )

    np.testing.assert_allclose(result, np.array([0.05, 0.05]))


def test_wave_speed_uncertainty_combines_relative_uncertainties() -> None:
    result = wave_speed_uncertainty(
        lambda_m=np.array([2.0]),
        frequency_hz=np.array([10.0]),
        delta_lambda_m=np.array([0.1]),
        delta_frequency_hz=np.array([0.5]),
    )

    np.testing.assert_allclose(result, np.array([np.sqrt(2.0)]))
