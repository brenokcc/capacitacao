from project203.goal2 import violation_counts_by_make


def test_violation_counts_by_make():
    sorted_data = violation_counts_by_make()
    print(sorted_data)
    keys = list(sorted_data.keys())
    first = keys[0]
    last = keys[-1]
    assert first == 'TOYOT' and sorted_data['TOYOT'] == 112
    assert last == 'MI/F' and sorted_data['MI/F'] == 1


test_violation_counts_by_make()
