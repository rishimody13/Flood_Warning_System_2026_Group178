

import numpy as np
from matplotlib.dates import date2num


def polyfit(dates, levels, p):
    #convert dates to nums as specified
    x = date2num(dates)
    #usual syntax
    d0 = x[0]
    p_coeff = np.polyfit(x - d0, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, d0
