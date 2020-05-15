import csv
from contextlib import contextmanager


def parse_data(file_name):
    file = open(file_name)
    try:
        dialect = csv.Sniffer().sniff(file.read(2048))
        file.seek(0)
        next(file)
        yield from csv.reader(file, dialect=dialect)
    finally:
        file.close()


def coroutine(fn):
    def inner(*args, **kwargs):
        coro = fn(*args, **kwargs)
        # prime the coroutine
        next(coro)
        return coro
    return inner


@coroutine
def save_file(file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        while True:
            row = yield
            writer.writerow(row)


@coroutine
def filter_data(filter_pred, target):
    while True:
        row = yield
        if filter_pred(row):
            target.send(row)


@coroutine
def pipeline_coroutine(out_file, name_filters):
    save = save_file(out_file)

    target = save
    for name_filter in name_filters:
        target = filter_data(lambda d, v=name_filter: v in d[0], target)
    while True:
        received = yield
        target.send(received)


@contextmanager
def pipeline(out_file, name_filters):
    pipe = pipeline_coroutine(out_file, name_filters)
    try:
        yield pipe
    finally:
        pipe.close()

