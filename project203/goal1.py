from collections import namedtuple
from datetime import datetime
from functools import partial


with open('nyc_parking_tickets_extract.csv') as f:
    headers = next(f).strip('\n').split(',')

Ticket = namedtuple('Ticket', [header.replace(' ', '_').lower() for header in headers])


def read_data():
    with open('nyc_parking_tickets_extract.csv') as file:
        next(file)
        yield from file


def parse_int(value, *, default=None):
    try:
        return int(value)
    except ValueError:
        return default


def parse_date(value, *, default=None):
    try:
        return datetime.strptime(value, '%m/%d/%Y').date()
    except ValueError:
        return default


def parse_string(value, *, default=None):
    cleaned = str(value).strip()
    if not cleaned:
        return default
    else:
        return cleaned


parsers = (
    parse_int,
    parse_string,
    partial(parse_string, default=''),
    partial(parse_string, default=''),
    parse_date,
    parse_int,
    partial(parse_string, default=''),
    parse_string,
    lambda x: parse_string(x, default='')
)


def parse_row(row, *, default=None):
    fields = row.strip('\n').split(',')
    data = [func(field) for func, field in zip(parsers, fields)]
    if all(item is not None for item in data):
        return Ticket(*data)
    else:
        return default


def parse_data():
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed
