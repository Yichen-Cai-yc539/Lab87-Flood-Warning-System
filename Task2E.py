from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.analysis import update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run2e(station, dates, levels):
    plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    
    # Initialization
    stations = build_station_list()
    update_water_levels(stations)

    for station in stations:
        if station.name == "Letcombe Bassett":
            print(station.name, station.latest_level, station.typical_range,
            station.relative_water_level())
    
    # Top 5 stations with greatest water level
    risk_stations = stations_highest_rel_level(stations, 5)
    
    # Plot past 5 days of levels
    dt = 10
    for station in risk_stations:
        dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=datetime.timedelta(days=dt))
        print(levels)
        run2e(station, dates, levels)


