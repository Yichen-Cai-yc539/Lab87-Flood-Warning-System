from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
import pprint

def run2c(stations, N):

    risk_stations = stations_highest_rel_level(stations, N)
    name_rel = []
    for item in risk_stations:
        name_rel.append((item.name, item.relative_water_level()))

    return name_rel

if __name__ == "__main__":

    # Initialize
    stations = build_station_list()
    update_water_levels(stations)
    
    # Output
    pp = pprint.PrettyPrinter()
    pp.pprint(run2c(stations, 10))