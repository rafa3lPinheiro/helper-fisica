import numpy as np

from app.models import PlotData


def test_plot_data_accepts_optional_uncertainties() -> None:
    plot_data = PlotData(
        x=np.array([1.0, 2.0, 3.0]),
        y=np.array([10.0, 20.0, 30.0]),
        x_uncertainty=None,
        y_uncertainty=None,
        x_label="1/lambda (m^-1)",
        y_label="f (Hz)",
        title="Frequencia em funcao do inverso do comprimento de onda",
    )

    np.testing.assert_array_equal(plot_data.x, np.array([1.0, 2.0, 3.0]))
    np.testing.assert_array_equal(plot_data.y, np.array([10.0, 20.0, 30.0]))
    assert plot_data.x_uncertainty is None
    assert plot_data.y_uncertainty is None


def test_plot_data_accepts_uncertainty_arrays() -> None:
    x_uncertainty = np.array([0.1, 0.1, 0.2])
    y_uncertainty = np.array([0.5, 0.5, 0.7])

    plot_data = PlotData(
        x=np.array([1.0, 2.0, 3.0]),
        y=np.array([10.0, 20.0, 30.0]),
        x_uncertainty=x_uncertainty,
        y_uncertainty=y_uncertainty,
        x_label="sqrt(tau) (sqrt(N))",
        y_label="v (m/s)",
        title="Velocidade da onda em funcao da raiz da tensao",
    )

    np.testing.assert_array_equal(plot_data.x_uncertainty, x_uncertainty)
    np.testing.assert_array_equal(plot_data.y_uncertainty, y_uncertainty)

