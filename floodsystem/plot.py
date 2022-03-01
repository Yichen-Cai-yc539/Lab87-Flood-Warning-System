import numpy as np


def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    plt.xlabel('Date')
    plt.ylabel('Water level')
    plt.title("Station: " + station.name)
    plt.tight_layout()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p, show_typical_range =  True):
    ## Plots water levels for a station with ployfit
