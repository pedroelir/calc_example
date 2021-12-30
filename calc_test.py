import pytest

from myapp.tools.Calculator import calc


@pytest.fixture()
def Calculator():
    return calc.Calculator


def test_add(Calculator):
    mycalc = Calculator()
    result = mycalc.calc(mycalc.SUMA, 1, 2)
    assert result == 3


def test_sub(Calculator):
    mycalc = Calculator()
    result = mycalc.calc(mycalc.RESTA, 1, 2)
    assert result == -1


if __name__ == "__main__":
    pytest.main([__file__])
