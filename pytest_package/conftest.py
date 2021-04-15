import pytest

@pytest.fixture()
def setUp():
    print("Running conftest demo1 setup")
    yield
    print("Running conftest demo1 tearDown")