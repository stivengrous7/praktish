import pytest
from calculator import add, sub, mul, div


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 5) == -5


def test_mul():
    assert mul(4, 3) == 12
    assert mul(0, 100) == 0


def test_div():
    assert div(10, 2) == 5
    assert div(3, 2) == 1.5


def test_div_by_zero():
    with pytest.raises(ValueError):
        div(10, 0)