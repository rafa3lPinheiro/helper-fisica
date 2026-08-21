import numpy as np

from app.plotting import build_frequency_inverse_wavelength


def test_frequency_inverse_wavelength_builds_plot_data_and_fit() -> None:
    plot_data, fit_result, fit_label, parameter_text = build_frequency_inverse_wavelength(
        frequency_hz=np.array([2.0, 4.0, 6.0, 8.0]),
        lambda_m=np.array([1.0, 0.5, 1 / 3, 0.25]),
        delta_lambda_m=np.array([0.01, 0.01, 0.01, 0.01]),
        delta_frequency_hz=np.array([0.1, 0.1, 0.1, 0.1]),
    )

    np.testing.assert_allclose(plot_data.x, np.array([1.0, 2.0, 3.0, 4.0]))
    np.testing.assert_allclose(plot_data.x_uncertainty, np.array([0.01, 0.04, 0.09, 0.16]))
    np.testing.assert_array_equal(plot_data.y_uncertainty, np.full(4, 0.1))
    np.testing.assert_allclose(fit_result.slope, 2.0)
    np.testing.assert_allclose(fit_result.intercept, 0.0, atol=1e-12)
    assert fit_label == "Ajuste linear"
    assert "a = (2.00 +/-" in parameter_text
    assert "b = (0.00 +/-" in parameter_text
    assert "R2 = 1.000" in parameter_text


def test_frequency_inverse_wavelength_allows_missing_uncertainties() -> None:
    plot_data, _, _, _ = build_frequency_inverse_wavelength(
        frequency_hz=np.array([2.0, 4.1, 5.8]),
        lambda_m=np.array([1.0, 0.5, 1 / 3]),
    )

    assert plot_data.x_uncertainty is None
    assert plot_data.y_uncertainty is None
