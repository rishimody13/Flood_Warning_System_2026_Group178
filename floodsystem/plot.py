# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides functionality for plotting water level data
"""

from matplotlib.dates import date2num
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit


def plot_water_levels_base(station, dates, levels):
    """Create the shared base water-level plot for a station."""
    plt.figure()
    plt.plot(dates, levels, label="Water level")

    if station.typical_range_consistent():
        low, high = station.typical_range
        plt.axhline(y=low, color="green", linestyle="--", label="Typical low")
        plt.axhline(y=high, color="red", linestyle="--", label="Typical high")

    plt.xlabel("Date")
    plt.ylabel("Water level (m)")
    plt.title(station.name)
    plt.xticks(rotation=45)


def plot_water_levels(station, dates, levels):
    """Plot water level data for a station against time.
    
    The plot includes horizontal lines for typical low and high water levels.
    
    Args:
        station: MonitoringStation object with attributes name and typical_range
        dates: List of datetime objects
        levels: List of water level values
    """
    
    plot_water_levels_base(station, dates, levels)

    # Add legend
    plt.legend()
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Display the plot
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    x = date2num(dates)
    plot_water_levels_base(station, dates, levels)
    plt.plot(dates, poly(x - d0), label=f"Degree {p} fit")
    plt.legend()
    plt.tight_layout()
    plt.show()
