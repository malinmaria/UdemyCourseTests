import pytest

@pytest
def SetUp():
    print("Once before every method")

def test_methodA(setUp):
    print("Running method A")

def test_methodB(setUp):
    print("Running method B")