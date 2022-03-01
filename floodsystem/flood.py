from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples (station, rel water level)
    for stations with latest water level over tol
    """
    
    over_tol_list = []
    for station in stations:
        if station.relative_water_level() is None:
            pass
        elif station.relative_water_level() > tol:
            item = (station.name, station.relative_water_level())
            over_tol_list.append(item)
    over_tol_list = sorted_by_key(over_tol_list, 1, reverse=True)

    return over_tol_list

def stations_highest_rel_level(stations, N):
    """Takes a list of """
    
    # Generate a list of tuples of station name and level
    over_tol_list = stations_level_over_threshold(stations, -1000)
    
    # Generate a list of station name
    name = []
    for item in over_tol_list:
        name.append(item[0])
    
    # Generate a list of MonitoringStation objects
    most_risk = []
    for item in name:
        for station in stations:
            if item == station.name:
                most_risk.append(station)

    return most_risk[:N]