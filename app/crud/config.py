from typing import Any

from app.constants.database import ConstantDataBase
from app.crud.base import CRUDBase
from app.crud.manager import Connector
from app.constants.config import Config


class CRUDConfig(CRUDBase):
    """Управление таблицей с настройками приложения в БД."""

    def __init__(
        self,
        name_db: str,
        name_table: str,
        connector: type[Connector],
        field_name: str,
        field_value: str,
        name_config: type[Config],
    ) -> None:
        """
        Параметры:
            name_db: название Базы данных;
            name_table: название таблицы в БД;
            connector: менеджер подключения к БД.
            field_name: поле name у таблицы.
            field_value: поле value у таблицы.
            name_config: класс с названием всех конфигураций.
        """
        super().__init__(name_db, name_table, connector)
        self.field_name = field_name
        self.field_value = field_value
        self.name_config = name_config

    def create_db(self) -> None:
        """Создаст таблицу в БД для хранения настроек приложения."""
        with self.connector(self.name_db) as cursor:
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.name_table} (
            id INTEGER PRIMARY KEY,
            {self.field_name} TEXT NOT NULL,
            {self.field_value} INTEGER NOT NULL
            )
            """)

    def create_rows_in_db(self, data: dict[str, Any]) -> None:
        """Создаст записи в таблице с БД если их там нет."""
        with self.connector(self.name_db) as cursor:
            for key, value in data.items():
                if not cursor.execute(
                    f"""
                    SELECT *
                    FROM {self.name_table}
                    WHERE {self.field_name} = ?
                    """,
                    (key,),
                ).fetchall():
                    cursor.execute(
                        f"""
                        INSERT INTO {self.name_table}
                        ({self.field_name}, {self.field_value})
                        VALUES (?, ?)
                        """,
                        (key, value),
                    )

    def get_localization(self) -> str:
        """Вернет значение локализация из базы данных."""
        with self.connector(self.name_db) as cursor:
            return cursor.execute(
                f"""
                SELECT {self.field_value}
                FROM {self.name_table}
                WHERE {self.field_name} = ?
                """,
                (self.name_config.localization_app,)
            ).fetchone()[0]

    def get_all_settings(self) -> dict[str, Any]:
        """Вернет все значения настроек из БД."""
        with self.connector(self.name_db) as cursor:
            cursor.execute(
                f"""
                SELECT {self.field_name}, {self.field_value}
                FROM {self.name_table}
                """,
            )
            setting_db = cursor.fetchall()
        result = {name: value for name, value in setting_db}
        return result

    def update_all(self, data: dict[str, Any]) -> None:
        with self.connector(self.name_db) as cursor:
            for name, value in data.items():
                cursor.execute(
                    f"""
                    UPDATE {self.name_table}
                    SET {self.field_value} = ?
                    WHERE {self.field_name} = ?
                    """,
                    (value, name),
                )


crud_config = CRUDConfig(
    name_db=ConstantDataBase.name_db,
    name_table=ConstantDataBase.name_table_config,
    connector=Connector,
    field_name=ConstantDataBase.name,
    field_value=ConstantDataBase.value,
    name_config=Config,
)
