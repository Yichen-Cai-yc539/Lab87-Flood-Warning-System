from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list

def run2b(tol):
    """Demo for task 2b"""
    
    # Initialize
    stations = build_station_list()
    over_tol_list = stations_level_over_threshold(stations, tol)
    return over_tol_list

if __name__ == "__main__":
    run2b(0.8)
