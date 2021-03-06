# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

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
        """Checks consistency in typical range of river level"""

        # Check range is not None
        if self.typical_range is None:
            return False
        # Check low range is higher than high range
        else:
            low, high = self.typical_range
            if low > high:
                return False
        # Return True if passing test
            else:
                return True

    def relative_water_level(self):
        """Returns latest water level as a fraction of typical range"""
        if self.typical_range_consistent() == False:
            return None
        if self.latest_level == None:
            return None
        else:
            low = min(self.typical_range)
            high = max(self.typical_range)
            typ_range = high - low
            fraction = (self.latest_level - low) / typ_range
            return fraction

def inconsistent_typical_range_stations(stations):
    """Takes a list of MonitoringStation objects and returns a list
    of stations with inconsistent typical range data"""
    
    inconsistent_list = []
    for station in stations:
        if station.typical_range_consistent is False:
            inconsistent_list.append(station)
    
    return inconsistent_list