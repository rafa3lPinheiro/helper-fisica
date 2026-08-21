import numpy as np

from app.physics import linear_fit


def test_linear_fit_returns_exact_coefficients_and_r_squared() -> None:
    result = linear_fit(
        x=np.array([0.0, 1.0, 2.0, 3.0]),
        y=np.array([2.0, 5.0, 8.0, 11.0]),
    )

    assert result.slope == 3.0
    assert result.intercept == 2.0
    assert result.r_squared == 1.0


def test_linear_fit_returns_parameter_uncertainties() -> None:
    result = linear_fit(
        x=np.array([1.0, 2.0, 3.0, 4.0, 5.0]),
        y=np.array([3.1, 4.9, 7.2, 8.8, 11.1]),
        sigma_y=np.full(5, 0.2),
    )

    np.testing.assert_allclose(result.slope, 2.02, atol=0.1)
    np.testing.assert_allclose(result.intercept, 1.04, atol=0.3)
    assert result.slope_uncertainty > 0
    assert result.intercept_uncertainty > 0
    assert 0.99 < result.r_squared <= 1.0
