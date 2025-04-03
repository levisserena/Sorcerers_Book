from database.constant import DefaultSetting
from database.crud.base import CRUDBase


class CRUDPayload(CRUDBase):
    """Управление таблицей с полезной нагрузкой в БД."""

    def create_db(self):
        """Создаст таблицу в БД для хранения настроек приложения."""
        with self.connector(self.name_db) as cursor:
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.name_table} (
            id INTEGER PRIMARY KEY,
            {self.setting.slug} TEXT NOT NULL,
            {self.setting.description} TEXT,
            {self.setting.password} TEXT NOT NULL
            )
            """)


crud_payload = CRUDPayload(
    DefaultSetting.name_db,
    DefaultSetting.name_table_data,
)
