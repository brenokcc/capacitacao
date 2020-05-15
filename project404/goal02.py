import numbers


# Base descriptor
class BaseDescriptor:
    def __init__(self, _min=None, _max=None):
        self._min = _min
        self._max = _max

    def __set_name__(self, owner_class, attr_name):
        self.attr_name = attr_name

    def validate(self, value):
        pass

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.attr_name] = value

    def __get__(self, instance, owner_class):
        return instance is None and self or instance.__dict__.get(self.attr_name, None)


# Integer descriptor
class IntegerField(BaseDescriptor):
    def validate(self, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('{} must be an integer'.format(self.attr_name))
        if self._min is not None and value < self._min:
            raise ValueError('{} must be >= {}.'.format(self.attr_name, self._min))
        if self._max is not None and value > self._max:
            raise ValueError('{} must be <= {}'.format(self.attr_name, self._max))


# Char descriptor
class CharField(BaseDescriptor):
    def __init__(self, min_, max_):
        min_ = max(min_ or 0, 0)
        super().__init__(min_, max_)

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError('{} must be a string'.format(self.attr_name))
        if self._min is not None and len(value) < self._min:
            raise ValueError('{} must be >= {} chars'.format(self.attr_name, self._min))
        if self._max is not None and len(value) > self._max:
            raise ValueError('{} must be <= {} chars'.format(self.attr_name, self._max))
