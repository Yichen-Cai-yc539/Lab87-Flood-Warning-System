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
