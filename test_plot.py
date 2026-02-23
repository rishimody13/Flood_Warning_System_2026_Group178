import pytest
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.station import MonitoringStation
import datetime
def test_plot_water_levels():
    #unit test for plot_water_levels
    station = MonitoringStation("s1", "m1", "Station 1", (0.0, 1.0), (0.0, 1.0), "River 1", "Town 1")
    # station = MonitoringStation( "test_id", "test_measure_id", "Test Station", (0.0, 1.0), 0.5, 0.5)
    dates = [datetime.datetime(2026, 1, i) for i in range(1, 6)]
    levels = [0.5, 0.6, 0.4, 0.7, 0.3]
    plot_water_levels(station, dates, levels)
    #manual check: should display a plot with the correct title, labels, and data points
def test_plot_water_level_with_fit():
    #unit test for plot_water_level_with_fit
    station = MonitoringStation("s1", "m1", "Station 1", (0.0, 1.0), (0.0, 1.0), "River 1", "Town 1")
    dates = [datetime.datetime(2026, 1, i) for i in range(1, 6)]
    levels = [0.5, 0.6, 0.4, 0.7, 0.3]
    plot_water_level_with_fit(station, dates, levels, p=3)
    #manual check: should display a plot with the correct title, labels, data points, and a degree-3 polynomial fit

test_plot_water_levels()
test_plot_water_level_with_fit()