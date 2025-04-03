from database.constant import DefaultSetting
from database.manager import Connector


class CRUDBase:
    """Базовый класс управления БД."""

    def __init__(
        self,
        name_db: str,
        name_table: str,
        setting: type[DefaultSetting] = DefaultSetting,
        connector: type[Connector] = Connector,
    ) -> None:
        """
        ПараметрыЖ
            name_db: название Базы данных;
            name_table: название таблицы в БД;
            setting: класс с настройками приложения.
        """
        self.name_db = name_db
        self.name_table = name_table
        self.setting = setting
        self.connector = connector

    def create_db(self):
        """Создание таблицы в БД."""
        raise NotImplementedError
