import pytest 
import source.my_functions as my_functions
import time

def test_addition():
    result = my_functions.add(number_one=1, number_two=4)
    assert result == 5

def test_add_strings():
    result = my_functions.add("J'aime les ", "tests")
    assert result == "J'aime les tests"


def test_divide():
    result = my_functions.divide(number_one=10, number_two=2)
    assert result == 5

def test_divide_zero():
    with pytest.raises(ValueError):
        my_functions.divide(number_one=10, number_two=0)


def test_multiply_by_negative():
    result = my_functions.multiply(number_one=5, number_two=-2)
    assert result == -10

def test_multiply_by_positive():
    result = my_functions.multiply(number_one=5, number_two=2)
    assert result == 10

def test_multiply_by_zero():
    result = my_functions.multiply(number_one=5, number_two=0)
    assert result == 0

@pytest.mark.slow
def test_multiply_slow():
    time.sleep(5)
    result = my_functions.multiply(number_one=5, number_two=0)
    assert result == 0

@pytest.mark.skip(reason="broken")
def test_add():
    result= my_functions.add(1,4)
    assert result == 5

@pytest.mark.xfail(reason="bug wip")
def test_add_2():
    result= my_functions.add(1,4)
    assert result == 5