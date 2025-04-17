from dataclasses import dataclass
from gettext import translation
from typing import Protocol

from app.constants.constants import TAG_DEFAULT_LOCALIZATION
from app.crud.config import crud_config

LOCALIZATION_OPTIONS: tuple[tuple[str, str], ...] = (
    (TAG_DEFAULT_LOCALIZATION, 'Русский'),
    ('eng', 'English'),
)
"""Кортеж с настройками локализации:

- названия файла и значения в бд,
- названия языка в меню настройки приложения.
"""


class LocalizationP(Protocol):
    """Протокол класса Localization."""

    title_window_main: str
    """Название главного окна."""
    title_window_config: str
    """Название окна конфигурации."""
    title_window_about: str
    """Название окна с информацией о проекте."""
    button_config: str
    """Кнопка главного окна. Открытие окна конфигурации."""
    button_copy: str
    """Кнопка главного окна. Копирование пароля в буфер обмена."""
    button_search: str
    """Кнопка главного окна. Поиск в БД."""
    button_create: str
    """Кнопка главного окна. Открытие окна создания записи в БД."""
    button_updata: str
    """Кнопка главного окна. Открытие окна изменения записи в БД."""
    button_all_note: str
    """Кнопка главного окна. Открытие окна со всеми записями в БД."""
    text_label_localization: str
    """Надпись в окне конфигурации. Настройка локализации приложения."""
    text_label_password: str
    """Надпись в окне конфигурации. Настройка генерации пароля в приложении."""
    label_min_length_password: str
    """Надпись возле спинбокса конфигурации. Минимальная длина генерируемого
    пароля.
    """
    label_max_length_password: str
    """Надпись возле спинбокса конфигурации. Максимальная длина генерируемого
    пароля.
    """
    checkbutton_capital_letters: str
    """Кнопка окна конфигурации. Использование заглавных букв в генерируемом
    пароле.
    """
    checkbutton_numbers: str
    """Кнопка окна конфигурации. Использование цифр в генерируемом пароле."""
    checkbutton_characters: str
    """Кнопка окна конфигурации. Использование спец символов в генерируемом
    пароле.
    """
    button_config_about: str
    """Кнопка окна конфигурации. Открытие окна с информацией о приложении."""
    button_config_apply: str
    """Кнопка окна конфигурации. Принятие изменений конфигурации."""
    button_config_cancel: str
    """Кнопка окна конфигурации. Закрытие окна конфигурации без изменений."""
    text_for_about_windows: str
    """Текст, который отображается в окне с информацией о проекте."""
    text_for_about_windows_link: str
    """Ссылка, которая отображается в окне с информацией о проекте."""
    text_for_about_windows_signature: str
    """Подпись, которая отображается в окне с информацией о проекте."""
    button_config_about_close: str
    """Кнопка окна c с информацией о проекте. Закрывает окно."""


def get_locales() -> type[LocalizationP]:
    """
    Из БД получит выбранную пользователем локализацию,
    найдет соответствующий файл с переводом,
    вернет dataclass с переведенными константами."""

    languages = str(crud_config.get_localization())

    try:
        locales = translation(
            'loc', localedir='locales', languages=[languages]
        )
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
        title_window_about: str = _('О проекте')
        button_config: str = _('Настройки')
        button_copy: str = _('Скопировать')
        button_search: str = _('Найти')
        button_create: str = _('Создать запись')
        button_updata: str = _('Изменить')
        button_all_note: str = _('Посмотреть всё')
        text_label_localization: str = _('Выберете язык приложения:')
        text_label_password: str = _('Конфигурация генератора пароля:')
        label_min_length_password: str = _('Минимальная длина пароля')
        label_max_length_password: str = _('Максимальная длина пароля')
        checkbutton_capital_letters: str = _(
            'Использовать заглавные латинские буквы'
        )
        checkbutton_numbers: str = _('Использовать цифры')
        checkbutton_characters: str = _('Использовать спецсимволы')
        button_config_about: str = _('О проекте')
        button_config_apply: str = _('Применить')
        button_config_cancel: str = _('Отменить')
        text_for_about_windows: str = _(
            'Sorcerers Book: небольшое приложение, для хранения паролей от '
            'всего и вся.\n'
            'Как записная книжка. Писал для себя любимого.\n'
            'Код открытый, можете посмотреть:'
        )
        text_for_about_windows_link: str = (
            'https://github.com/levisserena/Sorcerers_Book'
        )
        text_for_about_windows_signature: str = _('C уважением, Акчурин Лев.')
        button_config_about_close: str = _('Лев, ты большой молодец!')

    return Localization
