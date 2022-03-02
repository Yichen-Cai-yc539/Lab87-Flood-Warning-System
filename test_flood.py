from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold


class MockStation():
    """Madeup station data for testing"""

    def __init__(self, name, typical_range, latest_level):

        self.name = name
        self.typical_range = typical_range
        self.latest_level = latest_level
    
    def relative_water_level(self):
        """Returns latest water level as a fraction of typical range"""

        low = min(self.typical_range)
        high = max(self.typical_range)
        typ_range = high - low
        fraction = (self.latest_level - low) / typ_range
        return fraction
        

def test_stations_level_over_threshold():
    
    # Initialize
    station1 = MockStation("a", (0, 1), 0.5)
    station2 = MockStation("b", (0, 1), 0.9)
    station3 = MockStation("c", (0, 1), 1)

    stations = [station1, station2, station3]

    over_tol_list = stations_level_over_threshold(stations, 0.8)
    
    assert over_tol_list is not None
    assert len(over_tol_list) == 2


def test_stations_highest_rel_level():

    # Initialize
    station1 = MockStation("a", (0, 1), 0.5)
    station2 = MockStation("b", (0, 1), 0.9)
    station3 = MockStation("c", (0, 1), 1)

    stations = [station1, station2, station3]

    most_risk = stations_highest_rel_level(stations, 2)
    assert len(most_risk) == 2
    n = 0
    for item in most_risk:
        assert item.name == "{}".format(stations[2-n].name)
        n += 1