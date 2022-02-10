# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
    geographical data.
"""

from inspect import CORO_CLOSED
from unicodedata import name

# from sklearn import utils
from .utils import sorted_by_key  # noqa
from haversine import haversine

def rivers_with_station(stations):
    rivers = []
    for station in stations:
        if not station.river in rivers:
            rivers.append(station.river)
    return rivers

def stations_by_river(stations):
    rivers_stations_of_dict = {}
    for rivers in rivers_with_station(stations):
        rivers_stations_of_dict[rivers] = sorted([station.name for station in stations if station.river == rivers])
    return rivers_stations_of_dict

def stations_by_distance(stations, p):
    """This function calculates sorted distances between each 
    pair of multiple input stations.
    
    Input Param: list of tuples (station, distance),  
                tuple coordinate p
                
    Ouput Param: sorted list of distances
    
    """
    name_distance_list = []

    for station in stations:
        distance = haversine(station.coord, p)
        indi_tuple = (station.name, distance)
        name_distance_list.append(indi_tuple)

    distance_sort_list = sorted_by_key(name_distance_list, 1)

    return distance_sort_list

def stations_within_radius(stations, centre, r):
    """This function returns a list of stations within radius r
    of a geographic coordinate x
    
    Input Param: list of tuples (station, distance)
                 centre coordinate tuple
                 integer threshold r
    
    Ouput Param: list of tuples (station, distance) within radius
    
    """
    
    # Build a list of (station, distance)
    distance_sort_list = stations_by_distance(stations, centre)  # (station, distance)

    # Cut by threshold
    filtered_list = []
    for item in distance_sort_list:
        if item[1] <= r:
            filtered_list.append(item)

    return filtered_list

def rivers_with_station(stations):
    rivers = []
    for station in stations:
        if not station.river in rivers:
            rivers.append(station.river)
    return rivers





def rivers_by_station_number(stations, N):
    rivers = rivers_with_station(stations)
    river_counted = []
    if N == 0:
        return None
    else:
        for river in rivers:
            count = 0
            for station in stations:
                if station.river == river:
                    count += 1
            river_counted.append((river,count))
        river_counted = sorted_by_key(river_counted, 1, reverse=True)
        while river_counted[N-1][1] == river_counted[N][1]:
            N += 1
        return river_counted[:N]