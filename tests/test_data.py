from pyproduct.data import Square, Vector3


def test_area():
    square = Square(Vector3(1, 1, 1), 3)
    assert square.area() == 9

