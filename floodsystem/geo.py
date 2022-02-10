# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
    geographical data.
"""

from .utils import sorted_by_key  # noqa

def rivers_with_station(stations):
    rivers = []
    for station in stations:
        if not station.river in rivers:
            rivers.append(station.river)
    return rivers



def stations_by_river(stations):
    rivers_stations_of_dict = {}
    for rivers in rivers_with_station(stations):
        rivers_stations_of_dict[river] = sorted([station.name for station in stations if stations.river == river])
    return rivers_stations_of_dict
