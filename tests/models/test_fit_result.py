from app.models import FitResult


def test_fit_result_stores_linear_regression_values() -> None:
    result = FitResult(
        slope=12.5,
        slope_uncertainty=0.2,
        intercept=1.5,
        intercept_uncertainty=0.1,
        r_squared=0.98,
    )

    assert result.slope == 12.5
    assert result.slope_uncertainty == 0.2
    assert result.intercept == 1.5
    assert result.intercept_uncertainty == 0.1
    assert result.r_squared == 0.98

