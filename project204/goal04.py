import itertools

from project204.goal03 import filtered_iter_combined


def group_data(data, key, group_key):
    data = filtered_iter_combined(data, key=key)
    sorted_data = sorted(data, key=group_key)
    groups = itertools.groupby(sorted_data, key=group_key)
    group_counts = ((g[0], len(list(g[1]))) for g in groups)
    return sorted(group_counts, key=lambda row: row[1], reverse=True)

