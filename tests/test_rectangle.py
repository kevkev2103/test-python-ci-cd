import source.shapes as shapes
import pytest

def area_check(rectangle_factory):
    my_rectangle = rectangle_factory(10,20)
    assert my_rectangle.area() == 10 * 20

def test_perimeter(rectangle_factory):
    my_rectangle = rectangle_factory(10,20)
    assert my_rectangle.perimeter() == 10*2 + 20*2

def test_equality(rectangle_factory):
    my_rectangle = rectangle_factory(10,20)
    another_same_rectangle = rectangle_factory(10,20)
    assert my_rectangle == another_same_rectangle

@pytest.fixture
def rectangle_factory():
    def create_rectangle(width, length):
        return shapes.Rectangle(width=width, length=length)
    return create_rectangle

def test_inequality(rectangle_factory):
    my_rectangle = rectangle_factory(10,20)
    another_different_rectangle = rectangle_factory(15,25)
    assert my_rectangle != another_different_rectangle