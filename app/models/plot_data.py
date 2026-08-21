from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


@dataclass
class PlotData:
    """Transformed data ready for plotting."""

    x: NDArray[np.float64]
    y: NDArray[np.float64]
    x_uncertainty: NDArray[np.float64] | None
    y_uncertainty: NDArray[np.float64] | None
    x_label: str
    y_label: str
    title: str

