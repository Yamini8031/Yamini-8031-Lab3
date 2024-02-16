import triangle


def test_integration():
    # Test area of the triangle by first calculating the perimeter and then using the value to calculate the area
    assert triangle.area(5, 6, 7) == 21
