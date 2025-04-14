TRUE: int = 1
"""Для подмены bool значения True."""
FALSE: int = 0
"""Для подмены bool значения False."""

STATIC_DIR: str = 'static'
"""Название папки со статикой."""
ICONBITMAP: str = STATIC_DIR + '/sb.ico'
"""Относительный путь до иконки приложения."""

TAG_DEFAULT_LOCALIZATION: str = 'rus'
"""rus"""

FONT: str = 'Arial'
"""Название используемого шрифт."""
FONT_SIZE: int = 11
"""Размер шрифта."""
FONT_REGULAR: tuple[str, int] = FONT, FONT_SIZE
"""Обычный шрифт."""
FONT_UNDERLINED: tuple[str, int, str] = FONT, FONT_SIZE, 'underline'
"""Подчеркнутый шрифт."""

NUMBER: str = '1234567890'
"""Коллекция цифр для генерации пароля."""
CHARACTERS: str = '~!@#$%^&*_-+=,.'
"""Коллекция символов для генерации пароля."""
CHARACTERS_RAW: str = r'~!@#$%^&*_\-\+=,.'
"""Коллекция символов для генерации пароля в виде сырой строки."""
LOWERCASE_LETTERS: str = 'abcdefghijklmnopqrstuvwxyz'
"""Коллекция строчных букв для генерации пароля."""
CAPITAL_LETTERS: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
"""Коллекция заглавных букв для генерации пароля."""
