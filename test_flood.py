import pytest
from floodsystem import datafetcher
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold

def test_stations_level_over_threshold():
    s1 = MonitoringStation("s1", "m1", "Station 1", (0.0, 0.5), (0.0, 1.0), "River A", "Town 1")
    s2 = MonitoringStation("s2", "m2", "Station 2", (0.0, 1.0), (0.0, 1.0), "River B", "Town 2")
    s3 = MonitoringStation("s3", "m3", "Station 3", (0.0, 2.0), (0.0, 1.0), "River A", "Town 3")
    s1.latest_level = 0.5
    s2.latest_level = 0.9
    s3.latest_level = 0.7
    stations = [s1, s2, s3]
    result = stations_level_over_threshold(stations, 0.8)
    expected = [(s2, 0.9)]
    assert result == expected

def test_stations_highest_rel_level():
    s1 = MonitoringStation("s1", "m1", "Station 1", (0.0, 0.5), (0.0, 1.0), "River A", "Town 1")
    s2 = MonitoringStation("s2", "m2", "Station 2", (0.0, 1.0), (0.0, 1.0), "River B", "Town 2")
    s3 = MonitoringStation("s3", "m3", "Station 3", (0.0, 2.0), (0.0, 1.0), "River A", "Town 3")
    s1.latest_level = 0.5
    s2.latest_level = 0.9
    s3.latest_level = 0.7
    stations = [s1, s2, s3]
    result = stations_highest_rel_level(stations, 2)
    expected = [(s2, 0.9), (s3, 0.7)]
    assert result == expected
