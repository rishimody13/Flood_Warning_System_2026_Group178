import pytest
from haversine import haversine
from floodsystem.geo import stations_by_distance, stations_by_river, stations_within_radius, rivers_with_station
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
