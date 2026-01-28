# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


from .utils import sorted_by_key  # noqa
from .stationdata import build_station_list
from haversine import haversine

stations = build_station_list()


def stations_by_distance(stations, p):
    """
    given a list of station objects and a coordinate p, 
    returns a list of (station, distance) tuples, 
    where distance (float) is the distance of the station (MonitoringStation) from the coordinate p. 
    The returned list should be sorted by distance.

    stations is a list of MonitoringStation objects and p is a tuple of floats for the coordinate p
    """
    station_distances = []
    for station in stations:
        dist = haversine(p, station.coord)
        station_distances.append((station.name, station.town, dist))
    return sorted_by_key(station_distances, 2)

def stations_within_radius(stations, centre, r):
    within_radius = []
    for station in stations:
        dist = haversine(centre, station.coord)
        if dist <= r:
            within_radius.append(station.name)
    return within_radius

def rivers_with_station(stations):
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    return sorted(rivers)

def stations_by_river(stations):
    river_station = {}
    for station in stations:
        if station.river not in river_station.keys():
            river_station[station.river] = []
        river_station[station.river].append(station.name)
        river_station[station.river].sort()
    return river_station

def rivers_by_station_number(stations, N):
  
    river_station_dict = stations_by_river(stations)
    
    river_counts = [(river, len(station_list)) 
                    for river, station_list in river_station_dict.items()]
    
    river_counts_sorted = sorted_by_key(river_counts, 1, reverse=True)
    
    if N <= 0 or not river_counts_sorted:
        return []
    if N >= len(river_counts_sorted):
        return river_counts_sorted

    nth_count = river_counts_sorted[N - 1][1]
    
    result = [river_tuple for river_tuple in river_counts_sorted 
              if river_tuple[1] >= nth_count]
    
    return result

