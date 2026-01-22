from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run(centre, r):
    """Requirements for Task 1B"""

    stations = build_station_list()
    print(stations_within_radius(stations, centre, r))
    
centre = (52.2053, 0.1218)
r = 10
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run(centre, r)
