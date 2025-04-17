from random import choice, randint
from re import match

from app.constants.constants import (
    CAPITAL_LETTERS,
    CHARACTERS,
    CHARACTERS_RAW,
    LOWERCASE_LETTERS,
    NUMBER,
)


def generate_password(
    min_range_pass: int,
    max_range_pass: int,
    number: int,
    capital_letters: int,
    characters: int,
) -> str:
    """Генератор паролей.

    Параметры:
    - min_range_pass:
    - max_range_pass:
    - number:
    - capital_letters:
    - capital_letters:

    Возвращает сгенерированный пароль в виде строки.
    """
    character_set = (
        LOWERCASE_LETTERS +
        NUMBER * number +
        CAPITAL_LETTERS * capital_letters +
        CHARACTERS * characters
    )

    def get_pattern():
        r"""
        Вернет паттерн, для проверки присутствия хотя бы одного символа из
        набора.

        Пример:
        `^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$`
        """
        part_pattern_1 = r'(?=.*[a-z])'
        part_pattern_2 = r'a-z'
        if capital_letters:
            part_pattern_1 += r'(?=.*[A-Z])'
            part_pattern_2 += r'A-Z'
        if number:
            part_pattern_1 += r'(?=.*\d)'
            part_pattern_2 += r'\d'
        if characters:
            part_pattern_1 += fr'(?=.*[{CHARACTERS_RAW}])'
            part_pattern_2 += CHARACTERS_RAW
        return fr'^{part_pattern_1}[{part_pattern_2}]{{{min_range_pass},}}$'

    pattern_password = get_pattern()

    if max_range_pass < min_range_pass:
        min_range_pass, max_range_pass = max_range_pass, min_range_pass
    range_pass = randint(min_range_pass, max_range_pass)
    for _ in range(1000):
        pass_list = [choice(character_set) for _ in range(range_pass)]
        password = ''.join(pass_list)
        if match(pattern_password, password) is not None:
            return password
    return password
