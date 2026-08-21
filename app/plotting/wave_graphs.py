from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from app.models import FitResult, PlotData
from app.physics import (
    format_value_with_uncertainty,
    inverse_harmonic,
    inverse_wavelength,
    inverse_wavelength_uncertainty,
    linear_fit,
)


@dataclass
class WavelengthInverseHarmonicResult:
    plot_data: PlotData
    fit_result: FitResult
    fit_label: str
    parameter_text: str
    expected_slope: float
    expected_slope_uncertainty: float | None
    compatible_with_expected: bool | None


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
    slope = format_value_with_uncertainty(fit_result.slope, fit_result.slope_uncertainty, "m/s")
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


def build_wavelength_inverse_harmonic(
    harmonic_n: NDArray[np.float64],
    lambda_m: NDArray[np.float64],
    length_m: float,
    delta_lambda_m: NDArray[np.float64] | None = None,
    delta_length_m: float | None = None,
) -> WavelengthInverseHarmonicResult:
    x = inverse_harmonic(harmonic_n)
    plot_data = PlotData(
        x=x,
        y=lambda_m,
        x_uncertainty=None,
        y_uncertainty=delta_lambda_m,
        x_label="1/n",
        y_label="lambda (m)",
        title="Comprimento de onda em funcao de 1/n",
    )
    fit_result = linear_fit(x, lambda_m, sigma_y=delta_lambda_m)
    expected_slope = 2 * length_m
    expected_slope_uncertainty = None if delta_length_m is None else 2 * delta_length_m
    compatible = _check_slope_compatibility(
        fit_result,
        expected_slope,
        expected_slope_uncertainty,
    )
    parameter_text = _build_harmonic_parameter_text(
        fit_result,
        expected_slope,
        expected_slope_uncertainty,
        compatible,
    )

    return WavelengthInverseHarmonicResult(
        plot_data=plot_data,
        fit_result=fit_result,
        fit_label="Ajuste linear",
        parameter_text=parameter_text,
        expected_slope=expected_slope,
        expected_slope_uncertainty=expected_slope_uncertainty,
        compatible_with_expected=compatible,
    )


def _check_slope_compatibility(
    fit_result: FitResult,
    expected_slope: float,
    expected_slope_uncertainty: float | None,
) -> bool | None:
    if expected_slope_uncertainty is None:
        return None
    return abs(fit_result.slope - expected_slope) <= (
        fit_result.slope_uncertainty + expected_slope_uncertainty
    )


def _build_harmonic_parameter_text(
    fit_result: FitResult,
    expected_slope: float,
    expected_slope_uncertainty: float | None,
    compatible: bool | None,
) -> str:
    slope = format_value_with_uncertainty(fit_result.slope, fit_result.slope_uncertainty, "m")
    intercept = format_value_with_uncertainty(
        fit_result.intercept,
        fit_result.intercept_uncertainty,
        "m",
    )
    expected = (
        format_value_with_uncertainty(expected_slope, expected_slope_uncertainty, "m")
        if expected_slope_uncertainty is not None
        else f"{expected_slope:.2f} m (incerteza nao informada)"
    )
    compatibility_text = {True: "sim", False: "nao", None: "indeterminada"}[compatible]
    return "\n".join(
        [
            "Ajuste linear:",
            "lambda = a(1/n) + b",
            "",
            f"a = {slope}",
            f"b = {intercept}",
            f"R2 = {fit_result.r_squared:.3f}",
            f"2L = {expected}",
            f"Compativel dentro das incertezas: {compatibility_text}",
        ]
    )
