from dataclasses import dataclass
from typing import Any

from app.constants.constants import TAG_DEFAULT_LOCALIZATION, TRUE


@dataclass
class Config:
    """
    Названия конфигураций в приложении.

    localization_app: локализация проекта.
    capital_letters: "заглавные буквы в пароле".
    numbers: "цифры в пароле".
    characters: "символы в пароле".
    min_length_password: "минимальная длина пароля".
    max_length_password: "максимальная длина пароля".
    """

    localization_app: str = 'localization_app'
    capital_letters: str = 'capital_letters'
    numbers: str = 'numbers'
    characters: str = 'characters'
    min_length_password: str = 'min_length_password'
    max_length_password: str = 'max_length_password'


@dataclass
class DefaultConfig:
    """
    Набор конфигураций по умолчанию.

    Значения, для настроек:
    default_localization: локализация проекта по умолчанию.
    default_length_password: длина пароля по умолчанию.
    """

    default_localization: str = TAG_DEFAULT_LOCALIZATION
    default_length_password: int = 16

    @classmethod
    def get_default_config(cls) -> dict[str, Any]:
        """
        Подготовит словарь с первоначальными настройками
        для первого заполнения таблицы Настройки в БД.
        """
        return {
            Config.localization_app: cls.default_localization,
            Config.capital_letters: TRUE,
            Config.numbers: TRUE,
            Config.characters: TRUE,
            Config.min_length_password: cls.default_length_password,
            Config.max_length_password: cls.default_length_password,
        }
