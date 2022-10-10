from src.transformations import fix_name


def test_fix_name(dummy_data):
    # Dummy data is automatically grabbed from conftest.py
    actual = fix_name(dummy_data)
    assert actual == "John Doe"
