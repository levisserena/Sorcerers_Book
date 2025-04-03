from database.constant import DefaultSetting
from database.create_db import create_all_db, default_settings
from windows.app import start


def main(name_db: str, setting: type[DefaultSetting]) -> None:
    """Функция, запускающая всё приложение."""
    create_all_db()
    default_settings(setting)
    start()


if __name__ == '__main__':
    main(DefaultSetting.name_db, DefaultSetting)
