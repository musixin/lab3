import pytest
from lib import fib, bubble_sort, find_primes


def test_fibonacci():
    assert fib(5) == [0, 1, 1, 2, 3]
    assert fib(1) == [0]
    assert fib(2) == [0, 1]
    assert fib(0) == []
    assert fib(-3) == []
    with pytest.raises(TypeError):
        fib("2")



def test_bubble_sort():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert bubble_sort([]) == []
    assert bubble_sort([5]) == [5]
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]
    assert bubble_sort([3, 3, 1]) == [1, 3, 3]

    with pytest.raises(AttributeError):
        bubble_sort("2,3,4")

    with pytest.raises(TypeError):
        bubble_sort([2.2, "string", 3.1, "", 5.0])


def test_find_primes():
    assert find_primes(10) == [2, 3, 5, 7]
    assert find_primes(3) == [2]
    assert find_primes(2) == []
    assert find_primes(1) == []
    assert find_primes(0) == []
    assert find_primes(-10) == []
    with pytest.raises(TypeError):
        find_primes(6.5)
