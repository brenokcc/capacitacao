from collections import defaultdict

from project203.goal1 import parse_data


def violation_counts_by_make():
    makes_counts = defaultdict(int)
    for data in parse_data():
        makes_counts[data.vehicle_make] += 1
    sorted_makes_counts = sorted(makes_counts.items(), key=lambda t: t[1], reverse=True)
    return {make: c for make, c in sorted_makes_counts}

