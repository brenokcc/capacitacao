from project402.goal01 import Mod

m1 = Mod(4, 3)  # 1
m2 = Mod(8, 3)  # 2


def test_mod():
    assert m1.value == 1
    assert m2.value == 2


def test_add():
    m = m1 + m2
    assert m.value == 0


def test_sub():
    m = m1 - m2
    assert m.value == 2


test_mod()
test_add()
test_sub()
