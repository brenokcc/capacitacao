from collections import Counter
from random import seed, choices

from exercises303.exercise01 import merge_with_dict, merge_with_counter
from exercises303.exercise02 import Person, count_eye_colors
from exercises303.exercise03 import load_settings, chain_recursively

d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}

d123 = {
    'python': 17, 'javascript': 15, 'java': 13, 'c#': 12, 'c++': 10, 'go': 9, 'erlang': 5, 'haskell': 2, 'pascal': 1
}
d12 = {'python': 16, 'javascript': 15, 'java': 13, 'c#': 12, 'c++': 10, 'go': 9}


def test_merge_with_dict():
    result = merge_with_dict(d1, d2, d3)
    assert result == d123

    result = merge_with_dict(d1, d2)
    assert result == d12


def test_merge_with_counter():
    result = merge_with_counter(d1, d2, d3)
    assert result == d123

    result = merge_with_dict(d1, d2)
    assert result == d12


def test_count_eye_colors():
    eye_colors = ("amber", "blue", "brown", "gray", "green", "hazel", "red", "violet")
    seed(0)
    people = [Person(color) for color in choices(eye_colors[2:], k=50)]
    result = count_eye_colors(people, eye_colors)
    assert result == Counter(
        {'amber': 0, 'blue': 0, 'brown': 3, 'gray': 10, 'green': 8, 'hazel': 7, 'red': 10, 'violet': 12}
    )


def test_load_settings():
    s1 = load_settings('common')
    s2 = load_settings('dev')
    dev = chain_recursively(s2, s1)

    assert dev['logs']['level'] == 'trace'

    s3 = load_settings('prod')
    prod = chain_recursively(s3, s1)
    assert prod['logs']['level'] == 'info'
    assert prod['database']['port'] == 5432
    assert prod['database']['user'] == '$PG_USER'


test_merge_with_dict()
test_merge_with_counter()
test_count_eye_colors()
test_load_settings()
