from twttr import shorten

# vowels are: "aeiou"


def test_lower_words_with_vowels():
    assert shorten("hello avocado") == "hll vcd"
    assert shorten("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"


def test_upper_words_with_vowels():
    assert shorten("HELLO AVOCADO") == "HLL VCD"
    assert shorten("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ"


def test_mixed_words_with_vowels():
    assert shorten("helLO AvOcaDo") == "hlL vcD"
    assert shorten("AbcdeFGHIJKlmnOPQrSTUvwxYZ") == "bcdFGHJKlmnPQrSTvwxYZ"


def test_words_without_vowels():
    assert shorten("hll vcd") == "hll vcd"
    assert shorten("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"
    assert shorten("bcdFGHJKlmnPQrSTvwxYZ") == "bcdFGHJKlmnPQrSTvwxYZ"


def test_with_numbers():
    assert shorten("hello world123") == "hll wrld123"
    assert shorten(
        "Ab1cd2eF3GH4IJ5Kl6mn7OP8Qr9STUvwxYZ") == "b1cd2F3GH4J5Kl6mn7P8Qr9STvwxYZ"


def test_with_punctuation():
    assert shorten("hello, avocado") == "hll, vcd"
    assert shorten("hello! world123") == "hll! wrld123"
