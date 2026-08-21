from dataclasses import dataclass


@dataclass
class ExportConfig:
    """Image export size and resolution settings."""

    width_px: int = 1600
    height_px: int = 1000
    dpi: int = 300

