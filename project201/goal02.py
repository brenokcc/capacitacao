from project201.goal01 import Polygon


class Polygons:
    def __init__(self, m, r):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._r = r
        self._polygons = [Polygon(i, r) for i in range(3, m + 1)]

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return 'Polygons(m={}, r={})'.format(self._m, self._r)

    def __getitem__(self, s):
        return self._polygons[s]

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(
            self._polygons,
            key=lambda p: p.area / p.perimeter,
            reverse=True
        )
        return sorted_polygons[0]
