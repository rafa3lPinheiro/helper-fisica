from app.physics import format_value_with_uncertainty


def test_format_value_with_uncertainty_includes_unit() -> None:
    assert format_value_with_uncertainty(12.43, 0.21, "m/s") == "(12.43 ± 0.21) m/s"


def test_format_value_with_uncertainty_can_omit_unit() -> None:
    assert format_value_with_uncertainty(2.0, 0.5) == "(2.00 ± 0.50)"
