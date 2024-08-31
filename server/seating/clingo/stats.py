# -*- coding: utf-8 -*-
"""

"""
import importlib


def make_stats(table_count, hanchan_count):
    player_count = table_count * 4
    try:
        seats_module = importlib.import_module(
            f"seats_{player_count}x{hanchan_count}")
    except:
        print(f"INFO no file for {player_count}x{hanchan_count}")
        return

    seats = getattr(seats_module, 'seats')
    p_p = [[0 for _ in range(player_count + 1)] for _ in range(player_count + 1)]
    p_t = [[0 for _ in range(table_count)] for _ in range(player_count + 1)]
    p_wind = [[0 for _ in range(4)] for _ in range(player_count + 1)]

    for h in range(hanchan_count):
        for t in range(table_count):
            for s1 in range(0, 4):
                p1 = seats[h][t][s1]
                p_t[p1][t] += 1
                p_wind[p1][s1] += 1
                for s2 in range(s1, 4):
                    p2 = seats[h][t][s2]
                    p_p[p1][p2] += 1
                    p_p[p2][p1] += 1

    w_hist = [0] * (hanchan_count + 1)
    t_hist = [0] * (hanchan_count + 1)
    meet_hist = [0] * (hanchan_count + 1)

    for p1 in range(1, player_count + 1):
        for s in range(4):
            w_hist[p_wind[p1][s]] += 1
        for t in range(table_count):
            t_hist[p_t[p1][t]] += 1
        for p2 in range(p1 + 1, player_count):
            meet_hist[p_p[p1][p2]] += 1

    wind_min = hanchan_count // 4
    wind_max = (hanchan_count + 3) // 4
    table_max = (hanchan_count + table_count * 2 - 1) // table_count
    meetup_max = 2

    warnings = []
    for n in range(wind_min):
        if False and w_hist[n] > 0:
            warnings.append(f"Low wind count: {w_hist[n]} occurrence(s) of {n} "
                            " wind allocation(s) for player-wind combinations")
            warnings.append(p_wind)

    for n in range(wind_max + 1, hanchan_count + 1):
        if False and w_hist[n] > 0:
            warnings.append(
                f"High wind count: {w_hist[n]} occurrence(s) of {n} "
                "wind allocations for player-wind combinations")

    for n in range(table_max + 1, hanchan_count + 1):
        if t_hist[n] > 0:
            warnings.append(
                f"High table count: {t_hist[n]} occurrence(s) of {n} "
                "visit(s) to a table by an individual player")

    for n in range(meetup_max + 1, hanchan_count + 1):
        if meet_hist[n] > 0:
            warnings.append(
                f"Repeat player meetups: {meet_hist[n]} occurrence(s) of {n} "
                "meetups of the same two players")

    if len(warnings) > 0:
        print(f"WARNINGS for {table_count} tables, {hanchan_count} hanchan:\n{'\n'.join(warnings)}")
    else:
        print(f"INFO no warnings for {table_count} tables, {hanchan_count} hanchan")
