from project405.goal01 import AppException


def test_app_exceptions():
    exceptions = [(ex.name, ex.code, ex.message) for ex in AppException]
    assert exceptions == [
        ('Generic', 100, 'Application exception'),
        ('Timeout', 101, 'Timeout connecting to resource'),
        ('NotAnInteger', 200, 'Value must be an integer'),
        ('NotAList', 201, 'Value must be a list')
    ]


test_app_exceptions()
