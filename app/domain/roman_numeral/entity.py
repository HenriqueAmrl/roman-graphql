from typing import Optional


class RomanNumeral:
    NUMBER_VALUES: dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    number: Optional[str] = None
    value: Optional[int] = None

    def __init__(self, number: str) -> None:
        number = number.strip().upper()
        if not number:
            raise ValueError("Invalid Roman numeral.")
        for digit in number:
            if digit not in self.NUMBER_VALUES:
                raise ValueError("Invalid Roman numeral.")

        self.number = number
        self.__calculate_value()

    def __calculate_value(self) -> None:
        value: int = 0
        for number in self.get_separated_numbers():
            if len(number) == 1:
                value += self.NUMBER_VALUES[number]
            else:
                value += self.NUMBER_VALUES[number[-1]] - self.NUMBER_VALUES[number[-2]]
        self.value = value

    def get_separated_numbers(self) -> list[str]:
        """Retorna uma lista com os números romanos separados."""
        separated_numbers: list = []
        last: Optional[str] = None

        for digit in self.number:
            if last:
                if self.__less_than(last, digit):
                    separated_numbers[-1] += digit
                    last = None
                else:
                    separated_numbers.append(digit)
                    last = digit
            else:
                separated_numbers.append(digit)
                last = digit
        return separated_numbers

    def __less_than(self, first: str, second: str) -> bool:
        return self.NUMBER_VALUES[first] < self.NUMBER_VALUES[second]

    def __repr__(self) -> str:
        return self.number

    def __eq__(self, __o) -> bool:
        return self.number == __o.number
