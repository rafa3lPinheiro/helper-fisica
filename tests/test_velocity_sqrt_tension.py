import numpy as np

from app.plotting import build_velocity_sqrt_tension


def test_velocity_sqrt_tension_calculates_values_and_uncertainties() -> None:
    result = build_velocity_sqrt_tension(
        mass_kg=np.array([0.1, 0.2, 0.4, 0.5]),
        frequency_hz=np.array([2.0, 2.8, 4.0, 4.5]),
        lambda_m=np.array([0.5, 0.5, 0.5, 0.5]),
        delta_mass_kg=np.full(4, 0.01),
        delta_frequency_hz=np.full(4, 0.1),
        delta_lambda_m=np.full(4, 0.01),
    )

    np.testing.assert_allclose(result.tension_n, np.array([0.98, 1.96, 3.92, 4.9]))
    np.testing.assert_allclose(result.speed_m_s, np.array([1.0, 1.4, 2.0, 2.25]))
    np.testing.assert_allclose(result.plot_data.x, np.sqrt(result.tension_n))
    assert result.plot_data.x_uncertainty is not None
    assert result.plot_data.y_uncertainty is not None
    assert result.fit_label == "Ajuste linear"
    assert "Inclinação = " in result.parameter_text
    assert "Coeficiente de determinação (R²) = " in result.parameter_text


def test_velocity_sqrt_tension_accepts_custom_gravity() -> None:
    result = build_velocity_sqrt_tension(
        mass_kg=np.array([0.1, 0.2, 0.4]),
        frequency_hz=np.array([2.0, 2.8, 4.0]),
        lambda_m=np.array([0.5, 0.5, 0.5]),
        g=10.0,
    )

    np.testing.assert_allclose(result.tension_n, np.array([1.0, 2.0, 4.0]))


def test_velocity_sqrt_tension_keeps_missing_error_bars_as_none() -> None:
    result = build_velocity_sqrt_tension(
        mass_kg=np.array([0.1, 0.2, 0.4]),
        frequency_hz=np.array([2.0, 2.8, 4.0]),
        lambda_m=np.array([0.5, 0.5, 0.5]),
        delta_mass_kg=np.full(3, 0.01),
        delta_lambda_m=np.full(3, 0.01),
    )

    assert result.plot_data.x_uncertainty is not None
    assert result.plot_data.y_uncertainty is None
