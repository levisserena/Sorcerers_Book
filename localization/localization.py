from typing import Protocol, Type

from dataclasses import dataclass
from gettext import translation

from database.crud import crud_setting


class LocalizationP(Protocol):
    """Протокол класса Localization."""

    title: str
    title_window_setting: str
    button_setting: str
    button_copy: str
    button_search: str
    button_create: str
    button_updata: str
    button_all_note: str
    text_label_localization: str
    text_label_password: str


def get_locales() -> type[LocalizationP]:

    languages = crud_setting.get_localization()

    locales = translation('loc', localedir='locales', languages=[languages])
    locales.install()
    _ = locales.gettext

    @dataclass
    class Localization:
        """Локализация приложения."""

        title: str = _('Книжка колдуна')
        title_window_setting: str = _('Настройки')
        button_setting: str = _('Настройки')
        button_copy: str = _('Скопировать')
        button_search: str = _('Найти')
        button_create: str = _('Создать запись')
        button_updata: str = _('Изменить')
        button_all_note: str = _('Посмотреть всё')
        text_label_localization: str = _('Выберете язык приложения:')
        text_label_password: str = _('Настройки генератора пароля:')

    return Localization
