from seasons import date_validation, generate_words
import pytest

def test_valid_birthday():
    assert date_validation("1996-05-30") == "1996-05-30"
    assert date_validation("2021-02-20") == "2021-02-20"


def test_invalid_birthday():
    with pytest.raises(SystemExit):
        assert date_validation("20222-02-30")
    with pytest.raises(SystemExit):
        assert date_validation("1999-13-25")
    with pytest.raises(SystemExit):
        assert date_validation("1999-11-33")


def test_valid_output():
    """ this answers only correct for 2022-07-08 """
    assert generate_words(13730400) == "Thirteen million, seven hundred thirty thousand, four hundred minutes"
