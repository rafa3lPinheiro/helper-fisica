import numpy as np
from numpy.typing import NDArray
from scipy.optimize import curve_fit

from app.models import FitResult


def _linear_model(x: NDArray[np.float64], slope: float, intercept: float) -> NDArray[np.float64]:
    return slope * x + intercept


def linear_fit(
    x: NDArray[np.float64],
    y: NDArray[np.float64],
    sigma_y: NDArray[np.float64] | None = None,
) -> FitResult:
    parameters, covariance = curve_fit(
        _linear_model,
        x,
        y,
        sigma=sigma_y,
        absolute_sigma=sigma_y is not None,
    )
    slope, intercept = parameters
    parameter_uncertainties = np.sqrt(np.diag(covariance))

    predicted_y = _linear_model(x, slope, intercept)
    residual_sum_of_squares = np.sum((y - predicted_y) ** 2)
    total_sum_of_squares = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - residual_sum_of_squares / total_sum_of_squares

    return FitResult(
        slope=float(slope),
        slope_uncertainty=float(parameter_uncertainties[0]),
        intercept=float(intercept),
        intercept_uncertainty=float(parameter_uncertainties[1]),
        r_squared=float(r_squared),
    )
