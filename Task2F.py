"""Demonstration program for Task 2F.

For the 5 stations with the highest current relative water level, fetch
the past 2 days of level data and plot:
1) measured levels
2) best-fit degree-4 polynomial
3) typical low/high range lines
"""

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit


def run():
    stations = build_station_list()
    update_water_levels(stations)

    top_stations = stations_highest_rel_level(stations, 5)
    dt = datetime.timedelta(days=2)
    degree = 4

    #ltop_stations is a tuple of (station, level)
    # level not being used here cause its the latest piece of data but comes by default
    # with top_stations. 
    for station, level in top_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        
        if len(dates) < degree + 1:
            continue
        plot_water_level_with_fit(station, dates, levels, degree) 


        


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
