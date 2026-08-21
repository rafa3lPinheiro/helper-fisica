from dataclasses import dataclass


@dataclass
class FitResult:
    """Linear regression result."""

    slope: float
    slope_uncertainty: float
    intercept: float
    intercept_uncertainty: float
    r_squared: float

