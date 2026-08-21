import numpy as np
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

from app.models import ExportConfig, FitResult, PlotData


def build_linear_plot(
    plot_data: PlotData,
    fit_result: FitResult,
    fit_label: str,
    parameter_text: str,
    export_config: ExportConfig,
) -> Figure:
    figsize = (
        export_config.width_px / export_config.dpi,
        export_config.height_px / export_config.dpi,
    )
    figure, axis = plt.subplots(figsize=figsize, dpi=export_config.dpi)
    figure.patch.set_facecolor("white")
    axis.set_facecolor("white")

    axis.errorbar(
        plot_data.x,
        plot_data.y,
        xerr=plot_data.x_uncertainty,
        yerr=plot_data.y_uncertainty,
        fmt="o",
        color="tab:blue",
        capsize=3,
        label="Dados experimentais",
    )

    x_fit = np.linspace(np.min(plot_data.x), np.max(plot_data.x), 100)
    y_fit = fit_result.slope * x_fit + fit_result.intercept
    axis.plot(x_fit, y_fit, color="tab:orange", label=fit_label)

    axis.set_title(plot_data.title)
    axis.set_xlabel(plot_data.x_label)
    axis.set_ylabel(plot_data.y_label)
    axis.grid(True, alpha=0.3)
    axis.legend()
    axis.text(
        0.02,
        0.98,
        parameter_text,
        transform=axis.transAxes,
        verticalalignment="top",
        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.9},
    )
    figure.tight_layout()

    return figure
