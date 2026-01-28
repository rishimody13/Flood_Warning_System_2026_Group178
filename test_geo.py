import pytest
from haversine import haversine
from floodsystem.geo import stations_by_distance, stations_by_river, stations_within_radius, rivers_with_station, rivers_by_station_number
from floodsystem.station import MonitoringStation
#b
"""Unit test for the geo module"""
def test_stations_by_distance():
    p = (0.0, 0.0)
    s1 = MonitoringStation("s1", "m1", "Station 1", (0.0, 1.0), (0.0, 1.0), "River 1", "Town 1")
    s2 = MonitoringStation("s2", "m2", "Station 2", (0.0, 2.0), (0.0, 1.0), "River 2", "Town 2")
    s3 = MonitoringStation("s3", "m3", "Station 3", (1.0, 1.0), (0.0, 1.0), "River 3", "Town 3")

    stations = [s2, s3, s1]
    result = stations_by_distance(stations, p)

    expected = []
    for station in stations:
        expected.append(
            (station.name, station.town, haversine(p, station.coord))
        )

    expected = sorted(expected, key=lambda item: item[2])

    assert len(result) == len(expected)
    for res, exp in zip(result, expected):
        assert res[0] == exp[0]
        assert res[1] == exp[1]
        assert res[2] == pytest.approx(exp[2])
def test_stations_within_radius():
    centre = (0.0, 0.0)
    s1 = MonitoringStation("s1", "m1", "Station 1", (0.0, 0.5), (0.0, 1.0), "River 1", "Town 1")
    s2 = MonitoringStation("s2", "m2", "Station 2", (0.0, 1.0), (0.0, 1.0), "River 2", "Town 2")
    s3 = MonitoringStation("s3", "m3", "Station 3", (0.0, 2.0), (0.0, 1.0), "River 3", "Town 3")

    stations = [s1, s2, s3]
    result = stations_within_radius(stations, centre, 120)

    assert set(result) == {"Station 1", "Station 2"}
def test_rivers_with_station():
    s1 = MonitoringStation("s1", "m1", "Station 1", (0.0, 0.5), (0.0, 1.0), "River A", "Town 1")
    s2 = MonitoringStation("s2", "m2", "Station 2", (0.0, 1.0), (0.0, 1.0), "River B", "Town 2")
    s3 = MonitoringStation("s3", "m3", "Station 3", (0.0, 2.0), (0.0, 1.0), "River A", "Town 3")

    result = rivers_with_station([s1, s2, s3])

    assert result == ["River A", "River B"]
def test_stations_by_river():
    s1 = MonitoringStation("s1", "m1", "Station 1", (0.0, 0.5), (0.0, 1.0), "River A", "Town 1")
    s2 = MonitoringStation("s2", "m2", "Station 2", (0.0, 1.0), (0.0, 1.0), "River B", "Town 2")
    s3 = MonitoringStation("s3", "m3", "Station 3", (0.0, 2.0), (0.0, 1.0), "River A", "Town 3")

    result = stations_by_river([s1, s2, s3])

    assert result["River A"] == ["Station 1", "Station 3"]
    assert result["River B"] == ["Station 2"]
def test_rivers_by_station_number():
    s1 = MonitoringStation("s1", "m1", "Station 1", (0.0, 0.5), (0.0, 1.0), "River A", "Town 1")
    s2 = MonitoringStation("s2", "m2", "Station 2", (0.0, 1.0), (0.0, 1.0), "River B", "Town 2")
    s3 = MonitoringStation("s3", "m3", "Station 3", (0.0, 2.0), (0.0, 1.0), "River A", "Town 3")
    s4 = MonitoringStation("s4", "m4", "Station 4", (0.0, 3.0), (0.0, 1.0), "River A", "Town 4")
    s5 = MonitoringStation("s5", "m5", "Station 5", (0.0, 4.0), (0.0, 1.0), "River C", "Town 5")

    stations = [s1, s2, s3, s4, s5]
    
    # Test N=1: should return all rivers with the highest station count
    result = rivers_by_station_number(stations, 1)
    assert len(result) == 1
    assert result[0][0] == "River A"
    assert result[0][1] == 3
    
    result = rivers_by_station_number(stations, 2)
    assert len(result) == 3
    station_counts = {river: count for river, count in result}
    assert station_counts["River A"] == 3
    assert station_counts["River B"] == 1
    
    # Test N=3: should return all rivers
    result = rivers_by_station_number(stations, 3)
    assert len(result) == 3
    
    # Test N=0: should return empty list
    result = rivers_by_station_number(stations, 0)
    assert result == []
    
    # Test N > number of rivers: should return all rivers
    result = rivers_by_station_number(stations, 10)
    assert len(result) == 3
    
    # Test empty list: should return empty list
    result = rivers_by_station_number([], 1)
    assert result == []
