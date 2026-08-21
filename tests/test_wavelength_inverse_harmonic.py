import numpy as np

from app.plotting import build_wavelength_inverse_harmonic


def test_wavelength_inverse_harmonic_calculates_expected_slope_and_compatibility() -> None:
    result = build_wavelength_inverse_harmonic(
        harmonic_n=np.array([1.0, 2.0, 4.0, 5.0]),
        lambda_m=np.array([1.21, 0.60, 0.31, 0.24]),
        length_m=0.6,
        delta_lambda_m=np.full(4, 0.02),
        delta_length_m=0.01,
    )

    np.testing.assert_allclose(result.plot_data.x, np.array([1.0, 0.5, 0.25, 0.2]))
    assert result.plot_data.x_uncertainty is None
    np.testing.assert_array_equal(result.plot_data.y_uncertainty, np.full(4, 0.02))
    np.testing.assert_allclose(result.expected_slope, 1.2)
    np.testing.assert_allclose(result.expected_slope_uncertainty, 0.02)
    assert result.compatible_with_expected is True
    assert "2L = (1.20 +/- 0.02) m" in result.parameter_text
    assert "Compativel dentro das incertezas: sim" in result.parameter_text


def test_wavelength_inverse_harmonic_marks_incompatible_result() -> None:
    result = build_wavelength_inverse_harmonic(
        harmonic_n=np.array([1.0, 2.0, 4.0, 5.0]),
        lambda_m=np.array([1.21, 0.60, 0.31, 0.24]),
        length_m=0.8,
        delta_lambda_m=np.full(4, 0.02),
        delta_length_m=0.01,
    )

    assert result.compatible_with_expected is False
    assert "Compativel dentro das incertezas: nao" in result.parameter_text


def test_wavelength_inverse_harmonic_keeps_compatibility_indeterminate_without_length_uncertainty() -> None:
    result = build_wavelength_inverse_harmonic(
        harmonic_n=np.array([1.0, 2.0, 4.0, 5.0]),
        lambda_m=np.array([1.21, 0.60, 0.31, 0.24]),
        length_m=0.6,
    )

    assert result.expected_slope_uncertainty is None
    assert result.compatible_with_expected is None
    assert "incerteza nao informada" in result.parameter_text
