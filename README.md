# pytest playground

## Installation
- Python 3.7+ :snake:
- poetry :pen: _[(installation guide)](https://github.com/python-poetry/poetry#installation)_

## Usage
- Run the following command to install dependencies:

    poetry install

- Get coverage : `coverage run -m pytest && coverage report -m && coverage xml`
- Fixtures are shown in the `conftest.py` and `test_fixture.py` files.
- Mocking is shown in the `test_mock.py` file.
- Exception handling is shown in the `test_exception.py` file.