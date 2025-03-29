from typing import Protocol, Type

from dataclasses import dataclass
from gettext import translation

from database.localization import get_localization
from database.constant import DefaultSetting


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


def get_locales(name_db: str, setting: Type[DefaultSetting]) -> type[LocalizationP]:

    loc = get_localization(name_db, setting)

    locales = translation('loc', localedir='locales', languages=[loc])
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

    return Localization
