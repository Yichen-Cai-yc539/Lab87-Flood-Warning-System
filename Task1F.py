# Yichen Cai

from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run1f():
    """Runs Task1F demo"""
    
    # Initialize
    stations = build_station_list()
    inconsistent_list = inconsistent_typical_range_stations(stations)
    
    # Build and sort list of names
    name_list = []
    for item in inconsistent_list:
        name = item[0]
        name_list.append(name)
    name_list = sorted(name_list)

    print(name_list)
    
if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run1f()