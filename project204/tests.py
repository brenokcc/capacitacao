import itertools
from datetime import datetime
from functools import partial

from project204.goal01 import iter_file, parse_date
from project204.goal02 import iter_combined
from project204.goal03 import filtered_iter_combined
from project204.goal04 import group_data


def test_iter_file():
    data = [
        ('Personal', 'personal_info.csv', (str, str, str, str, str)),
        ('Employment', 'employment.csv', (str, str, str, str)),
        ('Vehicle', 'vehicles.csv', (str, str, str, int)),
        ('UpdateStatus', 'update_status.csv', (str, parse_date, parse_date))
    ]

    for class_name, fname, parser in data:
        file_iter = iter_file(fname, class_name, parser)
        # exibindo dois registros por tipo
        print(next(file_iter))
        print(next(file_iter))
        print()


def test_iter_combined():
    data = [
        ('Personal', 'personal_info.csv', (str, str, str, str, str), (True, True, True, True, True)),
        ('Employment', 'employment.csv', (str, str, str, str), (True, True, True, False)),
        ('Vehicle', 'vehicles.csv', (str, str, str, int), (False, True, True, True)),
        ('UpdateStatus', 'update_status.csv', (str, parse_date, parse_date), (False, True, True))
    ]

    data_iter = iter_combined(data)

    for row in itertools.islice(data_iter, 5):
        print(row)


def test_filter_iter_combined():
    data = [
        ('Personal', 'personal_info.csv', (str, str, str, str, str), (True, True, True, True, True)),
        ('Employment', 'employment.csv', (str, str, str, str), (True, True, True, False)),
        ('Vehicle', 'vehicles.csv', (str, str, str, int), (False, True, True, True)),
        ('UpdateStatus', 'update_status.csv', (str, parse_date, parse_date), (False, True, True))
    ]

    data_iter = iter_combined(data)

    for row in itertools.islice(data_iter, 5):
        print(row)

    print('-----------------')

    cutoff_date = datetime(2018, 3, 1)
    filtered_iter = filtered_iter_combined(data, key=lambda row: row.last_updated >= cutoff_date)
    for row in filtered_iter:
        print(row)


def test_group_data():
    cutoff_date = datetime(2017, 3, 1)
    data = [
        ('Personal', 'personal_info.csv', (str, str, str, str, str), (True, True, True, True, True)),
        ('Employment', 'employment.csv', (str, str, str, str), (True, True, True, False)),
        ('Vehicle', 'vehicles.csv', (str, str, str, int), (False, True, True, True)),
        ('UpdateStatus', 'update_status.csv', (str, parse_date, parse_date), (False, True, True))
    ]

    def filter_key(date, gender, obj):
        return obj.last_updated >= date and obj.gender == gender

    female_data = group_data(
        data,
        key=partial(filter_key, cutoff_date, 'Female'),
        group_key=lambda obj: obj.vehicle_make)

    print('FEMALE')
    for row in female_data:
        print(row)
    print()

    male_data = group_data(
        data,
        key=lambda obj: filter_key(cutoff_date, 'Male', obj),
        group_key=lambda obj: obj.vehicle_make
    )

    print('MALE')
    for row in male_data:
        print(row)


test_iter_file()
test_iter_combined()
test_filter_iter_combined()
test_group_data()
