# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():

    stations = build_station_list()

    update_water_levels(stations)
    threshold = 0.8
    res = stations_level_over_threshold(stations, threshold)
    for item in res:
        print(item[0].name, " ", item[1])
   

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
