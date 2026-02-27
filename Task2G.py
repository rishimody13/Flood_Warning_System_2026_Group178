# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

"""Flood risk assessment for towns (Task 2G).

Strategy:
- Use current relative water level where available.
- Estimate trend (rising/falling) from a short history fit.
- Aggregate station risk to the town level (take worst station per town).
"""

import datetime

from matplotlib.dates import date2num

from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


LOOKBACK_DAYS = 2
POLY_DEGREE = 4
TOP_N = 50
PRINT_TOP = 10

REL_SEVERE = 2.0
REL_HIGH = 1.5
REL_MODERATE = 1.0
REL_ELEVATED = 0.75

RISING = 0.02  # m/day
RISING_FAST = 0.05  # m/day


def trend_slope(station):
    dt = datetime.timedelta(days=LOOKBACK_DAYS)
    dates, levels = fetch_measure_levels(station.measure_id, dt)

    if len(dates) < POLY_DEGREE + 1:
        return None

    poly, d0 = polyfit(dates, levels, POLY_DEGREE)
    x = date2num(dates)
    slope = poly.deriv()(x[-1] - d0)
    return slope


def classify_risk(rel_level, slope):
    rising = slope is not None and slope > RISING
    rising_fast = slope is not None and slope > RISING_FAST

    if rel_level >= REL_SEVERE or (rel_level >= REL_HIGH and rising) or (
        rel_level >= REL_MODERATE and rising_fast
    ):
        return "severe"
    if rel_level >= REL_HIGH or (rel_level >= REL_MODERATE and rising) or (
        rel_level >= REL_ELEVATED and rising_fast
    ):
        return "high"
    if rel_level >= REL_MODERATE or (rel_level >= REL_ELEVATED and rising):
        return "moderate"
    return "low"


def run():
    stations = build_station_list()
    update_water_levels(stations)

    top = stations_highest_rel_level(stations, TOP_N)
    candidates = [
        s
        for s, _level in top
        if s.town
        and s.relative_water_level() is not None
        and s.relative_water_level() >= REL_ELEVATED
    ]

    town_risk = {}
    for station in candidates:
        rel_level = station.relative_water_level()
        slope = trend_slope(station)
        risk = classify_risk(rel_level, slope)

        rank = {"low": 0, "moderate": 1, "high": 2, "severe": 3}[risk]
        key = station.town
        entry = (rank, rel_level, slope, station)

        if key not in town_risk:
            town_risk[key] = entry
        else:
            cur = town_risk[key]
            if entry[:2] > cur[:2]:
                town_risk[key] = entry

    ranked = sorted(town_risk.items(), key=lambda kv: (kv[1][0], kv[1][1]), reverse=True)

    print("Criteria used:")
    print("- Current relative water level compared to typical range.")
    print(
        "- Short-term trend from a degree-{} polynomial over the last {} days."
        .format(POLY_DEGREE, LOOKBACK_DAYS)
    )
    print("- Trend estimated only for the top {} stations by relative level."
          .format(TOP_N))
    print(
        "- Trend thresholds: rising > {:.2f} m/day, rising fast > {:.2f} m/day."
        .format(RISING, RISING_FAST)
    )
    print()

    print("Towns with greatest assessed flood risk:")
    for town, (rank, rel_level, slope, station) in ranked[:PRINT_TOP]:
        if rank == 0:
            continue
        trend = "unknown"
        gradient = "unknown"
        if slope is not None:
            trend = "rising" if slope > 0 else "falling"
            gradient = "{:.3f} m/day".format(slope)
        risk = ["low", "moderate", "high", "severe"][rank]
        print(
            "- {}: {} (station: {}, relative level: {:.2f}, trend: {}, gradient: {})".format(
                town, risk, station.name, rel_level, trend, gradient
            )
        )


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
