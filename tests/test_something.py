class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def calculate_area(self):
        a = ((self.p1.x * (self.p2.y - self.p3.y)) +
             (self.p2.x * (self.p3.y - self.p1.y)) +
             (self.p3.x * (self.p1.y - self.p2.y))) / 2
        return abs(a)



def test_calculate_area():
    """Test the calculate_area function of the Triangle class"""

    # Equilateral triangle
    p11 = Point(0, 0)
    p12 = Point(2, 0)
    p13 = Point(1, 1.7320)
    t1 = Triangle(p11, p12, p13)
    assert t1.calculate_area() == 6

    # Right-angled triangle
    p21 = Point(0, 0)
    p22 = Point(3, 0)
    p23 = Point(0, 4)
    t2 = Triangle(p21, p22, p23)
    assert t2.calculate_area() == 6

    # Isosceles triangle
    p31 = Point(0, 0)
    p32 = Point(4, 0)
    p33 = Point(2, 8)
    t3 = Triangle(p31, p32, p33)
    assert t3.calculate_area() == 16

    # Scalene triangle
    p41 = Point(0, 0)
    p42 = Point(3, 0)
    p43 = Point(1, 4)
    t4 = Triangle(p41, p42, p43)
    assert t4.calculate_area() == 6

    # Negative values
    p51 = Point(0, 0)
    p52 = Point(-3, 0)
    p53 = Point(0, -4)
    t5 = Triangle(p51, p52, p53)
    assert t5.calculate_area() == 6






import pytest

@pytest.mark.parametrize(
    ("p1x, p1y, p2x, p2y, p3x, p3y, expected"),
    [
        pytest.param(0, 0, 2, 0, 1, 1.7320, 1.7320, id="Equilateral triangle"),
        pytest.param(0, 0, 3, 0, 0, 4, 6, id="Right-angled triangle"),
        pytest.param(0, 0, 4, 0, 2, 8, 16, id="Isosceles triangle"),
        pytest.param(0, 0, 3, 0, 1, 4, 6, id="Scalene triangle"),
        pytest.param(0, 0, -3, 0, 0, -4, 6, id="Negative values")
    ]
)
def test_calculate_area(p1x, p1y, p2x, p2y, p3x, p3y, expected):
    p1 = Point(p1x, p1y)
    p2 = Point(p2x, p2y)
    p3 = Point(p3x, p3y)
    t = Triangle(p1, p2, p3)
    assert t.calculate_area() == expected









def func(a, b):
    return a + b
