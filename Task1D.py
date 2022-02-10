from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    stations = build_station_list()

    rivers = rivers_with_station(stations)
    print("\n {} stations. First 10 - {}".format(len(rivers), rivers[:10]))

    rivers_station_of_dict = stations_by_river(stations)
    print("\n Stations next to the River Aire: {}".format(rivers_station_of_dict['River Aire']))
    print("\n Stations next to the River Cam: {}".format(rivers_station_of_dict['River Cam']))
    print("\n Stations next to the River Thames: {}".format(rivers_station_of_dict['River Thames']))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part 1A Floor Warning System ***")
    run()
