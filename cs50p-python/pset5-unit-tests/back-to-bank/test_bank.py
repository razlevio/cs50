
from bank import value


def test_hello_input():
    assert value("hello my friend") == 0
    assert value("HELLO dear customer") == 0


def test_h_input():
    assert value("hey my friend") == 20
    assert value("HOWDEY dear customer") == 20


def test_no_h_nor_hello():
    assert value("welcome my friend") == 100
    assert value("BONJOUR dear customer") == 100
