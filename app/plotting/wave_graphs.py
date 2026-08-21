import numpy as np
from numpy.typing import NDArray

from app.models import FitResult, PlotData
from app.physics import (
    format_value_with_uncertainty,
    inverse_wavelength,
    inverse_wavelength_uncertainty,
    linear_fit,
)


def build_frequency_inverse_wavelength(
    frequency_hz: NDArray[np.float64],
    lambda_m: NDArray[np.float64],
    delta_lambda_m: NDArray[np.float64] | None = None,
    delta_frequency_hz: NDArray[np.float64] | None = None,
) -> tuple[PlotData, FitResult, str, str]:
    x = inverse_wavelength(lambda_m)
    x_uncertainty = (
        None
        if delta_lambda_m is None
        else inverse_wavelength_uncertainty(lambda_m, delta_lambda_m)
    )
    plot_data = PlotData(
        x=x,
        y=frequency_hz,
        x_uncertainty=x_uncertainty,
        y_uncertainty=delta_frequency_hz,
        x_label="1/lambda (m^-1)",
        y_label="f (Hz)",
        title="Frequencia em funcao do inverso do comprimento de onda",
    )
    fit_result = linear_fit(x, frequency_hz, sigma_y=delta_frequency_hz)
    parameter_text = _build_parameter_text(fit_result)

    return plot_data, fit_result, "Ajuste linear", parameter_text


def _build_parameter_text(fit_result: FitResult) -> str:
    slope = format_value_with_uncertainty(
        fit_result.slope,
        fit_result.slope_uncertainty,
        "m/s",
    )
    intercept = format_value_with_uncertainty(
        fit_result.intercept,
        fit_result.intercept_uncertainty,
        "Hz",
    )
    return "\n".join(
        [
            "Ajuste linear:",
            "f = a(1/lambda) + b",
            "",
            f"a = {slope}",
            f"b = {intercept}",
            f"R2 = {fit_result.r_squared:.3f}",
        ]
    )
