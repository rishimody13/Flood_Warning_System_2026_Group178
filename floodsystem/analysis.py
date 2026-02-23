"""Analysis tools for processing water level data."""

import numpy as np
from matplotlib.dates import date2num


def polyfit(dates, levels, p):
    """Fit a polynomial to level data.

    Args:
        dates: Sequence of datetime objects.
        levels: Sequence of water levels corresponding to ``dates``.
        p: Degree of polynomial fit.

    Returns:
        tuple: ``(poly, d0)`` where ``poly`` is a ``numpy.poly1d`` object
        fit to the shifted date values, and ``d0`` is the date-axis shift
        used in the fit.
    """
    x = date2num(dates)
    d0 = x[0]
    p_coeff = np.polyfit(x - d0, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, d0
