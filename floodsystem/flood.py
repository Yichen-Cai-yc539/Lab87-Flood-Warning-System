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
