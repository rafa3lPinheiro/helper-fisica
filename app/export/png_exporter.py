from pathlib import Path

from matplotlib.figure import Figure

from app.models import ExportConfig


EXPORT_PRESETS = {
    "relatorio": ExportConfig(width_px=1600, height_px=1000, dpi=300),
    "alta_resolucao": ExportConfig(width_px=2400, height_px=1500, dpi=300),
    "rapido": ExportConfig(width_px=1000, height_px=625, dpi=150),
}


def get_export_preset(name: str) -> ExportConfig:
    try:
        preset = EXPORT_PRESETS[name]
    except KeyError as error:
        available = ", ".join(sorted(EXPORT_PRESETS))
        raise ValueError(f"Preset de exportacao desconhecido: {name}. Disponiveis: {available}") from error

    return ExportConfig(
        width_px=preset.width_px,
        height_px=preset.height_px,
        dpi=preset.dpi,
    )


def export_png(
    figure: Figure,
    output_path: str | Path,
    export_config: ExportConfig,
) -> Path:
    path = Path(output_path).with_suffix(".png")
    figure.set_size_inches(
        export_config.width_px / export_config.dpi,
        export_config.height_px / export_config.dpi,
    )
    figure.savefig(
        path,
        dpi=export_config.dpi,
        facecolor="white",
        bbox_inches="tight",
        format="png",
    )
    return path
