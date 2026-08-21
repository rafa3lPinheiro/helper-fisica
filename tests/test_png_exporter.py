import matplotlib
import numpy as np
import pytest

matplotlib.use("Agg")

from matplotlib import pyplot as plt

from app.export import export_png, get_export_preset
from app.models import ExportConfig


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("relatorio", (1600, 1000, 300)),
        ("alta_resolucao", (2400, 1500, 300)),
        ("rapido", (1000, 625, 150)),
    ],
)
def test_get_export_preset_returns_expected_config(
    name: str,
    expected: tuple[int, int, int],
) -> None:
    config = get_export_preset(name)

    assert (config.width_px, config.height_px, config.dpi) == expected


def test_get_export_preset_returns_independent_config() -> None:
    first = get_export_preset("relatorio")
    second = get_export_preset("relatorio")
    first.width_px = 10

    assert second.width_px == 1600


def test_get_export_preset_rejects_unknown_name() -> None:
    with pytest.raises(ValueError, match="Preset de exportacao desconhecido"):
        get_export_preset("inexistente")


def test_export_png_creates_png_and_applies_config(tmp_path) -> None:
    figure, axis = plt.subplots()
    axis.plot(np.array([0.0, 1.0]), np.array([0.0, 1.0]))
    config = ExportConfig(width_px=800, height_px=500, dpi=100)

    output = export_png(figure, tmp_path / "grafico.csv", config)

    assert output == tmp_path / "grafico.png"
    assert output.exists()
    assert output.read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
    np.testing.assert_allclose(figure.get_size_inches(), [8.0, 5.0])
    plt.close(figure)
