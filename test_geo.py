# Yichen Cai

"""Unit test for geo module"""

from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():
    """Test function stations_by_distance"""

    # Initialize
    stations = build_station_list()
    print(stations[0])
    centre = (52.2053, 0.1218)
    output_list = stations_by_distance(stations, centre)

    # Check list is not None
    assert len(output_list) > 0

    # Check list is sorted
    distance_list = []
    for item in output_list:
        distance = item[1]
        distance_list.append(distance)
    sorted_list = sorted(distance_list)
    assert distance_list == sorted_list


def test_stations_within_radius():
    """Test function stations_within_radius"""
    
    # Initialize
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10
    within_r = stations_within_radius(stations, centre, r)
    
    # Check list is not None, radius < r
    assert len(within_r) > 0
    for item in within_r:
        assert item[1] <= r

