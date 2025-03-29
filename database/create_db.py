from typing import Type

from database.constant import DefaultSetting
from database.manager import Connector


def create_db(name_db: str, setting: Type[DefaultSetting]) -> None:
    """
    Создаст файл базы данных если его нет,
    и создаст таблицы в нем, если их нет.
    """
    with Connector(name_db) as cursor:
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {setting.name_table_data} (
        id INTEGER PRIMARY KEY,
        slug TEXT NOT NULL,
        description TEXT,
        password TEXT NOT NULL
        )
        """)
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {setting.name_table_setting} (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        value INTEGER NOT NULL
        )
        """)


def default_settings(name_db: str, setting: Type[DefaultSetting]) -> None:
    """Заполнит таблицу Setting в базе данных, тем самым, установит первоначальные настройки."""
    all_default_settings = {
        setting.localization: setting.default_localization,
        setting.capital_letters: setting.true,
        setting.numbers: setting.true,
        setting.characters: setting.true,
        setting.min_length_password: setting.default_length_password,
        setting.max_length_password: setting.default_length_password,
    }

    with Connector(name_db) as cursor:
        for key, value in all_default_settings.items():
            if not cursor.execute(
                f'SELECT * FROM {setting.name_table_setting} WHERE name = ?',
                (key,),
            ).fetchall():
                cursor.execute(
                    f'INSERT INTO {setting.name_table_setting} (name, value) VALUES (?, ?)',
                    (key, value),
                )
