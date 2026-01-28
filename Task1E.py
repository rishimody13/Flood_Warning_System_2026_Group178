from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river, rivers_by_station_number


def run():
    """Requirements for Task 1E"""

    stations = build_station_list()
    # print(len(rivers_with_station(stations)))
    # print(rivers_with_station(stations))
    print(rivers_by_station_number(stations, 9))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()