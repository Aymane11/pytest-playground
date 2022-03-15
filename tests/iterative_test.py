from src.main import fibonacci_iterative


def test_fibonacci_iterative_0():
    assert fibonacci_iterative(0) == 0


def test_fibonaaci_iterative_1():
    assert fibonacci_iterative(1) == 1


def test_fibonaaci_iterative_2():
    assert fibonacci_iterative(2) == 1


def test_fibonaaci_iterative_3():
    assert fibonacci_iterative(3) == 2


def test_fibonaaci_iterative_4():
    assert fibonacci_iterative(4) == 3


def test_fibonaaci_iterative_5():
    assert fibonacci_iterative(5) == 5


def test_fibonaaci_iterative_6():
    assert fibonacci_iterative(6) == 8


def test_fibonaaci_iterative_7():
    assert fibonacci_iterative(7) == 13


def test_fibonaaci_iterative_8():
    assert fibonacci_iterative(8) == 21


def test_fibonaaci_iterative_9():
    assert fibonacci_iterative(9) == 34


def test_fibonaaci_iterative_10():
    assert fibonacci_iterative(10) == 55
