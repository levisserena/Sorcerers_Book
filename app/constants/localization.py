from dataclasses import dataclass
from gettext import  translation
from typing import Protocol

from app.constants.constants import TAG_DEFAULT_LOCALIZATION
from app.crud.config import crud_config

LOCALIZATION_OPTIONS: tuple[tuple[str, str], ...] = (
    (TAG_DEFAULT_LOCALIZATION, 'Русский'),
    ('eng', 'English'),
    ('d', 'sdfa')
)
"""
Кортеж с настройками локализации:

    - названия файла и значения в бд,
    - названия языка в меню настройки приложения.
"""


class LocalizationP(Protocol):
    """Протокол класса Localization."""

    title_window_main: str
    title_window_config: str
    button_config: str
    button_copy: str
    button_search: str
    button_create: str
    button_updata: str
    button_all_note: str
    text_label_localization: str
    text_label_password: str


def get_locales() -> type[LocalizationP]:

    languages = crud_config.get_localization()

    try:
        locales = translation('loc', localedir='locales', languages=[languages])
        locales.install()
        _ = locales.gettext
    except FileNotFoundError:
        def _(text):
            """Будет возвращать не переведенный текст."""
            return text

    @dataclass
    class Localization:
        """Локализация приложения."""

        title_window_main: str = _('Книжка колдуна')
        title_window_config: str = _('Настройки')
        button_config: str = _('Настройки')
        button_copy: str = _('Скопировать')
        button_search: str = _('Найти')
        button_create: str = _('Создать запись')
        button_updata: str = _('Изменить')
        button_all_note: str = _('Посмотреть всё')
        text_label_localization: str = _('Выберете язык приложения:')
        text_label_password: str = _('Конфигурация генератора пароля:')

    return Localization
