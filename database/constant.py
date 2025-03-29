from dataclasses import dataclass

LOCALIZATION_OPTIONS: dict = {
    1: 'ru',
    2: 'eng',
}


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
    localization: поле с локализацией проекта.
    capital_letters: поле "заглавные буквы в пароле".
    numbers: поле "цифры в пароле".
    characters: поле "символы в пароле".
    min_length_password: поле "минимальная длина пароля".
    max_length_password: поле "максимальная длина пароля".

    Значения:
    default_length_password: длина пароля по умолчанию.
    true: заменит True в таблице.
    false: заменит False в таблице.
    """

    name_db: str = 'grimoire.db'

    name_table_data: str = 'Scroll'
    name_table_setting: str = 'Setting'

    localization: str = 'localization'
    capital_letters: str = 'capital'
    numbers: str = 'numbers'
    characters: str = 'characters'
    min_length_password: str = 'min'
    max_length_password: str = 'max'

    default_localization: str = LOCALIZATION_OPTIONS[1]
    default_length_password: int = 16
    true: int = 1
    false: int = 0
