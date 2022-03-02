import floodsystem.analysis 
    
station = build_station_list()
def test_call(station):
    a = floodsystem.analysis.relative_risk(station)

