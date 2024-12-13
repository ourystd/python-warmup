import pytest
from calculator import square, cube


def test_square():
    assert square(3) == 9


def test_square_str():
    with pytest.raises(TypeError):
        square("3")


def test_cube():
    assert cube(3) == 27
