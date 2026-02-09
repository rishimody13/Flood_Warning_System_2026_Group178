# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    threshold = 0.8
    res = stations_level_over_threshold(stations, threshold)
    for item in res:
        print(item[0].name, " ", item[1])
    # Alternative implementation
    # for station in [s for s in stations if s.name in names]:
    #     print("Station name and current level: {}, {}".format(station.name,
    #                                                           station.latest_level))


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
