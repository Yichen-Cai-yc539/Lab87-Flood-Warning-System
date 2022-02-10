# Yichen Cai

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run1b():
    """Run the Task2B program"""
    
    # Initialize
    stations = build_station_list()  # stations: [(name, ...), (), ...]
    centre = (52.2053, 0.1218)
    distance_sort_list = stations_by_distance(stations, centre)

    # Build dictionary that maps station to town
    name_town_dict = {}
    for station in stations:
        name_town_dict[station.name] = station.town
    
    # Build list of tuples (name, town, distance)
    item_list = []
    for item in distance_sort_list:  # item: (station.name, d)
        key = item[0]
        new_item = (key, name_town_dict[key], item[1])
        item_list.append(new_item)
    
    # Print first and last ten items in list
    closest = item_list[:10]
    farthest = item_list[-10:]
    print(closest)
    print(farthest)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run1b()