from .. import RomanNumeral, get_from_string, get_highest_value_from_string


def test_get_from_string(random_text_with_roman_numerals):
    text, numbers = random_text_with_roman_numerals
    items = get_from_string(text)
    assert [item.number for item in items] == numbers


def test_get_highest_value_from_string(random_text_with_roman_numerals):
    text, numbers = random_text_with_roman_numerals
    item = get_highest_value_from_string(text)
    assert (
        item
        == sorted(
            [RomanNumeral(number) for number in numbers], key=lambda rn: rn.value
        )[-1]
    )
