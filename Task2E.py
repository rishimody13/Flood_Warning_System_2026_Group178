# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels


def run():

    stations = build_station_list()


    station_name = "Cam"
    station = None
    for s in stations:
        if s.name == station_name:
            station = s
            break
    #valid station or not
    if not station:
        print("station {} not found".format(station_name))
        return

    # data over past 2 days
    dt = 2
    dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))
    plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
