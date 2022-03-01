import numpy as np
import matplotlib
from floodsystem.stationdata import *


def polyfit(dates, levels, p):

    p_coeff = np.polyfit(dates, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, dates[-1]


def relative_risk(station):
    ## Returns a numerical value for the relative risk from flooding for a particular station
    
    number = 0
    relative_level = MonitoringStation.relative_water_level(station)
    if relative_level == None:
        number = None
    else:
        if relative_level > 0.5:
            number += 1
        if relative_level > 1:
            number += 1
        if relative_level > 1.5:
            number+= 1
        if relative_level > 2:
            number +=1

    return number