from fuel import convert, gauge
import pytest


def test_convert_value_error():
    with pytest.raises(ValueError):
        assert convert("three/four")  # checking division by words
        assert convert("1.5/3")      # checking wrong type
        assert convert("1/3.5")      # checking wrong type
        assert convert("1.5/3.5")    # checking wrong type


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert convert("0/0")  # checking division by zero
        assert convert("4/0")  # checking division by zero


def test_convert():
    assert convert("1/2") == 50
    assert convert("2/2") == 100
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(10) == "10%"
    assert gauge(17) == "17%"
