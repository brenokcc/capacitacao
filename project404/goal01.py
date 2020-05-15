import numbers


# Integer descriptor
class IntegerField:
    def __init__(self, _min, _max):
        self._min = _min
        self._max = _max

    def __set_name__(self, owner_class, attr_name):
        self.attr_name = attr_name

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('{} must be an integer'.format(self.attr_name))
        if self._min is not None and value < self._min:
            raise ValueError('{} must be >= {}.'.format(self.attr_name, self._min))
        if self._max is not None and value > self._max:
            raise ValueError('{} must be <= {}'.format(self.attr_name, self._max))
        instance.__dict__[self.attr_name] = value

    def __get__(self, instance, owner_class):
        return instance is None and self or instance.__dict__.get(self.attr_name, None)


# Char descriptor
class CharField:
    def __init__(self, _min=None, _max=None):
        self._min = max(_min or 0, 0)
        self._max = _max

    def __set_name__(self, owner_class, attr_name):
        self.attr_name = attr_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('{} must be a string'.format(self.attr_name))
        if self._min is not None and len(value) < self._min:
            raise ValueError('{} must be >= {} chars'.format(self.attr_name, self._min))
        if self._max is not None and len(value) > self._max:
            raise ValueError('{} must be <= {} chars'.format(self.attr_name, self._max))
        instance.__dict__[self.attr_name] = value

    def __get__(self, instance, owner_class):
        return instance is None and self or instance.__dict__.get(self.attr_name, None)
