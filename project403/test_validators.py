import pytest

from project403.inventory import validate


class TestIntegerValidator:
    def test_valid(self):
        validate('arg', 10, 0, 20, 'custom min msg', 'custom max msg')

    def test_type_error(self):
        with pytest.raises(TypeError):
            validate('arg', 1.5)

    def test_min_std_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate('arg', 10, 100)
        assert 'arg' in str(ex.value)
        assert '100' in str(ex.value)

    def test_min_custom_msg(self):
        with pytest.raises(ValueError) as ex:
            validate('arg', 10, 100, custom_min_message='custom')
        assert str(ex.value) == 'custom'

    def test_max_std_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate('arg', 10, 1, 5)
        assert 'arg' in str(ex.value)
        assert '5' in str(ex.value)

    def test_max_custom_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate('arg', 10, 1, 5, custom_max_message='custom')
        assert str(ex.value) == 'custom'
