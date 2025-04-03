from typing import Any

from database.constant import DefaultSetting
from database.crud.base import CRUDBase


class CRUDSetting(CRUDBase):
    """Управление таблицей с настройками приложения в БД."""

    def create_db(self):
        """Создаст таблицу в БД для хранения настроек приложения."""
        with self.connector(self.name_db) as cursor:
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.name_table} (
            id INTEGER PRIMARY KEY,
            {self.setting.name} TEXT NOT NULL,
            {self.setting.value} INTEGER NOT NULL
            )
            """)

    def create_rows_in_db(self, data: dict[str, Any]):
        """Создаст записи в таблице с БД если их там нет."""
        with self.connector(self.name_db) as cursor:
            for key, value in data.items():
                if not cursor.execute(
                    f'SELECT * FROM {self.name_table} WHERE name = ?',
                    (key,),
                ).fetchall():
                    cursor.execute(
                        f'INSERT INTO {self.name_table} (name, value) VALUES (?, ?)',
                        (key, value),
                    )

    def get_localization(self) -> str:
        """Вернет значение локализация из базы данных."""
        with self.connector(self.name_db) as cursor:
            return cursor.execute(
                f'SELECT value FROM {self.name_table} WHERE name = ?',
                (self.setting.localization,)
            ).fetchone()[0]

    def get_all_settings(self) -> dict[str, Any]:
        """Вернет все значения настроек из БД."""
        with self.connector(self.name_db) as cursor:
            cursor.execute(f'SELECT * FROM {self.name_table}')
            setting_db = cursor.fetchall()
        result = {key: value for _, key, value in setting_db}
        # TODO: валидацию result из базы, мало ли.
        return result


crud_setting = CRUDSetting(
    DefaultSetting.name_db,
    DefaultSetting.name_table_setting,
)
