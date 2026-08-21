from app.models import ExportConfig


def test_export_config_uses_report_defaults() -> None:
    config = ExportConfig()

    assert config.width_px == 1600
    assert config.height_px == 1000
    assert config.dpi == 300

