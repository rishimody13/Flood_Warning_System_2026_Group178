# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consistent():
    s_ok = MonitoringStation("s1", "m1", "S1", (0.0, 0.0), (0.5, 1.5), "R1", "T1")
    s_none = MonitoringStation("s2", "m2", "S2", (0.0, 0.0), None, "R1", "T1")
    s_bad_order = MonitoringStation("s3", "m3", "S3", (0.0, 0.0), (2.0, 1.0), "R1", "T1")
    s_equal = MonitoringStation("s4", "m4", "S4", (0.0, 0.0), (1.0, 1.0), "R1", "T1")

    assert s_ok.typical_range_consistent() is True
    assert s_none.typical_range_consistent() is False
    assert s_bad_order.typical_range_consistent() is False
    assert s_equal.typical_range_consistent() is False

    bad = inconsistent_typical_range_stations([s_ok, s_none, s_bad_order, s_equal])
    assert bad == [s_none, s_bad_order, s_equal]
