from typing import Type

from database.constant import DefaultSetting
from database.manager import Connector


def get_localization(name_db: str, setting: Type[DefaultSetting]):
    """Вернет значение локализация из базы данных."""
    with Connector(name_db) as cursor:
        return cursor.execute(
            f'SELECT value FROM {setting.name_table_setting} WHERE name = ?',
            (setting.localization,)
        ).fetchone()[0]
