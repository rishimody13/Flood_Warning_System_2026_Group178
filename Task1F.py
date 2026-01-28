from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
def run():
    """Requirements for Task 1E"""

    stations = build_station_list()
    print(inconsistent_typical_range_stations(stations))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()