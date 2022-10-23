from kalkulator import *



def test_add():
    assert add(1, 2) == 3
    assert add(3, 1) == 4
    assert add(5,0) == 5


def test_sub():
    assert sub(1, 2) == -1
    assert sub(3, 1) == 2


def test_mul():
    assert mul(1, 2) == 2
    assert mul(2, 2) == 4


def test_div():
    assert div(2, 2) == 1
    assert div(4, 2) == 2
    assert  div(4,0) == "Nie dziel przez zero"

def test_kalkulator():
    assert kalkulator("10", 1, 1) == "Nieokreślona operacja"

