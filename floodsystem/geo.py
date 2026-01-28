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
        station_distances.append((station, dist))
    return sorted_by_key(station_distances, 1)

def stations_within_radius(stations, centre, r):
    """
    gathers data for the distance of stations from a centre and compares it to a radius r 
    to see whether or not they lie within a certain distance from this centre.
    A list of these stations is returned.
    """
    within_radius = []
    for station in stations:
        dist = haversine(centre, station.coord)
        if dist <= r: #dist check
            within_radius.append(station)
    return within_radius

def rivers_with_station(stations):
    """
    determines a set of rivers that have a station assigned to them, avoids duplicaes
    """
    rivers = set() #set to avoid duplicates
    for station in stations:
        rivers.add(station.river)
    return sorted(rivers)

def stations_by_river(stations):
    """
    associates each river from this previously mentioned set to the exact station/s that
    they have along them.
    """
    river_station = {}
    for station in stations:
        if station.river not in river_station.keys(): #check if river not already in dict
            river_station[station.river] = []
        river_station[station.river].append(station.name) #add a station to the list assosciated with the river
        river_station[station.river].sort()
    return river_station

def rivers_by_station_number(stations, N):
    """
    counts the number of stations each river has along them and returns a list of N
    rivers with the greatest number of stations along them. If there are more rivers
    with the same number of stations as the river in Nth place, they are also returned.
    """
  
    river_station_dict = stations_by_river(stations)
    
    river_counts = [(river, len(station_list)) 
                    for river, station_list in river_station_dict.items()] #creates list w tuples of (river, number of stations with that river)
    
    river_counts_sorted = sorted_by_key(river_counts, 1, reverse=True) #sort by number of stations, descending order
    
    if N <= 0 or not river_counts_sorted: #if empty or invalid N, return empty list
        return []
    if N >= len(river_counts_sorted): #all rivers if N greater than number of rivers
        return river_counts_sorted

    nth_count = river_counts_sorted[N - 1][1] #find number of stations for Nth river
    
    result = [river_tuple for river_tuple in river_counts_sorted 
              if river_tuple[1] >= nth_count] #add rivers with station count >= Nth river's count
    
    return result

