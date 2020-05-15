from project202.goal01 import Polygon


class PolygonsIterator:
    def __init__(self, m, r):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._r = r
        self._i = 3

    # iterator protocol
    def __iter__(self):
        return self

    # iterator protocol
    def __next__(self):
        if self._i > self._m:
            raise StopIteration
        else:
            result = Polygon(self._i, self._r)
            self._i += 1
            return result


class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._max_efficiency_polygon = None

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return 'Polygons(m={}, R={})'.format(self._m, self._R)

    # iterable protocol
    def __iter__(self):
        return PolygonsIterator(self._m, self._R)

    @property
    def max_efficiency_polygon(self):
        if self._max_efficiency_polygon is None:
            sorted_polygons = sorted(
                PolygonsIterator(self._m, self._R),
                key=lambda p: p.area/p.perimeter,
                reverse=True)
            self._max_efficiency_polygon = sorted_polygons[0]
        return self._max_efficiency_polygon
