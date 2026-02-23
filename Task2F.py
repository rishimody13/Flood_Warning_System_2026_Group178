"""Demonstration program for Task 2F.

For the 5 stations with the highest current relative water level, fetch
the past 2 days of level data and plot:
1) measured levels
2) best-fit degree-4 polynomial
3) typical low/high range lines
"""

import datetime

import matplotlib.pyplot as plt
from matplotlib.dates import date2num

from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stations = build_station_list()
    update_water_levels(stations)

    top_stations = stations_highest_rel_level(stations, 5)
    dt = datetime.timedelta(days=2)
    degree = 4

    for station, _ in top_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        if len(dates) < degree + 1:
            continue

        poly, d0 = polyfit(dates, levels, degree)
        x = date2num(dates)

        plt.figure()
        plt.plot(dates, levels, label="Water level")
        plt.plot(dates, poly(x - d0), label="Degree 4 fit")

        if station.typical_range_consistent():
            low, high = station.typical_range
            plt.axhline(y=low, color="green", linestyle="--", label="Typical low")
            plt.axhline(y=high, color="red", linestyle="--", label="Typical high")

        plt.xlabel("Date")
        plt.ylabel("Water level (m)")
        plt.title(station.name)
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
