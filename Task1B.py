
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run(p):
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()
    sorted_distances = stations_by_distance(stations, p)
    print(sorted_distances[:10])

p = (52.2053, 0.1218)
if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run(p)

#test