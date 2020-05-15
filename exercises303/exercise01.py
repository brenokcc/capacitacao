from collections import Counter
from collections import defaultdict


def merge_with_dict(*dicts):
    unsorted = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            unsorted[k] += v
    return dict(sorted(unsorted.items(), key=lambda e: e[1], reverse=True))


def merge_with_counter(*dicts):
    result = Counter()
    for d in dicts:
        result.update(d)
    return dict(result.most_common())
