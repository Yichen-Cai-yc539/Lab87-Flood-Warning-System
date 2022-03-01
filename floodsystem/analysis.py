import numpy as np
import matplotlib
from floodsystem.stationdata import *


def polyfit(dates, levels, p):
    p_coeff = np.polyfit(dates, levels, p)
    poly = np.ploy1d(p_coeff)

    return poly, dates[-1]

def relative_risk(station:
    ## This returns a numerical value depending on how vunerable a station is to flooding
    number = 0
    relative_level = MonitoringStation.relative_water_level(station)
    if relative_level == None:
        number = None
    else: 
        if relative_level