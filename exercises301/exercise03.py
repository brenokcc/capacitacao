
def merge(*dicts):
    unsorted = dict()
    for d in dicts:
        for k, v in d.items():
            unsorted[k] = unsorted.get(k, 0) + v
    return dict(
        sorted(unsorted.items(), key=lambda e: e[1], reverse=True)
    )
