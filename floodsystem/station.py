# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


from floodsystem.utils import sorted_by_key


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """checks the typically range data for the stations to see first if it is present
        and the determines whether this is consistent by checking if the low range < high range"""
        if self.typical_range is None:
            return False
        if len(self.typical_range) != 2: #[low, high]
            return False
        low, high = self.typical_range
        if low is None or high is None:
            return False
        return low < high
    
    def relative_water_level(self):
        #check if data is consistent first and if it even exists
        if not self.typical_range_consistent() or self.latest_level is None:
            return None
        low, high = self.typical_range
        #calculater the ratio then
        return (self.latest_level - low) / (high - low)


def inconsistent_typical_range_stations(stations):
    """returns a list of these stations with inconsistent typical range data"""
    inconsistent_stations = [station for station in stations if not station.typical_range_consistent()]
    return inconsistent_stations  # sort by station name
