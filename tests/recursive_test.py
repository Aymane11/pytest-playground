from src.main import fibonacci_recursive


def test_fibonacci_recursive_0():
    assert fibonacci_recursive(0) == 0


def test_fibonaaci_iterative_1():
    assert fibonacci_recursive(1) == 1


def test_fibonaaci_iterative_2():
    assert fibonacci_recursive(2) == 1


def test_fibonaaci_iterative_3():
    assert fibonacci_recursive(3) == 2


def test_fibonaaci_iterative_4():
    assert fibonacci_recursive(4) == 3


def test_fibonaaci_iterative_5():
    assert fibonacci_recursive(5) == 5


def test_fibonaaci_iterative_6():
    assert fibonacci_recursive(6) == 8


def test_fibonaaci_iterative_7():
    assert fibonacci_recursive(7) == 13


def test_fibonaaci_iterative_8():
    assert fibonacci_recursive(8) == 21


def test_fibonaaci_iterative_9():
    assert fibonacci_recursive(9) == 34


def test_fibonaaci_iterative_10():
    assert fibonacci_recursive(10) == 55
