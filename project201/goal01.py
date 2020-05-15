import math


class Polygon:
    def __init__(self, n, r):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._r = r

    def __repr__(self):
        return 'Polygon(n={}, r={})'.format(self._n, self._r)

    @property
    def count_vertices(self):
        return self._n

    @property
    def count_edges(self):
        return self._n

    @property
    def circumradius(self):
        return self._r

    @property
    def interior_angle(self):
        return (self._n - 2) * 180 / self._n

    @property
    def side_length(self):
        return 2 * self._r * math.sin(math.pi / self._n)

    @property
    def apothem(self):
        return self._r * math.cos(math.pi / self._n)

    @property
    def area(self):
        return self._n / 2 * self.side_length * self.apothem

    @property
    def perimeter(self):
        return self._n * self.side_length

    def __eq__(self, other):
        if isinstance(other, Polygon):
            if self.count_edges == other.count_edges:
                if self.circumradius == other.circumradius:
                    return True
            return False
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented
