from . import datafetcher
from . import station
from floodsystem.utils import sorted_by_key
def stations_level_over_threshold(stations, tol):
    stations_over_threshold = []
    for station in stations:
        relative_level = station.relative_water_level()
        if relative_level is not None and relative_level > tol:
            stations_over_threshold.append((station, relative_level))
    return sorted_by_key(stations_over_threshold, 1, reverse=True)

def stations_highest_rel_level(stations, N):
    stations_with_rel_level = []
    for station in stations:
        relative_level = station.relative_water_level()
        if relative_level is not None:
            stations_with_rel_level.append((station, relative_level))
    return sorted_by_key(stations_with_rel_level, 1, reverse=True)[:N] #sort then index and get first N,
#reverse to get highest first