import matplotlib
import numpy as np

matplotlib.use("Agg")

from app.models import ExportConfig, FitResult, PlotData
from app.plotting import build_linear_plot


def make_plot_data(
    x_uncertainty: np.ndarray | None = None,
    y_uncertainty: np.ndarray | None = None,
) -> PlotData:
    return PlotData(
        x=np.array([1.0, 2.0, 3.0]),
        y=np.array([3.0, 5.0, 7.0]),
        x_uncertainty=x_uncertainty,
        y_uncertainty=y_uncertainty,
        x_label="1/lambda (m^-1)",
        y_label="f (Hz)",
        title="Frequencia em funcao de 1/lambda",
    )


def make_fit_result() -> FitResult:
    return FitResult(
        slope=2.0,
        slope_uncertainty=0.1,
        intercept=1.0,
        intercept_uncertainty=0.2,
        r_squared=1.0,
    )


def test_build_linear_plot_configures_figure_and_fit() -> None:
    figure = build_linear_plot(
        plot_data=make_plot_data(),
        fit_result=make_fit_result(),
        fit_label="Ajuste linear",
        parameter_text="a = 2.0 +/- 0.1",
        export_config=ExportConfig(width_px=1600, height_px=1000, dpi=200),
    )

    axis = figure.axes[0]
    assert figure.dpi == 200
    np.testing.assert_allclose(figure.get_size_inches(), [8.0, 5.0])
    assert axis.get_title() == "Frequencia em funcao de 1/lambda"
    assert axis.get_xlabel() == "1/lambda (m^-1)"
    assert axis.get_ylabel() == "f (Hz)"
    assert len(axis.lines) == 2
    assert {text.get_text() for text in axis.get_legend().get_texts()} == {
        "Dados experimentais",
        "Ajuste linear",
    }
    assert axis.texts[0].get_text() == "a = 2.0 +/- 0.1"


def test_build_linear_plot_draws_optional_error_bars() -> None:
    figure = build_linear_plot(
        plot_data=make_plot_data(
            x_uncertainty=np.array([0.1, 0.1, 0.1]),
            y_uncertainty=np.array([0.2, 0.2, 0.2]),
        ),
        fit_result=make_fit_result(),
        fit_label="Ajuste linear",
        parameter_text="R2 = 1.0",
        export_config=ExportConfig(),
    )

    axis = figure.axes[0]
    assert len(axis.containers) == 1
    assert axis.containers[0].has_xerr is True
    assert axis.containers[0].has_yerr is True
