import pytest 
import source.shapes as shapes

@pytest.fixture
def my_circle():
    return shapes.Circle(10)

# @pytest.fixture
# def my_rectangle():
#     return shapes.Rectangle(10,20)

# @pytest.fixture 
# def another_same_rectangle():
#     return shapes.Rectangle(10,20)

# @pytest.fixture
# def another_different_rectangle():
#     return shapes.Rectangle(15,30)

@pytest.fixture 
def rectangle_factory():
    def create_rectangle(width, length):
        return shapes.Rectangle(width=width, length=length)
    return create_rectangle