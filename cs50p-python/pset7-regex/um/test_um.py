import pytest
from um import count

def test_number_of_ums():
    assert count("um") == 1
    assert count("um um um") == 3


def test_with_symbols():
    assert count("um,") == 1
    assert count("um! um, um@ um!") == 4


def test_with_uppercase():
    assert count("UM uM") == 2
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2

def test_with_no_um():
    assert count("hello world") == 0

def test_with_um_in_words():
    assert count("yummey") == 0
    assert count("album um") == 1
