from project301.goal01 import match_keys, match_types, recurse_validate


def test_match_keys():
    t = {'a': int, 'b': int, 'c': int, 'd': int}
    d = {'a': 'wrong type', 'b': 100, 'c': 200, 'd': {'wrong': 'type'}}
    is_valid, msg = match_keys(d, t, 'some.path')
    assert (is_valid, msg) == (True, None)


def test_missing_keys():
    t = {'a': int, 'b': int, 'c': int, 'd': int}
    d = {'a': 'test', 'b': 'test', 'c': 'test'}
    is_valid, msg = match_keys(d, t, 'some.path')
    assert (is_valid, msg.strip()) == (False, 'missing keys: some.path.d')


def test_extra_keys():
    t = {'a': int, 'b': int, 'c': int, 'd': int}
    d = {'a': 'test', 'b': 'test', 'c': 'test', 'd': 'test', 'z': 'extra'}
    is_valid, msg = match_keys(d, t, 'some.path')
    assert (is_valid, msg.strip()) == (False, 'extra keys: some.path.z')


def test_match_types():
    t = {'a': int, 'b': str, 'c': {'d': int}}
    d = {'a': 100, 'b': 'test', 'c': {'some': 'dict'}}
    is_valid, msg = match_types(d, t, 'some.path')
    assert (is_valid, msg) == (True, None)


def test_incorrect_type():
    t = {'a': int, 'b': str, 'c': {'d': int}}
    d = {'a': 100, 'b': 'test', 'c': 'unexpected'}
    match_types(d, t, 'some.path')


def test_recursive_valiation():
    template = {
        'user_id': int,
        'name': {
            'first': str,
            'last': str
        },
        'bio': {
            'dob': {
                'year': int,
                'month': int,
                'day': int
            },
            'birthplace': {
                'country': str,
                'city': str
            }
        }
    }
    john = {
        'user_id': 100,
        'name': {
            'first': 'John',
            'last': 'Cleese'
        },
        'bio': {
            'dob': {
                'year': 1939,
                'month': 11,
                'day': 27
            },
            'birthplace': {
                'country': 'United Kingdom',
                'city': 'Weston-super-Mare'
            }
        }
    }
    is_valid, msg = recurse_validate(john, template, 'root')
    assert (is_valid, msg) == (True, None)
    eric = {
        'user_id': 101,
        'name': {
            'first': 'Eric',
            'last': 'Idle'
        },
        'bio': {
            'dob': {
                'year': 1943,
                'month': 3,
                'day': 29
            },
            'birthplace': {
                'country': 'United Kingdom'
            }
        }
    }
    is_valid, msg = recurse_validate(eric, template, 'root')
    assert (is_valid, msg.strip()) == (False, 'missing keys: root.bio.birthplace.city')
    michael = {
        'user_id': 102,
        'name': {
            'first': 'Michael',
            'last': 'Palin'
        },
        'bio': {
            'dob': {
                'year': 1943,
                'month': 'May',
                'day': 5
            },
            'birthplace': {
                'country': 'United Kingdom',
                'city': 'Sheffield'
            }
        }
    }
    is_valid, msg = recurse_validate(michael, template, 'root')
    assert (is_valid, msg.strip()) == (False, 'incorrect type: root.bio.dob.month -> expected int, found str')


test_match_keys()
test_extra_keys()
test_missing_keys()
test_match_types()
test_incorrect_type()
test_recursive_valiation()
