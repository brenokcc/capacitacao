import math
from project201.goal01 import Polygon
from project201.goal02 import Polygons


def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001

    # forçando exceção
    try:
        Polygon(2, 10)
        assert False, 'Creating a Polygon with 2 sides: Exception expected, not received'
    except ValueError:
        pass

    n = 3
    r = 1
    p = Polygon(n, r)
    assert str(p) == 'Polygon(n=3, r=1)', 'actual: {}'.format(p)
    assert p.count_vertices == n
    assert p.count_edges == n
    assert p.circumradius == r
    assert p.interior_angle == 60
    n = 4
    r = 1
    p = Polygon(n, r)
    assert p.interior_angle == 90
    assert math.isclose(p.area, 2, rel_tol=abs_tol, abs_tol=abs_tol)

    assert math.isclose(p.side_length, math.sqrt(2), rel_tol=rel_tol, abs_tol=abs_tol)

    assert math.isclose(p.perimeter, 4 * math.sqrt(2), rel_tol=rel_tol, abs_tol=abs_tol)

    assert math.isclose(p.apothem, 0.707, rel_tol=rel_tol, abs_tol=abs_tol)
    p = Polygon(6, 2)
    assert math.isclose(p.side_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)

    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5


def test_polygons():
    polygons = Polygons(10, 1)
    print([(p, p.area/p.perimeter) for p in polygons])
    assert polygons.max_efficiency_polygon == Polygon(n=10, r=1)
    polygons = Polygons(500, 1)
    assert int(polygons[-1].area * 100) == 314


test_polygon()
test_polygons()
