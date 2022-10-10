import pytest

from src.fibo import fibonacci_iterative


def test_fibonacci_iterative_0():
    assert fibonacci_iterative(0) == 0


def test_fibonaaci_iterative_1():
    assert fibonacci_iterative(1) == 1


def test_fibonaaci_iterative_2():
    assert fibonacci_iterative(2) == 1


def test_fibonaaci_iterative_3():
    assert fibonacci_iterative(3) == 2


def test_fibonaaci_iterative_negative():
    with pytest.raises(Exception) as e:
        fibonacci_iterative(-1)  # Should raise an exception

    assert str(e.value) == "n must be non-negative"
    assert e.type == ValueError
