from project204.goal02 import iter_combined


def filtered_iter_combined(data, *, key=None):
    iter_combo = iter_combined(data)
    yield from filter(key, iter_combo)

