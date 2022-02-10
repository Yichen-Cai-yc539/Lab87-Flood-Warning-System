# Yichen Cai

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run1c():
    """Runs Task1C"""

    # Initialize
    centre = (52.2053, 0.1218)
    r = 10
    stations = build_station_list()

    # Call stations_within_radius function
    name_distance_list = stations_within_radius(stations, centre, r)

    # Extract name and sort alphabetically
    name_list = []
    for item in name_distance_list:
        name_list.append(item[0])
    name_list = sorted(name_list)
    print(name_list)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run1c()