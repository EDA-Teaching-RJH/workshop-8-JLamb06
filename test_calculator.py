import pytest
import math
from Calculator import add, subtract, times, divide

def test_assert():
    assert times(1,3)
    assert divide(1,3)
    assert add(1,3)
    assert subtract(1,3)