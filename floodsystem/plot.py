# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT


from matplotlib.dates import date2num
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit


def plot_water_levels_base(station, dates, levels):
    #need base function because then we can use this 
    # for both the normal plot and the one with the fit without having to repeat code
    plt.figure()
    plt.plot(dates, levels, label="Water level")

#plots typical high and low values
    if station.typical_range_consistent():
        low, high = station.typical_range
        plt.axhline(y=low, color="green", linestyle="--", label="Typical low")
        plt.axhline(y=high, color="red", linestyle="--", label="Typical high")
    plt.xlabel("Date")
    plt.ylabel("Water level (m)")
    plt.title(station.name)

    plt.xticks(rotation=45)


def plot_water_levels(station, dates, levels):
    #get base function
    plot_water_levels_base(station, dates, levels)

    # then add legend and some formatting stuff
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    x = date2num(dates)
    plot_water_levels_base(station, dates, levels)
    plt.plot(dates, poly(x - d0), label=f"Degree {p} fit")
    plt.legend()
    plt.tight_layout()
    plt.show()
