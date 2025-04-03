from dataclasses import dataclass
from typing import Any

LOCALIZATION_OPTIONS: dict[int, tuple[str, str]] = {
    1: ('ru', 'Русский'),
    2: ('eng', 'English'),
}
"""
Словарь с настройками локализации.

- Ключи - цифры по порядку начиная с 0. Важно!
- Значения - кортеж состоящий из:
    - названия файла и значения в бд
    - названия языка в меню настройки приложения.
"""


@dataclass
class DefaultSetting:
    """
    Набор настроек по умолчанию,
    которые будут хранится в виде таблицы.

    Названия:
    name_db: имя файла БД.
    name_table_data: название таблицы с полезной нагрузкой.
    name_table_setting: название таблицы с настройками.

    Поля:
    slug: поле слаг, по которому будет поиск.
    description: описание.
    password: пароль, который хотим сохранить.
    name: название настройки.
    value: значение настройки.

    Названия, для настроек:
    localization: локализация проекта.
    capital_letters: "заглавные буквы в пароле".
    numbers: "цифры в пароле".
    characters: "символы в пароле".
    min_length_password: "минимальная длина пароля".
    max_length_password: "максимальная длина пароля".

    Значения, для настроек:
    default_length_password: длина пароля по умолчанию.
    true: заменит True в таблице.
    false: заменит False в таблице.
    """

    name_db: str = 'grimoire.db'

    name_table_data: str = 'Scroll'
    name_table_setting: str = 'Setting'

    slug: str = 'slug'
    description: str = 'description'
    password: str = 'password'
    name: str = 'name'
    value: str = 'value'

    localization: str = 'localization'
    capital_letters: str = 'capital'
    numbers: str = 'numbers'
    characters: str = 'characters'
    min_length_password: str = 'min'
    max_length_password: str = 'max'

    default_localization: str = LOCALIZATION_OPTIONS[1][0]
    default_length_password: int = 16
    true: int = 1
    false: int = 0

    @property
    def default_settings(self) -> dict[str, Any]:
        """
        Подготовит словарь с первоначальными настройками
        для первого заполнения таблицы Настройки в БД.
        """
        return {
            self.localization: self.default_localization,
            self.capital_letters: self.true,
            self.numbers: self.true,
            self.characters: self.true,
            self.min_length_password: self.default_length_password,
            self.max_length_password: self.default_length_password,
        }
