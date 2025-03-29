from typing import Type

from database.constant import DefaultSetting
from database.create_db import create_db, default_settings
from localization.localization import get_locales
from windows.app import start


def main(name_db: str, setting: Type[DefaultSetting]) -> None:
    """Функция, запускающая всё приложение."""
    create_db(name_db, setting)
    default_settings(name_db, setting)
    start(get_locales(name_db, setting))


if __name__ == '__main__':
    main(DefaultSetting.name_db, DefaultSetting)
