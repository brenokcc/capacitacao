import csv
from collections import namedtuple
from contextlib import contextmanager


@contextmanager
def parsed_data(f_name):
    f = open(f_name, 'r')
    try:
        dialect = csv.Sniffer().sniff(f.read(1024))
        f.seek(0)
        reader = csv.reader(f, dialect)
        headers = map(lambda line: line.lower(), next(reader))
        nt = namedtuple('Data', headers)
        yield (nt(*line) for line in reader)
    finally:
        f.close()


