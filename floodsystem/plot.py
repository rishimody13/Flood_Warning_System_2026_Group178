# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides functionality for plotting water level data
"""

import matplotlib.pyplot as plt


def plot_water_levels(station, dates, levels):
    """Plot water level data for a station against time.
    
    The plot includes horizontal lines for typical low and high water levels.
    
    Args:
        station: MonitoringStation object with attributes name and typical_range
        dates: List of datetime objects
        levels: List of water level values
    """
    
    # Create figure and axis
    plt.figure()
    
    # Plot water level data
    plt.plot(dates, levels, label='Water level')
    
    # Add lines for typical low and high levels if available
    if station.typical_range_consistent():
        low, high = station.typical_range
        plt.axhline(y=low, color='green', linestyle='--', label='Typical low')
        plt.axhline(y=high, color='red', linestyle='--', label='Typical high')
    
    # Label axes and set title
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.title(station.name)
    
    # Add legend
    plt.legend()
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Display the plot
    plt.show()

