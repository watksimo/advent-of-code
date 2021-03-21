from day_21 import *
import pytest

@pytest.fixture
def global_var():
    ptest_var = None

def test_1(global_var):
    assert 1 == 1
