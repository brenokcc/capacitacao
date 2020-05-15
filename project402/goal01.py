import operator
from functools import total_ordering


@total_ordering
class Mod:
    def __init__(self, value, modulus):
        if not isinstance(modulus, int):
            raise TypeError('Unsupported type for modulus')
        if not isinstance(value, int):
            raise TypeError('Unsupported type for value')
        if modulus <= 0:
            raise ValueError('Modulus must be positive')

        self._modulus = modulus
        self._value = value % modulus

    @property
    def modulus(self):
        return self._modulus

    @property
    def value(self):
        return self._value

    def __repr__(self):
        return 'Mod({}, {})'.format(
            self._value, self._modulus
        )

    def __int__(self):
        return self.value

    def _get_value(self, other):
        if isinstance(other, int):
            return other % self.modulus
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return other.value
        raise TypeError('Incompatible types')

    def _perform_operation(self, other, op, *, in_place=False):
        other_value = self._get_value(other)
        new_value = op(self.value, other_value)
        if in_place:
            self._value = new_value % self.modulus
            return self
        else:
            return Mod(new_value, self.modulus)

    def __eq__(self, other):
        other_value = self._get_value(other)
        return other_value == self.value

    def __hash__(self):
        return hash((self.value, self.modulus))

    def __neg__(self):
        return Mod(-self.value, self.modulus)

    def __add__(self, other):
        return self._perform_operation(other, operator.add)

    def __iadd__(self, other):
        return self._perform_operation(other, operator.add, in_place=True)

    def __sub__(self, other):
        return self._perform_operation(other, operator.sub)

    def __isub__(self, other):
        return self._perform_operation(other, operator.sub, in_place=True)

    def __mul__(self, other):
        return self._perform_operation(other, operator.mul)

    def __imul__(self, other):
        return self._perform_operation(other, operator.mul, in_place=True)

    def __pow__(self, other):
        return self._perform_operation(other, operator.pow)

    def __ipow__(self, other):
        return self._perform_operation(other, operator.pow, in_place=True)

    def __lt__(self, other):
        try:
            other_value = self._get_value(other)
            return self.value < other_value
        except TypeError:
            return NotImplemented
