import pytest

def test_test_primes():
    ret = pytest.main(["test_primality.py", "-q"])
    assert ret == 1
