from .entity import RomanNumeral


def get_from_string(string: str) -> list[RomanNumeral]:
    """Limpa a string recebida (removendo caracteres que não são números romanos)
    e retorna somente os caracteres romanos.

    Args:
        string (str)

    Returns:
        list[RomanNumeral]
    """
    try:
        string = string.strip().upper()
    except AttributeError:
        raise ValueError('Invalid text') from AttributeError

    separated_numbers: list = []
    number: str = ""

    for digit in string:
        if digit in RomanNumeral.NUMBER_VALUES:
            number += digit
        elif number:
            separated_numbers.append(RomanNumeral(number))
            number = ""

    separated_numbers.append(RomanNumeral(number))
    return separated_numbers


def get_highest_value_from_string(string: str) -> RomanNumeral:
    """Identifica os números romanos presentes na string e retorna o de maior valor

    Args:
        string (str)

    Returns:
        RomanNumeral
    """
    numbers: list[RomanNumeral] = get_from_string(string)
    return sorted(numbers, key=lambda rn: rn.value)[-1]
