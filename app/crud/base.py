from app.crud.manager import Connector


class CRUDBase:
    """Базовый класс управления БД."""

    def __init__(
        self,
        name_db: str,
        name_table: str,
        connector: type[Connector],
    ) -> None:
        """
        Параметры:
            name_db: название Базы данных;
            name_table: название таблицы в БД;
            connector: менеджер подключения к БД.
        """
        self.name_db = name_db
        self.name_table = name_table
        self.connector = connector

    def create_db(self) -> None:
        """Создание таблицы в БД."""
        raise NotImplementedError
