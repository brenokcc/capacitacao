import itertools
from collections import namedtuple

from project204.goal01 import iter_file, field_names


def named_tuple_class(data):
    compress_fields = itertools.chain.from_iterable(t[3] for t in data)
    fields = itertools.chain.from_iterable(field_names(t[1]) for t in data)
    compressed_field_names = itertools.compress(fields, compress_fields)
    return namedtuple('Data', compressed_field_names)


def iter_combined(data):
    combo_nt = named_tuple_class(data)
    compress_fields = tuple(itertools.chain.from_iterable(t[3] for t in data))
    zipped_tuples = zip(*(iter_file(fname, class_name, parser) for class_name, fname, parser, _ in data))

    merged_iter = (itertools.chain.from_iterable(zipped_tuple) for zipped_tuple in zipped_tuples)
    for row in merged_iter:
        compressed_row = itertools.compress(row, compress_fields)
        yield combo_nt(*compressed_row)



