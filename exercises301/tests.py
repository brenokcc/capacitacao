from exercises301.exercise01 import sort_dict_by_value
from exercises301.exercise02 import intersect
from exercises301.exercise03 import merge
from exercises301.exercise04 import identify


def test_sort_dict_by_value():
    composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}
    sorted_composers = {'Wolfgang': 35, 'Frederic': 39, 'Ludwig': 56, 'Johann': 65}
    result = sort_dict_by_value(composers)
    assert result == sorted_composers


def test_intersect():
    d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}
    result = intersect(d1, d2)
    assert result == {'b': (2, 20), 'c': (3, 30)}


def test_merge():
    d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
    d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
    d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}
    result = merge(d1, d2, d3)
    assert result == {
        'python': 17, 'javascript': 15, 'java': 13, 'c#': 12, 'c++': 10, 'go': 9, 'erlang': 5, 'haskell': 2, 'pascal': 1
    }


def test_identify():
    n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
    n2 = {'employees': 250, 'users': 23, 'user': 230}
    n3 = {'employees': 150, 'users': 4, 'login': 1000}
    result = identify(n1, n2, n3)
    assert result == { 'login': (0, 0, 1000), 'user': (100, 230, 0), 'employee': (5000, 0, 0)}


test_sort_dict_by_value()
test_intersect()
test_merge()
test_identify()
