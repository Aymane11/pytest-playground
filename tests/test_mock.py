from unittest.mock import patch

from src.transformations import make_transformation


@patch("src.transformations.load_random_data")
def test_make_transformation(mocker):
    """
    Since we're checking the behavior of the `make_transformation` method
    we don't need to rely on the behavior of the `load_random_data` method.
    That's why we're mocking it, by fixing it's return value to `1`.
    """
    mocker.return_value = 1
    actual = make_transformation()
    expected = 3
    assert actual == expected
