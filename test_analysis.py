from xml.dom.expatbuilder import parseString
from floodsystem.analysis import relative_risk, polyfit
from floodsystem.stationdata import build_station_list



def test_call():
    station = build_station_list()
    a = relative_risk(station)
    pass

