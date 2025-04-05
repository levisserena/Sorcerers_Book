from app.constants.database import ConstantDataBase
from app.crud.base import CRUDBase
from app.crud.manager import Connector


class CRUDPayload(CRUDBase):
    """Управление таблицей с полезной нагрузкой в БД."""

    def __init__(
        self,
        name_db: str,
        name_table: str,
        connector: type[Connector],
        field_slug: str,
        field_description: str,
        field_password: str,
    ) -> None:
        """
        Параметры:
            name_db: название Базы данных;
            name_table: название таблицы в БД;
            connector: менеджер подключения к БД.
            field_slug: поле slug у таблицы, заменит короткое название.
            field_description: поле description у таблицы, для подробного описания.
            field_password: поле password у таблицы, для хранения пароля.
        """
        super().__init__(name_db, name_table, connector)
        self.field_slug = field_slug
        self.field_description = field_description
        self.field_password = field_password

    def create_db(self):
        """Создаст таблицу в БД для хранения настроек приложения."""
        with self.connector(self.name_db) as cursor:
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.name_table} (
            id INTEGER PRIMARY KEY,
            {self.field_slug} TEXT NOT NULL,
            {self.field_description} TEXT,
            {self.field_password} TEXT NOT NULL
            )
            """)


crud_payload = CRUDPayload(
    name_db=ConstantDataBase.name_db,
    name_table=ConstantDataBase.name_table_payload,
    connector=Connector,
    field_slug=ConstantDataBase.slug,
    field_description=ConstantDataBase.description,
    field_password=ConstantDataBase.password,
)
