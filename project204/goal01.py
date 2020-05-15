import csv
from collections import namedtuple
from datetime import datetime


def csv_parser(file_name, include_header=False):
    with open(file_name) as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        if not include_header:
            next(f)
        # delegando iteração
        yield from reader


def parse_date(value, *, fmt='%Y-%m-%dT%H:%M:%SZ'):
    return datetime.strptime(value, fmt)


def field_names(file_name):
    reader = csv_parser(file_name, include_header=True)
    return next(reader)


def named_tuple_class(file_name, class_name):
    fields = field_names(file_name)
    return namedtuple(class_name, fields)


def iter_file(file_name, class_name, parser):
    nt_class = named_tuple_class(file_name, class_name)
    reader = csv_parser(file_name)
    for row in reader:
        parsed_data = (parse_fn(value)for value, parse_fn in zip(row, parser))
        yield nt_class(*parsed_data)
