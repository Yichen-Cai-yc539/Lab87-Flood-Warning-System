# Yichen Cai

from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run1f():
    """Runs Task1F demo"""
    
    # Initialize
    stations = build_station_list()
    inconsistent_list = inconsistent_typical_range_stations(stations)
    print(inconsistent_list)


    name_list = []
    for station in stations:
        if station.typical_range_consistent() == False:
            name_list.append(station.name)
    name_list = sorted(name_list)

    print(name_list)
    
if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run1f()