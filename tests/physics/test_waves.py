import numpy as np

from app.physics import (
    inverse_harmonic,
    inverse_wavelength,
    sqrt_tension,
    tension_from_mass,
    wave_speed,
)


def test_inverse_wavelength_returns_inverse_in_meters() -> None:
    result = inverse_wavelength(np.array([0.5, 1.0, 2.0]))

    np.testing.assert_allclose(result, np.array([2.0, 1.0, 0.5]))


def test_wave_speed_multiplies_wavelength_by_frequency() -> None:
    result = wave_speed(
        lambda_m=np.array([0.5, 1.0]),
        frequency_hz=np.array([10.0, 20.0]),
    )

    np.testing.assert_allclose(result, np.array([5.0, 20.0]))


def test_tension_from_mass_uses_default_gravity() -> None:
    result = tension_from_mass(np.array([0.1, 0.2]))

    np.testing.assert_allclose(result, np.array([0.98, 1.96]))


def test_tension_from_mass_accepts_custom_gravity() -> None:
    result = tension_from_mass(np.array([0.1, 0.2]), g=10.0)

    np.testing.assert_allclose(result, np.array([1.0, 2.0]))


def test_sqrt_tension_returns_square_root_of_tension() -> None:
    result = sqrt_tension(np.array([1.0, 4.0, 9.0]))

    np.testing.assert_allclose(result, np.array([1.0, 2.0, 3.0]))


def test_inverse_harmonic_returns_inverse_of_harmonic_number() -> None:
    result = inverse_harmonic(np.array([1.0, 2.0, 4.0]))

    np.testing.assert_allclose(result, np.array([1.0, 0.5, 0.25]))

