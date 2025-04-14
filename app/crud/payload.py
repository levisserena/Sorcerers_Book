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

    def create_db(self) -> None:
        """Создаст таблицу в БД для хранения настроек приложения."""
        with self.connector(self.name_db) as cursor:
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.name_table} (
            id INTEGER PRIMARY KEY,
            {self.field_slug} TEXT NOT NULL UNIQUE,
            {self.field_description} TEXT,
            {self.field_password} TEXT NOT NULL
            )
            """)

    def create_entry(self, slug: str, password: str, description: str = '') -> None:
        """
        Создаст новую запись в БД.

        - slug: значение для поля slug,
        - password: значение для поля password,
        - description: значение для поля description.
        """
        with self.connector(self.name_db) as cursor:
            cursor.execute(f"""
                INSERT INTO {self.name_table} (
                {self.field_slug}, {self.field_description}, {self.field_password}
                ) VALUES (?, ?, ?)""",
                (slug, description, password),
            )

    def get_by_slug_or_none(self, slug: str) -> dict[str, str] | None:
        """
        Получит данные из БД по slug и вернет их в виде словаря.

        - slug: значение поля slug, по которому будет происходить поиск.
        """
        with self.connector(self.name_db) as cursor:
            pre_result = cursor.execute(f"""
                SELECT {self.field_slug}, {self.field_description}, {self.field_password}
                FROM {self.name_table} WHERE {self.field_slug} = ?
                """,
                (slug,),
            ).fetchone()
            result = None if not pre_result else dict(zip(
                (self.field_slug, self.field_description, self.field_password),
                pre_result,
            ))
            return result


crud_payload = CRUDPayload(
    name_db=ConstantDataBase.name_db,
    name_table=ConstantDataBase.name_table_payload,
    connector=Connector,
    field_slug=ConstantDataBase.slug,
    field_description=ConstantDataBase.description,
    field_password=ConstantDataBase.password,
)
