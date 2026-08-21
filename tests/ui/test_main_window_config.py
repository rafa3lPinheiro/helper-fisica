from app.ui.main_window import GRAPH_COLUMNS, GRAPH_TYPES


def test_mvp_exposes_three_graph_types() -> None:
    assert list(GRAPH_TYPES.values()) == [
        "frequency_inverse_wavelength",
        "wavelength_inverse_harmonic",
        "velocity_sqrt_tension",
    ]


def test_each_graph_type_has_editable_columns() -> None:
    assert all(GRAPH_COLUMNS[key] for key in GRAPH_TYPES.values())
    assert "delta_lambda_m" in dict(GRAPH_COLUMNS["frequency_inverse_wavelength"]).values()
    assert "delta_mass_kg" in dict(GRAPH_COLUMNS["velocity_sqrt_tension"]).values()
