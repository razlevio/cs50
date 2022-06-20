from numb3rs import validate

def test_format():
    assert validate("") == False
    assert validate("1.1.1") == False
    assert validate("1.1") == False
    assert validate("1") == False
    assert validate("1/1/1/1") == False
    assert validate("1$1$1") == False
    assert validate("1.1.1.1") == True

def test_greater_numbers():
    assert validate("256.1.1.1") == False
    assert validate("275.300.500.355") == False
    assert validate("275") == False
    assert validate("1.300.1.1") == False
    assert validate("1.1.500.1") == False
    assert validate("1.1.1.355") == False
    assert validate("255.2.55.16") == True

def test_lower_numbers():
    assert validate("-256.1.1.1") == False
    assert validate("-275.-300.-500.-355") == False
    assert validate("-275") == False
    assert validate("-1.-300.1.1") == False
    assert validate("1.1.-500.1") == False
    assert validate("1.-1.1.355") == False
