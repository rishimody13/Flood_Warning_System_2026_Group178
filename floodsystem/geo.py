# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


from .utils import sorted_by_key  # noqa
from .stationdata import build_station_list
from haversine import haversine

def stations_by_distance(stations, p):
    """
    given a list of station objects and a coordinate p, 
    returns a list of (station, distance) tuples, 
    where distance (float) is the distance of the station (MonitoringStation) from the coordinate p. 
    The returned list should be sorted by distance.

    stations is a list of MonitoringStation objects and p is a tuple of floats for the coordinate p
    """
    stations = build_station_list()
    station_distances = []
    for station in stations:
        dist = haversine(p, station.coord)
        station_distances.append((station.name, station.town, dist))
    return sorted_by_key(station_distances, 2)


