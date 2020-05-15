from project205.goal01 import FileParser
from project205.goal02 import parsed_data
import itertools


def test_context_manager_class():
    print('--- PERSONAL INFO ---')
    with FileParser('personal_info.csv') as data:
        for row in itertools.islice(data, 2):
            print(row)

    print('--- CARS ---')
    with FileParser('cars.csv') as data:
        for row in itertools.islice(data, 2):
            print(row)


def test_context_manager_function():
    print('--- PERSONAL INFO ---')
    with parsed_data('personal_info.csv') as data:
        for row in itertools.islice(data, 2):
            print(row)

    print('--- CARS ---')
    with parsed_data('cars.csv') as data:
        for row in itertools.islice(data, 2):
            print(row)


test_context_manager_class()
test_context_manager_function()
