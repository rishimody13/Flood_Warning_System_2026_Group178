from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def run():
    """Requirements for Task 1D"""

    stations = build_station_list()
    # print(len(rivers_with_station(stations)))
    # print(rivers_with_station(stations))
    print(stations_by_river(stations))
    

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
