import pytest

from ..entity import RomanNumeral


def test_conversion_to_int(valid_numbers: dict):
    for number, value in valid_numbers.items():
        rn = RomanNumeral(number)
        assert rn.value == value


def test_fails_when_starts_with_invalid_value():
    with pytest.raises(ValueError):
        RomanNumeral("RXVIII")


def test_fails_when_contains_invalid_value():
    with pytest.raises(ValueError):
        RomanNumeral("XXBBVII")


def test_fails_when_finishes_with_invalid_value():
    with pytest.raises(ValueError):
        RomanNumeral("VITY")
