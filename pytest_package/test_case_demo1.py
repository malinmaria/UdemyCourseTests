import pytest

@pytest.fixture()
def setUp():
    print("Once before every method")
    yield
    print("Once after every method")

def test_methodA(setUp):
    print("Running method A")

def test_case1_methodA(self):
    print("Running class 1 -> method A")

def test_methodB(setUp):
    print("Running method B")
